# EverLight Agent Skills Workspace

This workspace sits alongside the Agent Skills spec and reference SDK. Use it to
create, validate, and organize EverLight OS skills before publishing them.

## Layout

- `skills/` - Local skill directories (each contains a `SKILL.md`).
- `templates/skill-template/` - Starter template for new skills.
- `scripts/` - Helpers for creating and validating skills.
- `docs/` - Notes for team conventions and publishing.

## Quick start

1) Create a skill

```
./scripts/new-skill.sh my-skill "Describe what it does and when to use it."
```

2) Validate a skill

```
./scripts/validate-skill.sh ./skills/my-skill
```

3) Validate all skills

```
./scripts/validate-all.sh
```

## skills-ref CLI

The validation scripts expect the `skills-ref` CLI to be installed at:

```
/mnt/aether_vault/omni-stack/tools/agentskills/skills-ref/.venv/bin/skills-ref
```

To install it, follow `skills-ref/README.md` in the parent repository.
You can override the path by exporting `SKILLS_REF_BIN`.

## Publishing

When a skill is ready, copy it into the distribution repo and validate it again.
Keep each `SKILL.md` concise and move deep references into `references/`.
