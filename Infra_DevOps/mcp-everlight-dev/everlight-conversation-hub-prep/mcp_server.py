import os

from mcp.server.fastmcp import FastMCP

from notion_client import NotionClient, rich_text_to_plain

mcp = FastMCP("EverLight Conversation Hub")


def resolve_db_id(db_id):
    if db_id:
        return db_id
    env_id = os.environ.get("NOTION_DB_ID")
    if env_id:
        return env_id
    raise RuntimeError("NOTION_DB_ID is not set and no db_id was provided.")


def blocks_to_text(blocks):
    lines = []
    for block in blocks:
        btype = block.get("type")
        data = block.get(btype, {}) if btype else {}
        text = rich_text_to_plain(data.get("rich_text", []))
        if not text:
            continue
        if btype == "heading_1":
            lines.append(f"# {text}")
        elif btype == "heading_2":
            lines.append(f"## {text}")
        elif btype == "heading_3":
            lines.append(f"### {text}")
        elif btype == "bulleted_list_item":
            lines.append(f"- {text}")
        elif btype == "numbered_list_item":
            lines.append(f"1. {text}")
        elif btype == "quote":
            lines.append(f"> {text}")
        elif btype == "code":
            language = data.get("language") or ""
            lines.append(f"```{language}\n{text}\n```")
        else:
            lines.append(text)
    return "\n".join(lines).strip()


@mcp.tool()
def list_databases(query: str | None = None, limit: int = 20):
    """List accessible Notion databases. Use this to find the correct database ID."""
    client = NotionClient.from_env()
    return client.list_databases(query=query, limit=limit)


@mcp.tool()
def list_logs(limit: int = 50, cursor: str | None = None, db_id: str | None = None):
    """List logs in the Notion database with pagination."""
    client = NotionClient.from_env()
    db_id = resolve_db_id(db_id)
    data = client.query_database(db_id, start_cursor=cursor, page_size=min(100, max(1, limit)))
    items = [client.extract_properties(page) for page in data.get("results", [])]
    return {
        "items": items,
        "next_cursor": data.get("next_cursor"),
        "has_more": data.get("has_more", False),
    }


@mcp.tool()
def get_log_by_conversation_id(conversation_id: str, db_id: str | None = None):
    """Fetch a log by Conversation ID Tag."""
    client = NotionClient.from_env()
    db_id = resolve_db_id(db_id)
    filter_obj = {
        "property": "Conversation ID Tag",
        "multi_select": {"contains": conversation_id},
    }
    data = client.query_database(db_id, filter_obj=filter_obj)
    results = data.get("results", [])
    return [client.extract_properties(page) for page in results]


@mcp.tool()
def get_log_by_slug(slug: str, db_id: str | None = None):
    """Fetch a log by its Slug property."""
    client = NotionClient.from_env()
    db_id = resolve_db_id(db_id)
    filter_obj = {
        "property": "Slug",
        "rich_text": {"equals": slug},
    }
    data = client.query_database(db_id, filter_obj=filter_obj)
    results = data.get("results", [])
    return [client.extract_properties(page) for page in results]


@mcp.tool()
def get_log_content(page_id: str):
    """Fetch the plain text content for a Notion page."""
    client = NotionClient.from_env()
    blocks = client.get_page_blocks(page_id)
    return {
        "page_id": page_id,
        "block_count": len(blocks),
        "content": blocks_to_text(blocks),
    }


@mcp.tool()
def search_logs(query: str, limit: int = 10, db_id: str | None = None):
    """Search logs using Notion's search API, then filter to the target database."""
    client = NotionClient.from_env()
    db_id = resolve_db_id(db_id)
    results = []
    cursor = None
    while len(results) < limit:
        data = client.search(query=query, filter_obj={"property": "object", "value": "page"}, start_cursor=cursor)
        for page in data.get("results", []):
            parent = page.get("parent", {})
            if parent.get("type") != "database_id":
                continue
            if parent.get("database_id") != db_id:
                continue
            results.append(client.extract_properties(page))
            if len(results) >= limit:
                break
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return results


if __name__ == "__main__":
    mcp.run()
