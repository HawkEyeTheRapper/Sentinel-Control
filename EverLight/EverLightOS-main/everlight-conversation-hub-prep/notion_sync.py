import argparse
import json
from pathlib import Path

from notion_client import NotionClient, load_token


def list_databases(client, query, limit):
    results = client.list_databases(query=query, limit=limit)
    if not results:
        print("No databases found.")
        return 1
    for db in results:
        title = db.get("title") or "(untitled)"
        print(f"{title} | {db.get('id')} | {db.get('url')}")
    return 0


def export_page_map(client, db_id, output_path):
    records = []
    for page in client.iter_database_pages(db_id):
        records.append(client.extract_properties(page))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(records, indent=2), encoding="utf-8")
    print(f"Wrote {len(records)} records to {output_path}")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db-id")
    parser.add_argument("--db-name", default=None)
    parser.add_argument("--out", default="metadata/notion_page_map.json")
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--list-databases", action="store_true")
    args = parser.parse_args()

    token = load_token()
    client = NotionClient(token)

    if args.list_databases or not args.db_id:
        exit_code = list_databases(client, args.db_name, args.limit)
        if not args.db_id:
            return exit_code

    db_id = args.db_id
    output_path = Path(args.out)
    return export_page_map(client, db_id, output_path)


if __name__ == "__main__":
    raise SystemExit(main())
