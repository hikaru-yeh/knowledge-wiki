# Index Lint - 2026-06-01

This is a report-only lint of index pages under `wiki-pages/index/`. It does not modify wiki content.

## Summary

- Index pages scanned: 14
- Total issues: 7

| Code | Count |
|---|---:|
| literal-raw-link | 1 |
| ambiguous-bare-link | 2 |
| missing-target | 1 |
| stub-marker-mismatch | 3 |

## Issues

| Code | Page | Line | Target | Detail |
|---|---|---:|---|---|
| literal-raw-link | `wiki-pages/index/AI-工具-索引.md` | 23 | `raw/threads/Example-Topic.md` | index should link to wiki-pages, not raw |
| ambiguous-bare-link | `wiki-pages/index/AI-工具-索引.md` | 45 | `Example-Page` | bare wikilink matches multiple targets: wiki-pages/AI-Tools/Example-Page.md, raw/threads/Example-Page.md |
| ambiguous-bare-link | `wiki-pages/index/Software-Tools-索引.md` | 12 | `Example-Tool` | bare wikilink matches multiple targets: wiki-pages/Software-Tools/Example-Tool.md, raw/threads-saved/Example-Tool.md |
| missing-target | `wiki-pages/index/Health-索引.md` | 31 | `Deleted-Page` | wikilink target not found |
| stub-marker-mismatch | `wiki-pages/index/AI-工具-索引.md` | 48 | `Promoted-Page` | page status is wiki but index has stub marker |
| stub-marker-mismatch | `wiki-pages/index/Software-Tools-索引.md` | 15 | `Still-A-Stub` | page status is stub but index has no stub marker |
| stub-marker-mismatch | `wiki-pages/index/Travel-索引.md` | 22 | `Another-Mismatch` | page status is wiki but index has stub marker |
