#!/usr/bin/env node
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import * as z from "zod/v4";

const DEFAULT_REMOTE_URL = "https://api.aetheranalysis.com/mcp/";
const MAX_LIMIT = 200;

const normalizeRemoteUrl = (value) => {
  const url = new URL(value);
  if (!url.pathname.endsWith("/mcp") && !url.pathname.endsWith("/mcp/")) {
    url.pathname = `${url.pathname.replace(/\/+$/, "")}/mcp/`;
  }
  if (url.pathname.endsWith("/mcp")) {
    url.pathname = `${url.pathname}/`;
  }
  return url;
};

const listLogsSchema = z.object({
  limit: z.coerce.number().min(1).max(MAX_LIMIT).default(50),
  offset: z.coerce.number().min(0).default(0),
  tag: z.string().optional(),
});

const getLogByConversationIdSchema = z.object({
  conversation_id: z.string().min(1),
});

const getLogBySlugSchema = z.object({
  slug: z.string().min(1),
});

const searchLogsSchema = z.object({
  query: z.string().min(2),
  limit: z.coerce.number().min(1).max(MAX_LIMIT).default(20),
});

const getLogContentSchema = z
  .object({
    conversation_id: z.string().optional(),
    slug: z.string().optional(),
  })
  .refine((value) => Boolean(value.conversation_id || value.slug), {
    message: "Provide conversation_id or slug.",
  });

const remoteInput = process.env.MCP_REMOTE_URL || process.argv[2] || DEFAULT_REMOTE_URL;
const remoteUrl = normalizeRemoteUrl(remoteInput);

const client = new Client({ name: "everlight-sentinel-bridge", version: "1.0.0" });
const clientTransport = new StreamableHTTPClientTransport(remoteUrl);

await client.connect(clientTransport);
await client.listTools();

const server = new McpServer({ name: "everlight-sentinel-bridge", version: "1.0.0" });

const callRemote = async (name, params) => {
  return client.callTool({ name, arguments: params ?? {} });
};

server.registerTool(
  "list_logs",
  { description: "List logs with optional tag filter.", inputSchema: listLogsSchema },
  async (params) => callRemote("list_logs", params)
);

server.registerTool(
  "get_log_by_conversation_id",
  { description: "Fetch metadata by conversation ID tag.", inputSchema: getLogByConversationIdSchema },
  async (params) => callRemote("get_log_by_conversation_id", params)
);

server.registerTool(
  "get_log_by_slug",
  { description: "Fetch metadata by slug.", inputSchema: getLogBySlugSchema },
  async (params) => callRemote("get_log_by_slug", params)
);

server.registerTool(
  "search_logs",
  { description: "Search logs by title, log title, or summary.", inputSchema: searchLogsSchema },
  async (params) => callRemote("search_logs", params)
);

server.registerTool(
  "get_log_content",
  { description: "Fetch full log content from R2 using convo_id or slug.", inputSchema: getLogContentSchema },
  async (params) => callRemote("get_log_content", params)
);

const stdio = new StdioServerTransport();
await server.connect(stdio);

console.error(`[bridge] EverLight Sentinel MCP bridge online -> ${remoteUrl.toString()}`);

const shutdown = async () => {
  try {
    await server.close();
  } catch {
    // ignore
  }
  try {
    if (typeof client.close === "function") {
      await client.close();
    }
  } catch {
    // ignore
  }
};

process.on("SIGINT", () => {
  void shutdown().finally(() => process.exit(0));
});
process.on("SIGTERM", () => {
  void shutdown().finally(() => process.exit(0));
});
