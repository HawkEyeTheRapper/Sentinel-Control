import argparse
import json
import os
import re
import time
import urllib.error
import urllib.request

NOTION_VERSION = "2022-06-28"
API_BASE = "https://api.notion.com/v1"
MAX_TEXT = 1800
BLOCK_BATCH = 100


def load_token():
    token = os.environ.get("NOTION_TOKEN")
    if token:
        return token
    raise RuntimeError("NOTION_TOKEN is not set. Source /home/admiralswan/secrets/omni-env.sh before running.")


def notion_request(method, path, token, data=None, retry=3):
    url = API_BASE + path
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
    }
    body = None
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            payload = resp.read().decode("utf-8")
            return json.loads(payload) if payload else {}
    except urllib.error.HTTPError as e:
        if e.code == 429 and retry > 0:
            time.sleep(1.2)
            return notion_request(method, path, token, data, retry=retry - 1)
        error_body = e.read().decode("utf-8")
        raise RuntimeError(f"Notion API error {e.code}: {error_body}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Notion API network error: {e}")


def chunk_text(text, max_len=MAX_TEXT):
    chunks = []
    text = text.replace("\r\n", "\n")
    for i in range(0, len(text), max_len):
        chunks.append(text[i : i + max_len])
    return chunks


def text_to_blocks(text):
    blocks = []
    for chunk in chunk_text(text):
        blocks.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": chunk}}]
            },
        })
    return blocks


def clamp_text(text, limit=MAX_TEXT):
    if text is None:
        return ""
    return text[:limit]


def find_title_property(properties):
    for name, prop in properties.items():
        if prop.get("type") == "title":
            return name
    return None


def ensure_properties(token, db_id, existing_props, conv_prop, log_title_prop, slug_prop, tags_prop,
                      include_message_count=True, include_summary=True, include_accounts=True):
    desired = {
        log_title_prop: {"rich_text": {}},
        conv_prop: {"multi_select": {}},
        slug_prop: {"rich_text": {}},
        tags_prop: {"multi_select": {}},
    }
    if include_message_count:
        desired["Message Count"] = {"number": {"format": "number"}}
    if include_summary:
        desired["Summary"] = {"rich_text": {}}
    if include_accounts:
        desired["Accounts"] = {"multi_select": {}}
    updates = {}
    for name, definition in desired.items():
        if name in existing_props:
            continue
        updates[name] = definition
    if updates:
        notion_request("PATCH", f"/databases/{db_id}", token, {"properties": updates})
    return updates


def fetch_existing_pages(token, db_id, conv_prop):
    existing = {}
    cursor = None
    while True:
        payload = {"page_size": 100}
        if cursor:
            payload["start_cursor"] = cursor
        data = notion_request("POST", f"/databases/{db_id}/query", token, payload)
        for page in data.get("results", []):
            props = page.get("properties", {})
            conv = props.get(conv_prop, {})
            if conv.get("type") != "multi_select":
                continue
            for opt in conv.get("multi_select", []):
                name = opt.get("name")
                if not name:
                    continue
                existing.setdefault(name, []).append(page.get("id"))
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return existing


def archive_page(token, page_id):
    notion_request("PATCH", f"/pages/{page_id}", token, {"archived": True})


def page_has_children(token, page_id):
    data = notion_request("GET", f"/blocks/{page_id}/children?page_size=1", token)
    return len(data.get("results", [])) > 0


def append_blocks(token, page_id, blocks):
    for i in range(0, len(blocks), BLOCK_BATCH):
        chunk = blocks[i : i + BLOCK_BATCH]
        notion_request("PATCH", f"/blocks/{page_id}/children", token, {"children": chunk})
        time.sleep(0.35)


def strip_trailing_hash(value):
    if not value:
        return ""
    pattern = r"(?:[-_ ]+[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|[-_ ]+[0-9a-f]{16,})$"
    cleaned = re.sub(pattern, "", value, flags=re.IGNORECASE)
    return cleaned.rstrip(" -_")


def slugify(value):
    text = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return re.sub(r"-{2,}", "-", text)


def build_properties(title_prop, record, conv_prop, log_title_prop, slug_prop, tags_prop,
                     clean_log_title=False, slug_with_conv_id=False, extra_tags=None,
                     include_message_count=True, include_summary=True, include_accounts=True):
    title = clamp_text(record.get("Title", ""))
    log_title = clamp_text(record.get("Log Title", "")) or title
    if clean_log_title:
        log_title = clamp_text(strip_trailing_hash(log_title))
    conv_id = record.get("Conversation ID Tag", "") or record.get("Convo ID Tag", "")
    slug = clamp_text(record.get("Slug", ""))
    if slug_with_conv_id:
        base = slugify(log_title or title or "untitled")
        slug = f"{base}-{conv_id}" if conv_id else base
    message_count = record.get("Message Count")
    summary = clamp_text(record.get("Summary", ""))
    tags = record.get("Tags", "")
    accounts = record.get("Accounts", "")

    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    if extra_tags:
        tag_list.extend(extra_tags)
    tag_list = sorted(set(tag_list), key=str.lower)
    account_list = [a.strip() for a in accounts.split(",") if a.strip()]

    props = {
        title_prop: {"title": [{"type": "text", "text": {"content": title or log_title or "Untitled"}}]},
        log_title_prop: {"rich_text": [{"type": "text", "text": {"content": log_title or title}}]},
        conv_prop: {"multi_select": [{"name": conv_id}]} if conv_id else {"multi_select": []},
        slug_prop: {"rich_text": [{"type": "text", "text": {"content": slug}}]},
        tags_prop: {"multi_select": [{"name": t} for t in tag_list]},
    }
    if include_message_count:
        props["Message Count"] = {"number": message_count if isinstance(message_count, int) else None}
    if include_summary:
        props["Summary"] = {"rich_text": [{"type": "text", "text": {"content": summary}}]} if summary else {"rich_text": []}
    if include_accounts:
        props["Accounts"] = {"multi_select": [{"name": a} for a in account_list]}
    return props


