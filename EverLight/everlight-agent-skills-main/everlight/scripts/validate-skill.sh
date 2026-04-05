#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <skill-dir> [<skill-dir> ...]"
  exit 1
fi

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

skills_ref_bin="${SKILLS_REF_BIN:-/mnt/aether_vault/omni-stack/tools/agentskills/skills-ref/.venv/bin/skills-ref}"

if [ ! -x "${skills_ref_bin}" ]; then
  echo "skills-ref not found: ${skills_ref_bin}"
  echo "Install it via /mnt/aether_vault/omni-stack/tools/agentskills/skills-ref/README.md"
  exit 1
fi

"${skills_ref_bin}" validate "$@"
