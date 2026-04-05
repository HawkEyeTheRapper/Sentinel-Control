#!/usr/bin/env bash
set -euo pipefail

BUCKET=${1:-}
SOURCE=${2:-}

if [[ -z "$BUCKET" || -z "$SOURCE" ]]; then
  echo "Usage: upload_r2_remote.sh <bucket> <source>"
  exit 1
fi

if [[ ! -d "$SOURCE" ]]; then
  echo "Source folder not found: $SOURCE"
  exit 1
fi

SOURCE=$(cd "$SOURCE" && pwd)
SOURCE=${SOURCE%/}

while IFS= read -r -d '' file; do
  rel="${file#"$SOURCE"/}"
  wrangler r2 object put "$BUCKET/$rel" --file "$file" --remote
  
  # avoid hammering
  sleep 0.05

done < <(find "$SOURCE" -type f -print0)

echo "R2 upload complete (remote)."
