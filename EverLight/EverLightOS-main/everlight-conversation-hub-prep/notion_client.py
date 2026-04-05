import json
import os
import time
import urllib.error
import urllib.request

NOTION_VERSION = "2022-06-28"
API_BASE = "https://api.notion.com/v1"
DEFAULT_PAGE_SIZE = 100


def load_token():
    token = os.environ.get("NOTION_TOKEN")
    if token:
        return token
    raise RuntimeError("NOTION_TOKEN is not set. Source /home/admiralswan/secrets/omni-env.sh before running.")


def rich_text_to_plain(rich_text):
    if not rich_text:
        return ""
    return "".join(part.get("plain_text", "") for part in rich_text)


def get_title_property_name(properties):
    for name, prop in properties.items():
        if prop.get("type") == "title":
            return name
    return None


def get_rich_text_value(properties, name):
    prop = properties.get(name, {})
    if prop.get("type") != "rich_text":
        return ""
    return rich_text_to_plain(prop.get("rich_text", []))


def get_multi_select_values(properties, name):
    prop = properties.get(name, {})
    if prop.get("type") != "multi_select":
        return []
    return [item.get("name") for item in prop.get("multi_select", []) if item.get("name")]


def get_first_multi_select_values(properties, names):
    for name in names:
        values = get_multi_select_values(properties, name)
        if values:
            return values
    return []


def get_number_value(properties, name):
    prop = properties.get(name, {})
    if prop.get("type") != "number":
        return None
    return prop.get("number")


class NotionClient:
    def __init__(self, token, db_id=None):
        self.token = token
        self.db_id = db_id

    @classmethod
    def from_env(cls, db_env="NOTION_DB_ID"):
        return cls(load_token(), os.environ.get(db_env))

    def request(self, method, path, data=None, retry=3):
        url = API_BASE + path
        headers = {
            "Authorization": f"Bearer {self.token}",
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
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and retry > 0:
                time.sleep(1.2)
                return self.request(method, path, data, retry=retry - 1)
            error_body = exc.read().decode("utf-8")
            raise RuntimeError(f"Notion API error {exc.code}: {error_body}")
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Notion API network error: {exc}")

    def search(self, query=None, filter_obj=None, start_cursor=None, page_size=DEFAULT_PAGE_SIZE):
        payload = {"page_size": page_size}
        if query:
            payload["query"] = query
        if filter_obj:
            payload["filter"] = filter_obj
        if start_cursor:
            payload["start_cursor"] = start_cursor
        return self.request("POST", "/search", payload)

    def list_databases(self, query=None, limit=50):
        results = []
        cursor = None
        while True:
            page_size = min(DEFAULT_PAGE_SIZE, max(1, limit - len(results)))
            data = self.search(
                query=query,
                filter_obj={"property": "object", "value": "database"},
                start_cursor=cursor,
                page_size=page_size,
            )
            for db in data.get("results", []):
                title = rich_text_to_plain(db.get("title", []))
                results.append({
                    "id": db.get("id"),
                    "title": title,
                    "url": db.get("url"),
                })
                if len(results) >= limit:
                    return results
            if not data.get("has_more"):
                break
            cursor = data.get("next_cursor")
        return results

    def query_database(self, db_id, filter_obj=None, sorts=None, start_cursor=None, page_size=DEFAULT_PAGE_SIZE):
        payload = {"page_size": page_size}
        if filter_obj:
            payload["filter"] = filter_obj
        if sorts:
            payload["sorts"] = sorts
        if start_cursor:
            payload["start_cursor"] = start_cursor
        return self.request("POST", f"/databases/{db_id}/query", payload)

    def iter_database_pages(self, db_id, filter_obj=None, sorts=None):
        cursor = None
        while True:
            data = self.query_database(db_id, filter_obj=filter_obj, sorts=sorts, start_cursor=cursor)
            for page in data.get("results", []):
                yield page
            if not data.get("has_more"):
                break
            cursor = data.get("next_cursor")

    def get_page_blocks(self, page_id):
        blocks = []
        cursor = None
        while True:
            path = f"/blocks/{page_id}/children?page_size={DEFAULT_PAGE_SIZE}"
            if cursor:
                path += f"&start_cursor={cursor}"
            data = self.request("GET", path)
            blocks.extend(data.get("results", []))
            if not data.get("has_more"):
                break
            cursor = data.get("next_cursor")
        return blocks

    def extract_properties(self, page):
        props = page.get("properties", {})
        title_prop = get_title_property_name(props)
        title = ""
        if title_prop:
            title = rich_text_to_plain(props.get(title_prop, {}).get("title", []))

        return {
            "page_id": page.get("id"),
            "url": page.get("url"),
            "title": title,
            "log_title": get_rich_text_value(props, "Log Title") or title,
            "conversation_id_tags": get_first_multi_select_values(props, ["Conversation ID Tag", "Convo ID Tag"]),
            "slug": get_rich_text_value(props, "Slug"),
            "message_count": get_number_value(props, "Message Count"),
            "summary": get_rich_text_value(props, "Summary"),
            "tags": get_multi_select_values(props, "Tags"),
            "accounts": get_multi_select_values(props, "Accounts"),
            "created_time": page.get("created_time"),
            "last_edited_time": page.get("last_edited_time"),
        }
