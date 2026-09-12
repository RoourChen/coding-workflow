# Independent review contract

## Reviewer inputs

Provide:

- the task brief or exact user request;
- the relevant diff or changed files;
- fresh test, lint, build, or manual verification evidence;
- minimal surrounding code needed to evaluate behavior.

Do not provide the implementer's claim that the work is correct. The reviewer should inspect evidence rather than inherit confidence.

## Review order

1. **Contract:** Does the change satisfy every acceptance condition and avoid every non-goal?
2. **Correctness:** Check behavior, edge cases, error paths, state, and regression coverage.
3. **Safety:** Check permissions, secrets, destructive behavior, input boundaries, and dependency changes when relevant.
4. **Simplicity:** Flag unnecessary code, features, dependencies, abstractions, or unrelated refactors.
5. **Verification:** Confirm that the evidence actually tests the changed behavior.

Review security, performance, accessibility, or migration concerns deeply only when the change makes those dimensions relevant. Do not turn every ordinary review into a universal audit.

## Output format

Return findings first, ordered by severity:

```markdown
## Blocker

- <finding with file/line evidence and required correction>

## Important

- <material finding and reason>

## Suggestion

- <optional improvement>

## Verdict

<Ready / Not ready, followed by one sentence of evidence>
```

Omit empty sections. A Blocker or unresolved Important finding means Not ready. After fixes, review the changed areas and their affected tests again.
