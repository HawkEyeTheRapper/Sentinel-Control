# EverLight Agent Skills Workflow

## Goals

- Keep skills consistent with the Agent Skills specification.
- Validate every skill before distribution.
- Capture extra guidance in focused reference files.

## Conventions

- Skill names are lowercase with hyphens only, and must match the folder name.
- Keep `SKILL.md` under 500 lines when possible.
- Store deep detail in `references/`.
- Use `scripts/validate-skill.sh` for every change.

## Distribution checklist

1) Confirm `SKILL.md` frontmatter is valid.
2) Run validation against the final skill directory.
3) Confirm any scripts mention dependencies.
4) Add a short README for any shared assets.
