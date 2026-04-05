#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_dir="${root}/skills"

skills_ref_bin="${SKILLS_REF_BIN:-/mnt/aether_vault/omni-stack/tools/agentskills/skills-ref/.venv/bin/skills-ref}"

if [ ! -x "${skills_ref_bin}" ]; then
  echo "skills-ref not found: ${skills_ref_bin}"
  echo "Install it via /mnt/aether_vault/omni-stack/tools/agentskills/skills-ref/README.md"
  exit 1
fi

found=0

if [ -d "${skills_dir}" ]; then
  for dir in "${skills_dir}"/*; do
    if [ -d "${dir}" ] && [ -f "${dir}/SKILL.md" ]; then
      found=1
      echo "Validating ${dir}"
      "${skills_ref_bin}" validate "${dir}"
    fi
  done
fi

if [ "${found}" -eq 0 ]; then
  echo "No skills found in ${skills_dir}"
fi