def create_page(token, db_id, properties, blocks):
    payload = {
        "parent": {"database_id": db_id},
        "properties": properties,
    }
    if blocks:
        payload["children"] = blocks[:BLOCK_BATCH]
    page = notion_request("POST", "/pages", token, payload)
    page_id = page.get("id")
    remaining = blocks[BLOCK_BATCH:] if blocks else []
    if remaining:
        append_blocks(token, page_id, remaining)
    return page_id


def update_page_properties(token, page_id, properties):
    notion_request("PATCH", f"/pages/{page_id}", token, {"properties": properties})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db-id", required=True)
    parser.add_argument("--metadata", default="/home/admiralswan/Documents/everlight-conversation-hub-prep/metadata/conversation_hub_records.json")
    parser.add_argument("--state", default="/home/admiralswan/Documents/everlight-conversation-hub-prep/metadata/import_state.json")
    parser.add_argument("--conv-prop", default="Conversation ID Tag")
    parser.add_argument("--log-title-prop", default="Log Title")
    parser.add_argument("--slug-prop", default="Slug")
    parser.add_argument("--tags-prop", default="Tags")
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument("--clean-log-title", action="store_true")
    parser.add_argument("--slug-with-conv-id", action="store_true")
    parser.add_argument("--minimal", action="store_true")
    args = parser.parse_args()

    token = load_token()
    with open(args.metadata, "r") as f:
        records = json.load(f)

    try:
        db = notion_request("GET", f"/databases/{args.db_id}", token)
    except RuntimeError as exc:
        raise RuntimeError(f"Failed to access database {args.db_id}. Ensure the integration has access. {exc}")

    title_prop = find_title_property(db.get("properties", {}))
    if not title_prop:
        raise RuntimeError("No title property found on database.")

    ensure_properties(
        token,
        args.db_id,
        db.get("properties", {}),
        args.conv_prop,
        args.log_title_prop,
        args.slug_prop,
        args.tags_prop,
        include_message_count=not args.minimal,
        include_summary=not args.minimal,
        include_accounts=not args.minimal,
    )
    db = notion_request("GET", f"/databases/{args.db_id}", token)

    existing = fetch_existing_pages(token, args.db_id, args.conv_prop)
    duplicates = 0
    for conv_id, page_ids in existing.items():
        if len(page_ids) > 1:
            keep = page_ids[0]
            for dup in page_ids[1:]:
                archive_page(token, dup)
                duplicates += 1
                time.sleep(0.35)
            existing[conv_id] = [keep]

    state = {"processed": []}
    if os.path.exists(args.state):
        with open(args.state, "r") as f:
            state = json.load(f)
    processed = set(state.get("processed", []))

    created = 0
    updated = 0
    skipped = 0

    for idx, record in enumerate(records, start=1):
        conv_id = record.get("Conversation ID Tag", "") or record.get("Convo ID Tag", "")
        if not conv_id:
            skipped += 1
            continue
        if conv_id in processed:
            skipped += 1
            continue

        props = build_properties(
            title_prop,
            record,
            args.conv_prop,
            args.log_title_prop,
            args.slug_prop,
            args.tags_prop,
            clean_log_title=args.clean_log_title,
            slug_with_conv_id=args.slug_with_conv_id,
            extra_tags=args.tag,
            include_message_count=not args.minimal,
            include_summary=not args.minimal,
            include_accounts=not args.minimal,
        )
        content_path = record.get("Prepared Path")
        blocks = []
        if content_path and os.path.exists(content_path):
            with open(content_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            blocks = text_to_blocks(text)
        else:
            blocks = text_to_blocks("Content missing from source export.")

        existing_pages = existing.get(conv_id, [])
        if existing_pages:
            page_id = existing_pages[0]
            update_page_properties(token, page_id, props)
            time.sleep(0.35)
            if not page_has_children(token, page_id):
                append_blocks(token, page_id, blocks)
            updated += 1
        else:
            create_page(token, args.db_id, props, blocks)
            created += 1

        processed.add(conv_id)
        state["processed"] = sorted(processed)
        with open(args.state, "w") as f:
            json.dump(state, f, indent=2)
        if idx % 10 == 0:
            print(f"Processed {idx}/{len(records)} (created {created}, updated {updated}, skipped {skipped}, dup-archived {duplicates})")
        time.sleep(0.35)

    print(f"Done. Created {created}, updated {updated}, skipped {skipped}, dup-archived {duplicates}.")


if __name__ == "__main__":
    main()
