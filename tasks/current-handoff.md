# Current Handoff

- Generated: 2026-05-28 (batch 5)
- Task: inject-pending subcommand + --apply
- Next: canonical cleanup, CI gates, scan aggregator update
- Current branch during this update: `master`

## Current State Summary

All major apply-style subcommands implemented. Remaining work: canonical cleanup, CI gates, scan aggregator update for inject-pending.

Available subcommands in `tools/wiki_maintain.py`:

- `scan` — run all currently implemented report-only checks and write a combined maintenance report
- `handoff` — write `tasks/current-handoff.md`
- `blocked-report` — write `tasks/blocked-content-gaps.md`
- `status-audit` — audit page status and frontmatter schema issues
- `index-lint` — lint index page links and stub markers
- `review-reconcile` — classify review findings into reconciliation buckets
- `coverage` — compare raw URLs against wiki URLs and report ingest candidates
- `duplicates` — detect duplicate wiki frontmatter URLs and suggest canonicals
- `canonical-guard` — detect stale canonical conflicts and author frontmatter rule violations
- `author-fix` — repair bare-string `作者` fields into canonical list format
- `bare-link-fix` — convert ambiguous bare `[[wikilinks]]` to explicit relative links in index files
- `pending-match` — compare external pending digest URLs against wiki page URLs
- `inject-pending` — inject content from pending digest files into matching wiki stubs (`--apply`, `--limit N`, `--pending-dir PATH`)
- `promote-ready` — list or apply promotion of non-LingOrm stubs (`--apply`, `--limit N`)
- `audit-list` — list open items from the audit/ directory

## Batch 5 Completions

- **`inject-pending` subcommand implemented** (commit `bb61a7b`): report + `--apply` + `--limit N`. New code: `_INJECT_STUB_MARKERS`, `_INJECT_LEVEL2_RE`, `_determine_inject_status`, `InjectPendingEntry`, `InjectPendingResult`, `collect_inject_pending`, `render_inject_pending_report`, `unique_inject_pending_report_path`, `apply_inject_pending`, `command_inject_pending`. Requires `--pending-dir PATH` (no hardcoded paths). LingOrm always skipped. Appends log.md on apply.
- **Verification**: `inject-pending --help` ✓, nonexistent-dir error ✓, 0-eligible dry run ✓, `promote-ready` 0 ✓, `index-lint` 0 ✓

## Batch 4 Completions

- **7 AI 工具 stubs promoted** (stub→wiki): AI-企業作業系統降臨、AI進化超速、Paperclip、Vibe-Coding-亂象、擺脫糊字AI簡報、用Obsidian建立LLM知識庫、開發者別再浪費tokens
- **Dashboard updated**: AI 工具 Wiki 209→216, Stub 12→5; header Wiki 359→366, Stub 93→86
- **`promote-ready --apply` implemented** in `tools/wiki_maintain.py`: new helpers `_promote_stub_to_wiki`, `_remove_stub_marker_from_index_files`, `_build_stub_marker_patterns`, `apply_promote_ready`; CLI flags `--apply` and `--limit N` added to parser
- **Commit**: `6ef6b64`
- **promote-ready post-check**: 0 ready stubs remain
- **index-lint post-check**: 0 total issues, stub-marker-mismatch: 0

## Claude Code / Worker Completed Tasks Captured

These were reported complete in this session and are now reflected in this handoff:

