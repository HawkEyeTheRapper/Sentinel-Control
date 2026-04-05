CREATE TABLE IF NOT EXISTS logs (
  convo_id TEXT PRIMARY KEY,
  title TEXT,
  log_title TEXT,
  slug TEXT,
  summary TEXT,
  message_count INTEGER,
  tags TEXT,
  accounts TEXT,
  r2_key TEXT
);

CREATE INDEX IF NOT EXISTS idx_logs_slug ON logs(slug);
CREATE INDEX IF NOT EXISTS idx_logs_title ON logs(title);
CREATE INDEX IF NOT EXISTS idx_logs_log_title ON logs(log_title);
