import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { WebStandardStreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/webStandardStreamableHttp.js";
import * as z from "zod/v4";

type Env = {
  LOGS_DB: D1Database;
  LOG_BUCKET: R2Bucket;
  LOG_PREFIX: string;
};

type LogRecord = {
  convo_id: string;
  title: string;
  log_title: string;
  slug: string;
  summary: string | null;
  message_count: number | null;
  tags: string[];
  accounts: string[];
  r2_key: string;
};

const MAX_LIMIT = 200;
const SELECT_COLUMNS =
  "convo_id, title, log_title, slug, summary, message_count, tags, accounts, r2_key";

class HttpError extends Error {
  status: number;

  constructor(status: number, message: string) {
    super(message);
    this.status = status;
  }
}

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

const parseJsonArray = (value: unknown): string[] => {
  if (!value) {
    return [];
  }
  if (Array.isArray(value)) {
    return value.map(String);
  }
  try {
    const parsed = JSON.parse(String(value));
    return Array.isArray(parsed) ? parsed.map(String) : [];
  } catch {
    return [];
  }
};

const rowToRecord = (row: Record<string, unknown>): LogRecord => {
  return {
    convo_id: String(row.convo_id ?? ""),
    title: String(row.title ?? ""),
    log_title: String(row.log_title ?? ""),
    slug: String(row.slug ?? ""),
    summary: row.summary ? String(row.summary) : null,
    message_count: row.message_count === null || row.message_count === undefined ? null : Number(row.message_count),
    tags: parseJsonArray(row.tags),
    accounts: parseJsonArray(row.accounts),
    r2_key: String(row.r2_key ?? ""),
  };
};

const listLogs = async (env: Env, params: unknown) => {
  const { limit, offset, tag } = listLogsSchema.parse(params ?? {});
  const where = tag ? "WHERE tags LIKE ?" : "";
  const sql = `SELECT ${SELECT_COLUMNS} FROM logs ${where} ORDER BY rowid LIMIT ? OFFSET ?`;
  const stmt = env.LOGS_DB.prepare(sql);
  const bound = tag ? stmt.bind(`%\"${tag}\"%`, limit, offset) : stmt.bind(limit, offset);
  const result = await bound.all();
  const items = (result.results || []).map(rowToRecord);
  return { items };
};

const getLogByConversationId = async (env: Env, params: unknown) => {
  const { conversation_id } = getLogByConversationIdSchema.parse(params ?? {});
  const result = await env.LOGS_DB.prepare(
    `SELECT ${SELECT_COLUMNS} FROM logs WHERE convo_id = ? LIMIT 1`
  )
    .bind(conversation_id)
    .first();
  return result ? rowToRecord(result as Record<string, unknown>) : null;
};

const getLogBySlug = async (env: Env, params: unknown) => {
  const { slug } = getLogBySlugSchema.parse(params ?? {});
  const result = await env.LOGS_DB.prepare(
    `SELECT ${SELECT_COLUMNS} FROM logs WHERE slug = ? LIMIT 1`
  )
    .bind(slug)
    .first();
  return result ? rowToRecord(result as Record<string, unknown>) : null;
};

const searchLogs = async (env: Env, params: unknown) => {
  const { query, limit } = searchLogsSchema.parse(params ?? {});
  const needle = `%${query.toLowerCase()}%`;
  const result = await env.LOGS_DB
    .prepare(
      `SELECT ${SELECT_COLUMNS} FROM logs WHERE lower(title) LIKE ? OR lower(log_title) LIKE ? OR lower(summary) LIKE ? ORDER BY rowid LIMIT ?`
    )
    .bind(needle, needle, needle, limit)
    .all();
  const items = (result.results || []).map(rowToRecord);
  return { items };
};

const getLogContent = async (env: Env, params: unknown) => {
  const { conversation_id, slug } = getLogContentSchema.parse(params ?? {});
  const field = conversation_id ? "convo_id" : "slug";
  const value = conversation_id ?? slug ?? "";
  const result = await env.LOGS_DB.prepare(
    `SELECT ${SELECT_COLUMNS} FROM logs WHERE ${field} = ? LIMIT 1`
  )
    .bind(value)
    .first();
  if (!result) {
    return { record: null, content: null };
  }
  const record = rowToRecord(result as Record<string, unknown>);
  const key = record.r2_key || `${env.LOG_PREFIX}${record.slug}.md`;
  const obj = await env.LOG_BUCKET.get(key);
  if (!obj) {
    return { record, content: null };
  }
  const text = await obj.text();
  return { record, content: text };
};

const createServer = (env: Env) => {
  const server = new McpServer({
    name: "everlight-sentinel-mcp",
    version: "1.0.0",
  });

  server.registerTool(
    "list_logs",
    {
      description: "List logs with optional tag filter.",
      inputSchema: listLogsSchema,
    },
    async (params) => {
      const { items } = await listLogs(env, params);
      return {
        content: [{ type: "text", text: JSON.stringify(items, null, 2) }],
        structuredContent: { items },
      };
    }
  );

  server.registerTool(
    "get_log_by_conversation_id",
    {
      description: "Fetch metadata by conversation ID tag.",
      inputSchema: getLogByConversationIdSchema,
    },
    async (params) => {
      const record = await getLogByConversationId(env, params);
      if (!record) {
        return {
          content: [{ type: "text", text: "Log not found." }],
          isError: true,
        };
      }
      return {
        content: [{ type: "text", text: JSON.stringify(record, null, 2) }],
        structuredContent: record,
      };
    }
  );

  server.registerTool(
    "get_log_by_slug",
    {
      description: "Fetch metadata by slug.",
      inputSchema: getLogBySlugSchema,
    },
    async (params) => {
      const record = await getLogBySlug(env, params);
      if (!record) {
        return {
          content: [{ type: "text", text: "Log not found." }],
          isError: true,
        };
      }
      return {
        content: [{ type: "text", text: JSON.stringify(record, null, 2) }],
        structuredContent: record,
      };
    }
  );

  server.registerTool(
    "search_logs",
    {
      description: "Search logs by title, log title, or summary.",
      inputSchema: searchLogsSchema,
    },
    async (params) => {
      const { items } = await searchLogs(env, params);
      return {
        content: [{ type: "text", text: JSON.stringify(items, null, 2) }],
        structuredContent: { items },
      };
    }
  );

  server.registerTool(
    "get_log_content",
    {
      description: "Fetch full log content from R2 using convo_id or slug.",
      inputSchema: getLogContentSchema,
    },
    async (params) => {
      const { record, content } = await getLogContent(env, params);
      if (!record) {
        return {
          content: [{ type: "text", text: "Log not found." }],
          isError: true,
        };
      }
      if (!content) {
        return {
          content: [{ type: "text", text: "Content missing in R2." }],
          isError: true,
        };
      }
      return {
        content: [{ type: "text", text: content }],
        structuredContent: {
          convo_id: record.convo_id,
          slug: record.slug,
          title: record.title,
          log_title: record.log_title,
          content,
        },
      };
    }
  );

  return server;
};

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    const trimmedPath = url.pathname.replace(/\/+$/, "");
    const isJsonWrapper = trimmedPath === "/mcp-json" || trimmedPath === "/mcp/json";

    if (isJsonWrapper) {
      const corsHeaders = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
      };

      if (request.method === "OPTIONS") {
        return new Response(null, { status: 204, headers: corsHeaders });
      }

      if (request.method === "GET") {
        const tools = [
          "list_logs",
          "get_log_by_conversation_id",
          "get_log_by_slug",
          "search_logs",
          "get_log_content",
        ];
        return new Response(
          JSON.stringify(
            {
              tools,
              usage: {
                endpoint: "/mcp-json",
                body: { tool: "list_logs", args: { limit: 10 } },
              },
            },
            null,
            2
          ),
          {
            status: 200,
            headers: { "Content-Type": "application/json", ...corsHeaders },
          }
        );
      }

      if (request.method !== "POST") {
        return new Response(
          JSON.stringify({ error: "Method not allowed." }),
          {
            status: 405,
            headers: { "Content-Type": "application/json", ...corsHeaders },
          }
        );
      }

      let payload: { tool?: string; name?: string; args?: unknown; arguments?: unknown; params?: unknown };
      try {
        payload = await request.json();
      } catch {
        return new Response(JSON.stringify({ error: "Invalid JSON body." }), {
          status: 400,
          headers: { "Content-Type": "application/json", ...corsHeaders },
        });
      }

      const tool = payload.tool ?? payload.name;
      const args = payload.args ?? payload.arguments ?? payload.params ?? {};

      const handlers: Record<string, (input: unknown) => Promise<unknown>> = {
        list_logs: async (input) => (await listLogs(env, input)).items,
        get_log_by_conversation_id: async (input) => {
          const record = await getLogByConversationId(env, input);
          if (!record) {
            throw new HttpError(404, "Log not found.");
          }
          return record;
        },
        get_log_by_slug: async (input) => {
          const record = await getLogBySlug(env, input);
          if (!record) {
            throw new HttpError(404, "Log not found.");
          }
          return record;
        },
        search_logs: async (input) => (await searchLogs(env, input)).items,
        get_log_content: async (input) => {
          const { record, content } = await getLogContent(env, input);
          if (!record) {
            throw new HttpError(404, "Log not found.");
          }
          if (!content) {
            throw new HttpError(404, "Content missing in R2.");
          }
          return {
            convo_id: record.convo_id,
            slug: record.slug,
            title: record.title,
            log_title: record.log_title,
            content,
          };
        },
      };

      if (!tool || !(tool in handlers)) {
        return new Response(
          JSON.stringify({ error: "Unknown tool.", available_tools: Object.keys(handlers) }),
          {
            status: 400,
            headers: { "Content-Type": "application/json", ...corsHeaders },
          }
        );
      }

      try {
        const result = await handlers[tool](args);
        return new Response(JSON.stringify({ tool, result }, null, 2), {
          status: 200,
          headers: { "Content-Type": "application/json", ...corsHeaders },
        });
      } catch (error) {
        const status = error instanceof HttpError ? error.status : 500;
        const message = error instanceof Error ? error.message : "Unexpected error.";
        return new Response(JSON.stringify({ error: message }), {
          status,
          headers: { "Content-Type": "application/json", ...corsHeaders },
        });
      }
    }

    if (!url.pathname.startsWith("/mcp")) {
      return new Response("Not Found", { status: 404 });
    }

    const server = createServer(env);
    const transport = new WebStandardStreamableHTTPServerTransport({
      sessionIdGenerator: undefined,
    });

    await server.connect(transport);
    const response = await transport.handleRequest(request);
    return response;
  },
};
