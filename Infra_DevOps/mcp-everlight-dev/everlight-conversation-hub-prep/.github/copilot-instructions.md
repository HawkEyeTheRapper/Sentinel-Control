# EverLight Conversation Hub - AI Coding Guidelines

## Architecture Overview
This project syncs conversation logs from a Notion database to Cloudflare D1 (metadata) and R2 (content) for high-performance MCP access. Local Python MCP server (`mcp_server.py`) provides development access; Cloudflare Worker (`everlight-mcp-worker/`) serves production remote MCP over streamable-HTTP.

**Key Components:**
- `notion_client.py`: Notion API wrapper with pagination and property extraction
- `import_to_notion.py`: Imports markdown logs into Notion pages with block batching
- `scripts/build_sentinel_seed.py`: Generates D1 SQL from Notion metadata export
- `everlight-mcp-worker/src/index.ts`: TypeScript MCP server with Zod validation

**Data Flow:** Markdown logs → Notion database → Export metadata → Seed D1/R2 → MCP tools query D1 and fetch from R2

## Critical Workflows
- **Local MCP Development:** `source /home/admiralswan/secrets/omni-env.sh && python mcp_server.py` (requires NOTION_TOKEN, NOTION_DB_ID)
- **Sync to Cloudflare:** Run `python scripts/build_sentinel_seed.py` to generate SQL, then `wrangler d1 execute everlight_sentinel --local --file=metadata/sentinel_seed.sql`
- **Deploy Worker:** `cd everlight-mcp-worker && wrangler deploy`
- **Verify Deployment:** Use curl commands from README.md for JSON wrapper testing

## Project Conventions
- **MCP Tools:** Use FastMCP (Python) or @modelcontextprotocol/sdk (TypeScript) with Zod schemas for validation
- **Notion Properties:** Access via `client.extract_properties(page)`; handle multi-select as arrays, rich_text as plain strings
- **Error Handling:** Retry 429s in Notion API calls; use HttpError in Worker for status codes
- **Environment:** Source `omni-env.sh` for secrets; avoid hardcoding tokens

## Integration Patterns
- **Notion API:** Paginate with `start_cursor`; filter databases by `multi_select` or `rich_text` properties
- **Cloudflare Bindings:** Bind D1 as `LOGS_DB`, R2 as `LOG_BUCKET`; use prepared statements for D1 queries
- **MCP Transport:** Local stdio for development; streamable-HTTP for remote clients via bridge script

Reference: [README.md](../README.md) for client configs; [notion_client.py](../notion_client.py) for API patterns; [everlight-mcp-worker/src/index.ts](../everlight-mcp-worker/src/index.ts) for production MCP implementation</content>
<parameter name="filePath">/home/admiralswan/Documents/everlight-conversation-hub-prep/.github/copilot-instructions.md