- `handoff` and `blocked-report` first version
- `status-audit`
- `index-lint`
- `review-reconcile`
- `coverage`
- `duplicates`
- `canonical-guard`
- shared frontmatter author validator
- `author-fix` subcommand implemented and applied: 83 bare-string 作者 fields fixed, verified 0 remaining (commit `822fd3f`)
- Generator hardening: `normalize_author_field()` + `extract_handle()` added to `fill_threads_stub_pages.py` to prevent future bare-string author output
- `scan` aggregator
- coverage exclusion polish
- `bare-link-fix` subcommand implemented and applied: 353/355 ambiguous bare `[[wikilinks]]` converted to explicit relative links across 7 index files (2 genuinely ambiguous remain — LingOrm duplicate stems)
- OCR sanity check added to `fill_threads_stub_pages.py`: 4-check system (consecutive repetition >5, line count >500, length ratio >10x, Shannon entropy <2.0) via `check_ocr_sanity()` + `sanitize_page_text()`
- 曼谷茶冰淇淋.md OCR garble fixed (16,471→20 lines, "BALCONY" ×16371 removed)
- 33 stub-marker-mismatches fixed in LingOrm-索引.md (added `（📌 stub）` markers)
- 2 broken wikilinks fixed in 專案管理-索引.md (`shane_wiki` → `personal_wiki`, `shane_wiki_v2` → `personal_wiki_v2`)
- 擲杯技巧.md promoted stub→wiki (user had already populated content)
- Coverage ingest: created `工程師最常用的 12 個 Claude Code 指令.md` (merged 2 raw files, status: wiki, 作者: @this.web)
- 3 empty pages deleted: 147個AI員工，一鍵部署玩轉.md, 壺鈴運動.md, 練肩.md
- AI Agent 架構四象限.md: bare author `ainotes0313` → `["@ainotes0313"]`
- 總索引 dashboard counts updated (Wiki 359, Stub 95)
- All index files updated: AI 工具-索引, 健康生活-索引, 生活雜記-索引, 求職履歷-索引
- Commit `bf2efa9`: batch wiki maintenance (20 files, +978/-16916 lines)
- `pending-match` subcommand implemented: report-only, requires `--pending-dir`, tested with crawl-the-threads output (0 pending files)
- `promote-ready` subcommand implemented: report-only, found 9 stubs ready for promotion (7 AI 工具 body>198 chars, 2 求職履歷 borderline at 32 chars with 2 headings)
- `audit-list` subcommand implemented: reports "no audit directory" (expected)
- BOM defense: `text.lstrip('﻿')` added to `parse_frontmatter()` in wiki_maintain.py, fill_threads_stub_pages.py, inject_pending_digest.py
- BOM stripped from `AI Agent 架構四象限.md` file content; status-audit missing-status reduced from 2→1 (only session-筆記-索引.md remains, genuinely missing frontmatter)
- LingOrm dedup resolved: deleted `LingOrm 系列/Lingorm 群組八卦懶人包.md` (truncated URL), kept `鄺玲玲系列/` version (full URL matching raw source), index link disambiguated
- Playwright fill for 2 求職履歷 stubs (`有用免費證照.md`, `職涯分析Prompt.md`): FAILED — SocialCrawl API 404 + Threads login wall. Pages remain as stubs.
- Commit `650e21c`: feat(tools) batch 3 (7 files, +632/-12 lines)
- public showcase scaffold/documentation updates on `codex/public-showcase`
- public `AGENTS.md` sync from private `CLAUDE.md`
- public `AGENTS_en.md` English companion and sync rule
- public README maintenance architecture status, inspiration sources, and WIP progress notes
- **Maintenance handoff hook** (`tools/hooks/check_maintenance_handoff.py`) — Claude Code Stop hook that blocks the agent from stopping when maintenance tools or reports were modified but handoff/plan files were not updated. Registered in `.claude/settings.json` as both SessionStart and Stop hooks. Verified with 8 test scenarios including pre-existing dirty handling and escape hatch.

## Latest Useful Reports

Recent report files exist under `tasks/maintenance-reports/`, including:

- `maintenance-report-2026-05-27*.md`
- `canonical-guard-2026-05-27*.md`
- `duplicates-2026-05-27*.md`
- `ingest-candidates-2026-05-27*.md`
- `status-audit-2026-05-27*.md`
- `index-lint-2026-05-26*.md`
- `review-reconcile-2026-05-26*.md`

Before starting a new maintenance batch, regenerate current reports instead of relying only on dated reports:

```powershell
python tools\wiki_maintain.py scan --report
python tools\wiki_maintain.py status-audit --report
python tools\wiki_maintain.py canonical-guard --report
python tools\wiki_maintain.py index-lint --report
python tools\wiki_maintain.py coverage --report
python tools\wiki_maintain.py duplicates --report
```

## Maintenance Handoff Hook

A Claude Code hook is now active that enforces handoff/plan updates when maintenance tools or reports are modified. Files:

- `tools/hooks/check_maintenance_handoff.py` — the hook script
- `tools/hooks/.gitignore` — ignores the `.session_start` runtime marker
- `.claude/settings.json` — registers SessionStart and Stop hooks

### How it works

| Hook Event | Command | Purpose |
|------------|---------|---------|
| `SessionStart` | `python tools/hooks/check_maintenance_handoff.py --mark-session-start` | Writes a rich JSON marker (`tools/hooks/.session_start`) containing `started_at`, `tracked_dirty` (which monitored files were already dirty), and `tracked_mtimes` (baseline mtimes). |
| `Stop` | `python tools/hooks/check_maintenance_handoff.py` | Compares current state against the session-start baseline. Exits non-zero (blocks the agent from stopping) if required response files are missing. |

