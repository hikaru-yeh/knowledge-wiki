# Canonical Guard - 2026-06-01

This is a report-only guard. No files were modified.

## Summary

- Scanned wiki pages: 502
- Stale file conflicts: 2
- Frontmatter author issues: 1

## Stale File Conflicts

Stale files are old or renamed copies that must not coexist with their canonical counterpart.

| Canonical | Stale | Action |
|---|---|---|
| `wiki-pages/log.md` | `wiki-pages/日誌.md` | merge-then-delete |
| `wiki-pages/index/AI 工具-索引.md` | `wiki-pages/index/AI 工具索引.md` | merge-then-delete |

## Frontmatter Author Issues

Validates `作者` field. Valid: `[]`, `["@handle"]`, `["@a", "@b"]`. Invalid: `[@handle]` (unquoted).

| Path | Rule | Severity | Actual Value |
|---|---|---|---|
| `wiki-pages/AI-Tools/example-page.md` | author-unquoted-bracket | error | `[@someuser]` |
