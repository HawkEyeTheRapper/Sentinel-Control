# EverLight Sentinel MCP

Cloudflare-hosted MCP service for EverLight conversation logs. Metadata lives in D1 and log bodies live in R2.

## Endpoints

- `https://api.aetheranalysis.com/mcp/`
- `https://mcp.everlightos.com/mcp/`

Transport: streamable-http (MCP over HTTP). No auth required.

## Tools

- `list_logs` - List log metadata, optional tag filter.
- `get_log_by_conversation_id` - Fetch metadata by Convo ID.
- `get_log_by_slug` - Fetch metadata by slug.
- `search_logs` - Search by title, log title, or summary.
- `get_log_content` - Fetch full log content from R2.

## Client Setup

### Canonical MCP Client Config (streamable-http)

Use this wherever remote MCP servers are supported:

```json
{
  "mcpServers": {
    "everlight-sentinel": {
      "transport": "streamable-http",
      "url": "https://api.aetheranalysis.com/mcp/"
    }
  }
}
```

### OpenWebUI

If your OpenWebUI build supports remote MCP servers, add a new MCP server:

- Name: `everlight-sentinel`
- URL: `https://api.aetheranalysis.com/mcp/`
- Transport: `streamable-http`
- Auth: none

If your OpenWebUI only supports stdio MCP, use the local bridge (see Bridge Zone section) and point OpenWebUI to that command.

### Claude Desktop

Claude Desktop expects local stdio MCP servers. Use the local bridge and point Claude to the script. Example config:

```json
{
  "mcpServers": {
    "everlight-sentinel": {
      "command": "node",
      "args": [
        "/home/admiralswan/Documents/everlight-conversation-hub-prep/everlight-mcp-worker/scripts/mcp_stdio_bridge.js"
      ],
      "env": {
        "MCP_REMOTE_URL": "https://api.aetheranalysis.com/mcp/"
      }
    }
  }
}
```

Place this in your Claude Desktop MCP config file (path varies by OS; on Linux it is typically under `~/.config`).

### Codex CLI, Microsoft Copilot, Gemini, ChatGPT

These do not currently expose native MCP client configuration. To use the MCP data, we can:

- Add a local MCP bridge and point the tool/plugin layer to it, or
- Expose a thin HTTP JSON wrapper around the MCP tools for those clients.

Tell me which client you want first and I will wire the recommended path.

## Bridge Zone Local Bridge

The local bridge is the “Bridge Zone” between stdio MCP clients and the remote streamable-http MCP endpoint.

Run it directly:

```bash
MCP_REMOTE_URL="https://api.aetheranalysis.com/mcp/" \
  node /home/admiralswan/Documents/everlight-conversation-hub-prep/everlight-mcp-worker/scripts/mcp_stdio_bridge.js
```

If the client spawns the bridge, set the command to the script and provide `MCP_REMOTE_URL` in the environment.

## HTTP JSON Wrapper

For non-MCP clients, a JSON wrapper is exposed at:

- `https://api.aetheranalysis.com/mcp-json`
- `https://mcp.everlightos.com/mcp-json`

Example:

```bash
curl -sS https://api.aetheranalysis.com/mcp-json \
  -H "Content-Type: application/json" \
  -d '{"tool":"list_logs","args":{"limit":3}}'
```

## Verification (copy-paste)

### 1) Metadata count (D1)

```bash
source /home/admiralswan/secrets/omni-env.sh
export CLOUDFLARE_API_TOKEN="$CF_API_TOKEN"
wrangler d1 execute everlight_sentinel --remote --command "SELECT COUNT(*) AS total FROM logs;"
```

Expected: `total` equals the number of log files (currently 802).

### 2) list_logs

```bash
curl -sS https://api.aetheranalysis.com/mcp-json \
  -H "Content-Type: application/json" \
  -d '{"tool":"list_logs","args":{"limit":2}}'
```

Expected: JSON with `tool` = `list_logs` and a `result` array of log metadata.

### 3) get_log_by_slug

```bash
curl -sS https://api.aetheranalysis.com/mcp-json \
  -H "Content-Type: application/json" \
  -d '{"tool":"get_log_content","args":{"slug":"folder-check-and-dive-68644222-7fb0-8011-84e0-2db100a61e33"}}'
```

Expected: JSON containing `content` with the Markdown log body.

### 4) get_log_by_conversation_id

```bash
curl -sS https://api.aetheranalysis.com/mcp-json \
  -H "Content-Type: application/json" \
  -d '{"tool":"get_log_by_conversation_id","args":{"conversation_id":"68644222-7fb0-8011-84e0-2db100a61e33"}}'
```

Expected: JSON with `slug`, `title`, and `r2_key`.

### 5) search_logs (partial match)

```bash
curl -sS https://api.aetheranalysis.com/mcp-json \
  -H "Content-Type: application/json" \
  -d '{"tool":"search_logs","args":{"query":"kamikaze","limit":3}}'
```

Expected: JSON `result` array containing matching logs.

## Data Roles

- D1 (`everlight_sentinel`) stores metadata and indexing fields (slug, convo ID, tags, summary).
- R2 (`everlight-mcp-logs`) stores the full Markdown log bodies under `logs/`.

## Notes

- Logs are stored in R2 under `logs/`.
- Metadata is stored in D1 (`everlight_sentinel`).
