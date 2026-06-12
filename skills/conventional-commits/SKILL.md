---
description: Conventional Commits 1.0.0 for clear, machine-readable commit messages with SemVer alignment. Use when writing commit messages, squashing PRs, configuring commitlint, or generating changelogs. WHEN: conventional commits, commit message format, feat, fix, chore, docs, style, refactor, perf, test, ci, build, revert, BREAKING CHANGE, semantic versioning, changelog, commitlint.
---

# Conventional Commits (v1.0.0)

A practical reference for writing commit messages that are easy for humans to read and easy for tools to parse.

## Canonical format

```text
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

## When to use
- You want clean history and predictable commit message structure.
- You use automated release/version tooling (for example semantic-release).
- You generate changelogs from git history.
- You want quick semantic intent in commit titles (`feat`, `fix`, etc.).

## When NOT to use
- One-off throwaway repositories where history quality is irrelevant.
- Teams without agreement on commit conventions.

## Required spec rules (v1.0.0)
- Header MUST start with a type, then optional scope, optional `!`, then `: ` and description.
- `feat` MUST be used for new features.
- `fix` MUST be used for bug fixes.
- Scope, when present, is in parentheses: `feat(parser): ...`.
- Body, when present, starts after one blank line.
- Footers, when present, start after one blank line from body (or header if no body).
- Footer token format is `<token>: <value>` or `<token> #<value>`.
- Footer tokens use hyphens instead of spaces (except `BREAKING CHANGE`).
- Breaking changes MUST be marked by either:
  - `!` in header before `:`, or
  - `BREAKING CHANGE: ...` footer (or `BREAKING-CHANGE: ...`).

## Recommended common types
These are common ecosystem conventions (not all are required by the spec):
- `feat`: new feature
- `fix`: bug fix
- `docs`: documentation only
- `style`: formatting only (no behavior changes)
- `refactor`: code change without feature or fix intent
- `perf`: performance improvement
- `test`: tests added/updated
- `build`: build system or dependency tooling
- `ci`: CI pipeline/config updates
- `chore`: maintenance work
- `revert`: revert a previous change

## SemVer mapping
- `fix` -> PATCH bump
- `feat` -> MINOR bump
- Any commit with breaking change marker (`!` or `BREAKING CHANGE`) -> MAJOR bump

## Good examples

```text
feat(auth): add refresh token rotation
```

```text
fix(api): handle null correlation id in middleware
```

```text
feat(ui)!: remove legacy theme variables
```

```text
refactor(parser): simplify token pipeline

Moves token normalization into a dedicated stage to reduce branching.

Refs: #482
```

```text
feat: allow config inheritance

BREAKING CHANGE: `extends` now overrides the previous merge strategy.
```

## Common mistakes and fixes
- Missing colon separator
  - Bad: `feat(auth) add oauth flow`
  - Good: `feat(auth): add oauth flow`
- Using sentence-style capitalization/punctuation in description
  - Prefer short imperative summary: `add oauth flow`
- Mixing unrelated changes in one commit
  - Split into multiple commits so each has a clear type.
- Using non-standard type by typo
  - Bad: `feet: ...`
  - Good: `feat: ...`

## PR squash commit guidance
When squashing, use one Conventional Commit header that reflects user impact:
- If any change is breaking, include `!` or `BREAKING CHANGE`.
- Otherwise prioritize by impact: `feat` over `fix`, then maintenance types.
- Add a body for key rationale and footers for traceability (`Refs: #123`).

## Commitlint starter config

```js
// commitlint.config.cjs
module.exports = {
  extends: ["@commitlint/config-conventional"],
};
```

## References
- Conventional Commits 1.0.0: https://www.conventionalcommits.org/en/v1.0.0/
- RFC 2119 terminology: https://www.rfc-editor.org/rfc/rfc2119
- Git trailers: https://git-scm.com/docs/git-interpret-trailers

## Lessons learned (rolling)
<!-- Append new entries here as patterns/pitfalls are discovered. Format:
- YYYY-MM-DD: <observation>
-->
- 2026-06-12: Teams adopting Conventional Commits get better release automation when they agree on allowed types and scope vocabulary up front.