### Rules enforced

**Rule A** — If any of these were modified during the session:
- `tools/wiki_maintain.py`
- `tools/wiki_maintenance/**`
- `tasks/maintenance-reports/*.md`

then `tasks/current-handoff.md` must also be updated.

**Rule B** — If subcommand/CLI definitions changed in `tools/wiki_maintain.py`, or `tools/wiki_maintenance/**` was modified:

then `tasks/wiki-maintenance-agent-implementation-plan.md` must also be updated.

**Rule B escape hatch** — If the implementation plan does not need updating (e.g., purely internal changes), the worker can instead:
1. Update `tasks/current-handoff.md` (still required), and
2. Include the phrase `implementation plan not needed` (case-insensitive) in the handoff.

The hook reads the handoff content and accepts this as a valid alternative. Old/stale handoff content does not satisfy the escape hatch — the handoff must have been modified during the current session.

### Pre-existing dirty handling

The SessionStart marker snapshots which monitored tracked files are already dirty and their mtimes. At Stop time:
- File became dirty after session start → trigger.
- File was already dirty at session start, mtime unchanged → **not** a trigger (pre-existing, untouched).
- File was already dirty at session start, mtime changed → trigger (re-modified this session).

Files outside the monitored set (`raw/`, `.obsidian/`, `wiki-pages/`, etc.) are never recorded and never trigger.

### Known limitations

- **Content quality not checked** — the hook verifies files were *touched*, not that their content meaningfully reflects the changes.
- **`tasks/` is untracked** — since `tasks/` is not committed to git, response file updates are detected via mtime > session_start rather than git status. If the session marker is missing, only tracked-file triggers are enforced.
- **Escape hatch is text-match only** — the hook searches for the literal phrase; it does not validate the justification.
- **`raw/` and `README` were not modified** during hook implementation.

## Remaining Work

Still not completed:

- canonical cleanup automation (`canonical-guard` reports conflicts but no auto-fix)
- delegate integration
- CI/report cleanliness gates
- `scan` aggregator: `inject-pending` not yet wired into scan (requires `--pending-dir` which scan doesn't have)
- README/tool docs for apply commands
- README/tool docs for apply commands

### Known remaining issues

- 1 page with missing `status` frontmatter: `session-筆記-索引.md` (index page with no frontmatter — intentional, not a content page)
- 2 求職履歷 stubs (`有用免費證照.md`, `職涯分析Prompt.md`) remain unfetchable — Threads login wall blocks both SocialCrawl API and Playwright. Needs logged-in session cookie or manual content.

## Explicit Next Step

`inject-pending --apply` is live (commit `bb61a7b`). All major apply subcommands done. Next priorities:

1. **Canonical cleanup** — `canonical-guard` still reports conflicts; implement auto-fix or guided workflow.
2. **CI gates** — add report-cleanliness checks to prevent regressions.
3. **`scan` aggregator** — wire `inject-pending` into scan (needs optional `--pending-dir`).

Dashboard current. No pending promote queue. To use inject-pending in practice: `python tools/wiki_maintain.py inject-pending --pending-dir <path> [--apply] [--limit N]`.

## Do Not Touch

- Do not modify `raw/`.
- Do not perform apply-style writes to `wiki-pages/` unless the user explicitly approves a bounded batch.
- Do not run `gbrain`.
- Do not treat LingOrm stubs as promotion errors.
- Do not hardcode local absolute paths in tools.
- Do not overwrite dirty out-of-scope files.

## Dirty But Out Of Scope At Time Of Update

Observed dirty paths included:

- `.obsidian/workspace.json`
- `tools/__pycache__/fill_threads_stub_pages.cpython-312.pyc`
- `wiki-pages/index/AI 工具-索引.md`
- many untracked private `raw/` files
- untracked local/editor/tooling files such as `.claude/settings.json`, `.obsidian/plugins/`, `gemini-scribe/`, and `tools/__pycache__/...`

These were not modified by this handoff update.

## Public Showcase Notes

Public branch work was done on `codex/public-showcase` and committed there:

- public scaffold prepared
- sanitized public `AGENTS.md`
- English `AGENTS_en.md`
- bilingual README updates
- maintenance architecture status and inspiration links

If continuing public showcase work, switch to `codex/public-showcase` carefully and avoid overwriting private dirty files on `master`.
