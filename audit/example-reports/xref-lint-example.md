# Cross-Reference Lint - 2026-06-01

Scans all non-index pages under `wiki-pages/` for broken wikilinks, orphan pages, and broken Cross References sections.

## Summary

- Non-index pages scanned: 488
- Broken wikilinks: 5
- Orphan pages: 2
- Broken Cross References section links: 4
- Missing Cross References section: 38
- Total issues: 49

| Code | Count |
|---|---:|
| broken-wikilink | 5 |
| orphan-page | 2 |
| broken-xref-section | 4 |
| missing-xref-section | 38 |

## broken-wikilink (5)

| Page | Line | Target | Detail |
|---|---:|---|---|
| `wiki-pages/AI-Tools/Agent/multi-agent-setup.md` | 54 | `deleted-config-ref` | wikilink target not found |
| `wiki-pages/log.md` | 71 | `old-page-name` | wikilink target not found |
| `wiki-pages/log.md` | 157 | `renamed-category` | wikilink target not found |
| `wiki-pages/log.md` | 284 | `deleted-page` | wikilink target not found |
| `wiki-pages/session-notes/example-session.md` | 100 | `people/old_ref` | wikilink target not found |

## broken-xref-section (4)

| Page | Line | Target | Detail |
|---|---:|---|---|
| `wiki-pages/AI-Tools/Agent/mcp-tools.md` | 42 | `Other-Tools/overview` | wikilink target not found |
| `wiki-pages/AI-Tools/Claude-Code/example-page.md` | 169 | `Claude-Code-索引` | wikilink target not found |
| `wiki-pages/AI-Tools/Github-Repos/example-repo.md` | 207 | `Github-Repos-索引` | wikilink target not found |
| `wiki-pages/AI-Tools/Prompt/techniques.md` | 77 | `AI Agent/Skill Design` | wikilink target not found |

## orphan-page (2)

| Page | Status | Body Length |
|---|---|---:|
| `wiki-pages/AI-Tools/orphan-example.md` | wiki | 1200 |
| `wiki-pages/Misc/unlinked-note.md` | wiki | 450 |

## missing-xref-section (38)

The following wiki/reference pages have no `## Cross References` section:

| # | Page | Status |
|---|---|---|
| 1 | `wiki-pages/AI-Tools/example-page-1.md` | wiki |
| 2 | `wiki-pages/AI-Tools/example-page-2.md` | wiki |
| 3 | `wiki-pages/AI-Tools/example-page-3.md` | reference |
| ... | ... (35 more) | ... |
