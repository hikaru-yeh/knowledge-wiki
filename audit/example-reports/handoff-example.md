# Current Handoff

- Generated: 2026-06-01T18:32:29
- Task: readability-lint batch fix (single-dump, batch 1)
- Next: continue readability-lint batch 2 (items 21-40)

## Current State Summary

Wiki maintenance v2 report-only tooling is active. Available subcommands:
- `scan` — aggregate all report-only checks
- `status-audit` — audit frontmatter status
- `index-lint` — lint index page links and stub markers
- `xref-lint` — cross-reference lint (broken links, orphans, xref sections)
- `readability-lint` — detect undigested wiki pages
- `tags-lint` — audit tags field (missing, empty, singleton)
- `canonical-guard` — detect stale canonical conflicts
- `coverage` — compare raw URL vs wiki URL, output ingest candidates
- `duplicates` — find duplicate wiki page URLs, suggest canonical
- `blocked-report` — list pages that cannot be auto-promoted
- `handoff` — this file
- `audit-list` — list open audit items
- `audit-resolve` — resolve audit items

To start next session: read this file, then run `python tools/wiki_maintain.py scan --report` to get current state.

## Available Reports

- `audit/maintenance-reports/maintenance-report-2026-06-01.md`
- `audit/maintenance-reports/readability-lint-2026-06-01.md`

## Files Touched In This Batch

- `wiki-pages/AI-Tools/example-page-1.md` (restructured, single-dump → resolved)
- `wiki-pages/AI-Tools/Agent/example-page-2.md` (restructured, single-dump → resolved)
- `wiki-pages/AI-Tools/Agent/example-page-3.md` (restructured, single-dump → resolved)
- ... (17 more pages restructured)

## Validations Passed

- `python tools/wiki_maintain.py readability-lint` — issue count decreased from 147 to 127
- `pwsh tools/validate-wiki.ps1` — PASS: 0 errors

## Explicit Next Step

continue readability-lint batch 2 (items 21-40)

## Do Not Touch

- `raw/`
- `wiki-pages/` apply-style writes outside current batch scope
- `README.md`

## Dirty But Out Of Scope

- ` M .obsidian/workspace.json`

## Dirty Raw Paths Out Of Scope

- None detected by `git status --short`.

## Report Files

- `tasks/current-handoff.md`
- `tasks/blocked-content-gaps.md`
- `audit/maintenance-reports/maintenance-report-2026-06-01.md`
