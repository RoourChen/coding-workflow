# Task brief template

Use the repository's existing convention when one exists. For short Standard work, an inline brief is enough. Otherwise use this compact shape for a durable task record and expand the risk section only for High-risk work.

```markdown
# Task: <short outcome>

## Goal

<Observable result for the user or system.>

## Non-goals

- <Adjacent feature or refactor that is intentionally excluded.>

## Done when

- <Checkable acceptance condition.>

## Scope

- Expected: `<file or component>`
- Preserve: <important existing behavior or user change>

## Verify

- `<exact command>` — proves <acceptance condition>
- Manual: <observable check, only when automation is unsuitable>

## Risks and assumptions

- <Only decisions that could materially change the result.>
```

Keep the brief readable by a non-programmer. Describe user-visible behavior before technical implementation. A task brief is a contract, not a diary: update decisions and scope changes, but do not paste implementation logs into it.
