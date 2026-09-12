# Design provenance

This skill is an independent, lightweight implementation. It adopts workflow ideas, not source text.

## Adopted patterns

### obra/superpowers

Reviewed at commit `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` (MIT).

- Fresh verification evidence before completion claims.
- Precisely scoped reviewer context instead of inheriting the implementer's reasoning.
- Severity-based review followed by correction and re-review.
- Small, independently verifiable implementation units.

Source: <https://github.com/obra/superpowers>

### addyosmani/agent-skills

Reviewed at commit `48cb1168aeaaa70dfc2bbf709eddfa2a8ed8129a` (MIT).

- Proportionate use: trivial work should not require a full specification.
- Explicit goal, commands, test strategy, success criteria, and behavioral boundaries.
- Review of correctness and simplicity beyond merely checking that tests pass.

Source: <https://github.com/addyosmani/agent-skills>

### Macondooo/codex-research-examples

Reviewed at commit `83a783a74b6626ef8fa9e0bd855ffb8cabd9fe1c`. The repository did not declare a license at review time, so no text or code was copied.

Independently implemented concepts inspired by the repository analysis:

- A task brief before implementation.
- Reproducible commands and output artifacts.
- Worker/reviewer separation and a fix-and-review loop.

Source: <https://github.com/Macondooo/codex-research-examples>

## Deliberately not adopted

- Mandatory TDD for every change.
- Mandatory worktrees, commits, branches, or pull requests.
- Human approval gates after every planning phase.
- A large suite of interdependent skills.
- Fixed directory conventions when a project already has suitable ones.

These omissions preserve implementation freedom and keep the workflow useful for small personal projects.
