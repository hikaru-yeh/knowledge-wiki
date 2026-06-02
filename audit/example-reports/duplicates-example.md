# Duplicate URL Report - 2026-06-01

This is a report-only scan. No files were modified.

> Note: Hub pages (pages with `## Sources` and multiple wikilinks) are annotated
> but still listed. Manual review is required before merging or deleting.

## Summary

- Wiki pages scanned: 502
- Pages with URL: 460
- Pages without URL: 42
- Duplicate URL groups: 2
- Total pages in duplicate groups: 5

## Duplicate URL Groups

### Group 1 — https://www.threads.com/@example/post/ABC123

Suggested canonical: `wiki-pages/Travel/example-canonical-page.md`

| Status | Is Hub | Path | Body chars | Index refs |
|---|---|---|---:|---:|
| wiki | no | `wiki-pages/Travel/example-canonical-page.md` | 2450 | 1 |
| wiki | yes | `wiki-pages/Travel/example-hub-page.md` | 1800 | 1 |
| stub | no | `wiki-pages/Travel/example-duplicate-page.md` | 120 | 0 |

Suggested action:
- Keep `wiki-pages/Travel/example-canonical-page.md` as canonical.
- Merge useful content from other pages.
- Replace wikilinks pointing to duplicates.
- Delete duplicates after review.

### Group 2 — https://www.threads.com/@example/post/DEF456

Suggested canonical: `wiki-pages/Health/example-main-page.md`

| Status | Is Hub | Path | Body chars | Index refs |
|---|---|---|---:|---:|
| wiki | no | `wiki-pages/Health/example-main-page.md` | 1200 | 1 |
| stub | no | `wiki-pages/Health/example-alt-title-page.md` | 80 | 0 |

Suggested action:
- Keep `wiki-pages/Health/example-main-page.md` as canonical.
- Merge useful content from other pages.
- Replace wikilinks pointing to duplicates.
- Delete duplicates after review.
