# Status Audit - 2026-06-01

This is a report-only audit of `wiki-pages/**/*.md`. It excludes `README.md` files and does not modify wiki content.

## Summary

- Scanned markdown pages: 502
- Content pages audited: 499
- Excluded README files: 3
- Missing status pages: 2
- Unknown status pages: 1
- Misplaced project-management statuses: 0
- Frontmatter author issues: 3

## Main Statuses

| Status | Count |
|---|---:|
| reference | 28 |
| stub | 95 |
| wiki | 359 |

## Project-Management Statuses

`active` and `legacy` are legal only under `wiki-pages/project-management/`.

| Status | Count |
|---|---:|
| active | 12 |
| legacy | 1 |

## Missing Status

| Path | Status | Category |
|---|---|---|
| `wiki-pages/AI-Tools/example-missing-status.md` | (none) | AI-Tools |
| `wiki-pages/Health/another-missing-status.md` | (none) | Health |

## Unknown Status

| Path | Status | Category |
|---|---|---|
| `wiki-pages/Misc/page-with-typo-status.md` | wki | Misc |

## Misplaced Project-Management Statuses

None detected.

## Excluded README Files

- `wiki-pages/README.md`
- `wiki-pages/project-management/projects/README.md`
- `wiki-pages/project-management/README.md`

## Frontmatter Author Issues

Validates `作者` field. Valid: `[]`, `["@handle"]`, `["@a", "@b"]`. Invalid: `[@handle]` (unquoted).

| Path | Rule | Severity | Actual Value |
|---|---|---|---|
| `wiki-pages/AI-Tools/example-bare-author.md` | author-unquoted-bracket | error | `[@example-author]` |
| `wiki-pages/Health/another-bare-author.md` | author-unquoted-bracket | error | `[@another-author]` |
| `wiki-pages/Misc/bare-string-author.md` | author-bare-string | error | `@example-user` |
