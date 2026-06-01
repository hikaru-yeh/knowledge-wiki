# Wiki Maintenance Report - 2026-06-01

## Summary

| Check | Errors | Warnings | Info |
|---|---:|---:|---:|
| status-audit | 0 | 0 | 0 |
| author-validation | 0 | 0 | 0 |
| canonical-guard | 0 | 0 | 0 |
| index-lint | 0 | 2 | 0 |
| xref-lint | 0 | 5 | 3 |
| readability-lint | 0 | 0 | 12 |
| tags-lint | 0 | 0 | 25 |
| coverage | 0 | 1 | 3 |
| duplicates | 0 | 0 | 0 |
| blocked-nonlingorm | 0 | 0 | 0 |
| blocked-lingorm | 0 | 0 | 8 |
| **Total** | **0** | **8** | **51** |

## Status Audit

- Content pages: 502
- wiki: 359, reference: 28, stub: 95

## Index Lint

### stub-marker-mismatch (2)

| Index | Line | Target | Page Status | Index Marker |
|---|---:|---|---|---|
| `wiki-pages/index/AI-工具-索引.md` | 45 | `Example Page` | wiki | has stub marker |
| `wiki-pages/index/工具軟體-索引.md` | 12 | `Another Page` | stub | no stub marker |

## Cross-Reference Lint

### broken-wikilink (3)

| Page | Line | Target | Detail |
|---|---:|---|---|
| `wiki-pages/log.md` | 71 | `deleted-page` | wikilink target not found |
| `wiki-pages/log.md` | 157 | `renamed-topic` | wikilink target not found |
| `wiki-pages/session-notes/example-session.md` | 100 | `people/old_ref` | wikilink target not found |

### broken-xref-section (2)

| Page | Line | Target | Detail |
|---|---:|---|---|
| `wiki-pages/AI-Tools/example-tool.md` | 42 | `Other-Tools/overview` | wikilink target not found |
| `wiki-pages/AI-Tools/another-page.md` | 169 | `Category-索引` | wikilink target not found |

### orphan-page (3)

| Page | Status | Body Length |
|---|---|---:|
| `wiki-pages/AI-Tools/orphan-example.md` | wiki | 1200 |
| `wiki-pages/Misc/unlinked-page.md` | wiki | 450 |
| `wiki-pages/Misc/another-orphan.md` | stub | 120 |

## Readability Lint (12 issues)

| # | Code | Path | Headings | Body len | Detail |
|---|------|------|---:|---:|--------|
| 1 | single-dump | `wiki-pages/AI-Tools/unstructured-paste.md` | 0 | 1100 | 0 meaningful headings, no format elements |
| 2 | social-tone | `wiki-pages/AI-Tools/social-post-example.md` | 3 | 710 | social media tone detected |
| 3 | no-formatting | `wiki-pages/AI-Tools/wall-of-text.md` | 2 | 2750 | has headings but no bullet lists, code blocks, tables |
| ... | ... | ... | ... | ... | 9 more issues |

## Tags Lint (25 issues)

- missing-tags-field: 5
- empty-tags: 15
- singleton-tag: 5

## Coverage

- Raw scanned: 471, with URL: 470
- Raw-only (not in wiki): 3
- Missing URL: 1

| Raw File | Suggested Category |
|---|---|
| `raw/threads/Example-Topic.md` | AI 工具 |
| `raw/threads/Another-Topic.md` | 生活雜記 |
| `raw/threads/Third-Topic.md` | AI 工具 |

## Blocked LingOrm Excluded (8)

8 LingOrm stubs excluded by policy.

## Suggested Next Agent Prompt

```text
請依照 audit/maintenance-reports/maintenance-report-YYYY-MM-DD.md，只處理 Errors。
LingOrm stub 保留。
先提出修復計畫，不要直接大批刪檔。
```
