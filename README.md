# coding-workflow

A lightweight Codex Agent Skill for people who want reliable AI-assisted coding without adopting a heavyweight software-development process.

It guides an agent through:

- a clear goal, non-goals, and definition of done;
- proportionate Tiny, Standard, and High-risk modes;
- narrow implementation without unrelated features or dependencies;
- fresh test or verification evidence before completion claims;
- independent read-only review with Blocker, Important, and Suggestion findings.

The workflow deliberately does **not** force TDD, Git worktrees, commits, pull requests, or lengthy specifications for every edit.

## Install

Clone directly into the Codex personal skill directory:

```bash
git clone https://github.com/w93139/coding-workflow.git ~/.codex/skills/coding-workflow
```

Codex can discover the skill on a later turn. Invoke it explicitly with `$coding-workflow`, or let its description match implementation and bug-fix requests automatically.

## Optional task-file helper

```bash
python ~/.codex/skills/coding-workflow/scripts/init_task.py --help
```

The helper refuses to overwrite an existing task file.

## Verify this repository

```bash
python -m unittest discover -s tests -v
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

## High-star workflow absorption

Yes. The skill incorporates selected ideas from `obra/superpowers` and `addyosmani/agent-skills`: fresh verification, reviewer-context isolation, severity gates, explicit boundaries, and proportional workflow selection. It independently implements task-brief and worker/reviewer concepts inspired by `Macondooo/codex-research-examples`; that repository had no declared license when reviewed, so no text or code was copied.

Exact reviewed revisions and deliberately rejected heavyweight rules are documented in [references/provenance.md](references/provenance.md).

## License

MIT. See [LICENSE](LICENSE).
