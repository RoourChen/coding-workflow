#!/usr/bin/env python3
"""Create a compact TASK.md without overwriting existing work."""

from __future__ import annotations

import argparse
from pathlib import Path


def bullet_lines(values) -> str:
    return "\n".join(f"- {value}" for value in values)


def render_task(
    title: str,
    goal: str,
    non_goals: list[str],
    done: list[str],
    verify: list[str],
    scope: list[str] | None = None,
) -> str:
    sections = [
        f"# Task: {title}",
        "## Goal\n\n" + goal,
        "## Non-goals\n\n" + bullet_lines(non_goals),
        "## Done when\n\n" + bullet_lines(done),
    ]
    if scope:
        sections.append("## Scope\n\n" + bullet_lines(scope))
    sections.extend(
        [
            "## Verify\n\n" + bullet_lines(f"`{command}`" for command in verify),
            "## Risks and assumptions\n\n- None recorded yet.",
        ]
    )
    return "\n\n".join(sections) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".", help="Project directory")
    parser.add_argument("--output", default="TASK.md", help="Path relative to project")
    parser.add_argument("--title", required=True)
    parser.add_argument("--goal", required=True)
    parser.add_argument("--non-goal", action="append", required=True, dest="non_goals")
    parser.add_argument("--done", action="append", required=True)
    parser.add_argument("--verify", action="append", required=True)
    parser.add_argument("--scope", action="append")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project = Path(args.project).expanduser().resolve()
    output = Path(args.output)
    if output.is_absolute() or ".." in output.parts:
        raise SystemExit("--output must stay inside the project directory")
    destination = (project / output).resolve()
    if destination != project and project not in destination.parents:
        raise SystemExit("--output must stay inside the project directory")
    if destination.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        render_task(
            args.title,
            args.goal,
            args.non_goals,
            args.done,
            args.verify,
            args.scope,
        ),
        encoding="utf-8",
    )
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
