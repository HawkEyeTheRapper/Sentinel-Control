#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <skill-name> <description>"
  exit 1
fi

name="$1"
shift

description="$*"

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

template_dir="${root}/templates/skill-template"
skills_dir="${root}/skills"
target_dir="${skills_dir}/${name}"

if [ -e "${target_dir}" ]; then
  echo "Skill already exists: ${target_dir}"
  exit 1
fi

mkdir -p "${skills_dir}"
cp -R "${template_dir}" "${target_dir}"

python3 - "${target_dir}/SKILL.md" "${name}" "${description}" <<'PY'
import pathlib
import sys

path = pathlib.Path(sys.argv[1])
name = sys.argv[2]
desc = sys.argv[3]
text = path.read_text()
text = text.replace("__SKILL_NAME__", name).replace("__DESCRIPTION__", desc)
path.write_text(text)
PY

echo "Created ${target_dir}"
