import json
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RECORDS_PATH = BASE_DIR / "metadata" / "conversation_hub_records.json"
OUTPUT_PATH = BASE_DIR / "metadata" / "sentinel_seed.sql"
LOGS_DIR = BASE_DIR / "logs"


def strip_trailing_hash(value: str) -> str:
    if not value:
        return ""
    pattern = r"(?:[-_ ]+[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|[-_ ]+[0-9a-f]{16,})$"
    cleaned = re.sub(pattern, "", value, flags=re.IGNORECASE)
    return cleaned.rstrip(" -_")


def slugify(value: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return re.sub(r"-{2,}", "-", text)


def sql_escape(value: str) -> str:
    return value.replace("'", "''")


def main() -> None:
    records = json.loads(RECORDS_PATH.read_text(encoding="utf-8"))
    lines = [
        "CREATE TABLE IF NOT EXISTS logs (",
        "  convo_id TEXT PRIMARY KEY,",
        "  title TEXT,",
        "  log_title TEXT,",
        "  slug TEXT,",
        "  summary TEXT,",
        "  message_count INTEGER,",
        "  tags TEXT,",
        "  accounts TEXT,",
        "  r2_key TEXT",
        ");",
        "CREATE INDEX IF NOT EXISTS idx_logs_slug ON logs(slug);",
        "CREATE INDEX IF NOT EXISTS idx_logs_title ON logs(title);",
        "CREATE INDEX IF NOT EXISTS idx_logs_log_title ON logs(log_title);",
        "DELETE FROM logs;",
    ]

    for record in records:
        convo_id = record.get("Conversation ID Tag", "") or record.get("Convo ID Tag", "")
        if not convo_id:
            continue
        title = record.get("Title", "") or "Untitled"
        log_title = record.get("Log Title", "") or title
        log_title = strip_trailing_hash(log_title)
        slug = record.get("Slug", "")
        if not slug:
            slug = f"{slugify(log_title or title)}-{convo_id}" if convo_id else slugify(log_title or title)
        summary = record.get("Summary", "") or ""
        message_count = record.get("Message Count")
        tags = [t.strip() for t in (record.get("Tags", "") or "").split(",") if t.strip()]
        if "NEW" not in tags:
            tags.append("NEW")
        accounts = [a.strip() for a in (record.get("Accounts", "") or "").split(",") if a.strip()]
        prepared = record.get("Prepared Path", "")
        filename = os.path.basename(prepared) if prepared else f"{slug}.md"
        r2_key = f"logs/{filename}"

        lines.append(
            "INSERT OR REPLACE INTO logs (convo_id, title, log_title, slug, summary, message_count, tags, accounts, r2_key) VALUES ("
            f"'{sql_escape(convo_id)}',"
            f"'{sql_escape(title)}',"
            f"'{sql_escape(log_title)}',"
            f"'{sql_escape(slug)}',"
            f"'{sql_escape(summary)}',"
            f"{int(message_count) if isinstance(message_count, int) else 'NULL'},"
            f"'{sql_escape(json.dumps(tags))}',"
            f"'{sql_escape(json.dumps(accounts))}',"
            f"'{sql_escape(r2_key)}'"
            ");"
        )

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
