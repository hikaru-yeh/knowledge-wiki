# Knowledge Wiki

Languages: [English](README.md) | [繁體中文](README.zh-TW.md)

A scaffold of an LLM-maintained knowledge wiki.

This project organizes raw saved material into durable, cross-linked wiki pages. The original vault is used as a private second brain for notes, references, project memory, AI tooling research, job-search material, health notes, travel/food notes, and fandom/media notes. This public-friendly version keeps the architecture and workflow while omitting the private note contents.

## What This Shows

- A practical information architecture for an AI-assisted personal knowledge base.
- A clean separation between raw source material and curated wiki pages.
- A workflow for turning messy saved posts, references, project notes, and imported documents into structured Markdown knowledge.
- Index maintenance rules, page status conventions, and workflow knowledge patterns.
- A repository shape that can be reused for Obsidian, Claude Code, Codex, or other LLM-assisted writing workflows.
- A maintenance tool layer with 20 subcommands for reporting wiki health, linting cross-references, auditing content readability, and applying safe batch fixes.

## Repository Structure

```text
knowledge-wiki/
├── AGENTS.md
├── AGENTS_en.md
├── audit/
│   └── example-reports/             # Sanitized example outputs from each tool
├── raw/                             # User-managed source material, treated as read-only
│   ├── README.md
│   └── examples/                    # Synthetic publishable source examples
├── tasks/
│   └── maintenance-reports/         # Placeholder for generated local reports
├── tools/                           # Repo-specific maintenance scripts
│   ├── wiki_maintain.py             # Main CLI: 20 subcommands for scan/lint/fix
│   ├── validate-wiki.ps1            # CI gate: parses scan output, fails on errors
│   ├── gen_content_audit.py         # One-shot content quality triage tool
│   ├── fill_threads_stub_pages.py   # Batch-create stub pages from raw/threads
│   ├── sync_public_agents.py        # Regenerate public AGENTS.md from private CLAUDE.md
│   └── wiki_ocr/                    # Standalone audit-driven OCR fetch tool
│       ├── _gemini_client.py        # Gemini API wrapper
│       ├── _image_ocr.py            # Image OCR pipeline (Gemini-only)
│       └── audit_ocr.py             # CLI: read audit reports → fetch images → OCR → apply
└── wiki-pages/                      # LLM-maintained structured knowledge pages
    ├── README.md
    ├── index/                       # Example index structure
    ├── example-topic/               # Synthetic curated page examples
    └── log.example.md
```

## Core Workflow

The wiki uses a two-layer model:

1. `raw/` is the source inbox. Files here are user-managed and treated as immutable evidence.
2. `wiki-pages/` is the curated knowledge layer. An LLM agent reads selected raw material, decides the preservation level, writes structured pages, and updates indexes.

Typical operations:

- **Ingest**: Convert a raw source into a wiki page.
- **Promote**: Expand a lightweight bookmark or stub into a full wiki/reference page.
- **Re-ingest**: Rebuild a page when the original extraction lost too much detail.
- **Reorganize**: Move, rename, merge, or split pages while preserving internal links.
- **Query**: Answer questions from the curated wiki and report knowledge gaps.
- **Lint**: Check for broken links, stale references, duplicate URLs, blocked pages, weak summaries, and inconsistent frontmatter metadata.

---

## Maintenance Tooling

The repository includes a report-first maintenance CLI with 20 subcommands:

```powershell
python tools\wiki_maintain.py <subcommand> [options]
```

Design principles:

- `raw/` is read-only — no tool ever writes to it.
- Report-only by default. Destructive commands require explicit `--apply`.
- Reports drive bounded cleanup batches — never run apply blindly.
- LingOrm stubs are excluded from promote/error checks by policy.

### Maintenance architecture status

The maintenance architecture is inspired by:

- [`kfchou/wiki-skills`](https://github.com/kfchou/wiki-skills)
- [`lewislulu/llm-wiki-skill`](https://github.com/lewislulu/llm-wiki-skill)

**Implemented (Phase 1–4):**

- public/private agent instruction sync: `AGENTS.md` and `AGENTS_en.md`
- session handoff report generation
- blocked content gap reporting
- status/frontmatter auditing and author field repair (`author-fix --apply`)
- index linting with bare-link auto-fix (`bare-link-fix --apply`)
- cross-reference linting: broken wikilinks, orphan pages, broken xref sections (`xref-lint`)
- readability linting: detect undigested wiki pages (`readability-lint`)
- tags auditing: missing/empty tags, singleton tags, frequency stats (`tags-lint`)
- review finding reconciliation
- raw-to-wiki coverage reporting
- duplicate URL detection
- canonical guard checks for stale files and author frontmatter rules
- one-command `scan` aggregator (runs all checks)
- pending raw-to-wiki matching (`pending-match`) and digest injection (`inject-pending --apply`)
- safe promote flow (`promote-ready --apply`)
- audit inbox lifecycle (`audit-list`, `audit-resolve --apply`)
- CI gate (`tools/validate-wiki.ps1`) — enforces 0 errors before publishing
- content quality triage tool (`tools/gen_content_audit.py`)
- standalone audit-driven OCR fetch tool (`tools/wiki_ocr/`)
- `wiki-maintenance` Claude Code skill for guided batch maintenance

**Not implemented yet:**

- canonical cleanup automation
- delegate integration for multi-agent maintenance batches (Phase 4.5)
- Obsidian/Web feedback UI (Phase 5)

---

### Quick start

```powershell
# Full scan — runs all checks, writes markdown report
python tools\wiki_maintain.py scan --report

# CI gate — exits 1 if any errors found
pwsh tools\validate-wiki.ps1

# Session handoff for next agent
python tools\wiki_maintain.py handoff --task "batch-name" --next "next-step"
```

### Common commands

```powershell
# Scan & report (aggregates all checks)
python tools\wiki_maintain.py scan --report

# Individual lint checks
python tools\wiki_maintain.py status-audit --report
python tools\wiki_maintain.py index-lint --report
python tools\wiki_maintain.py xref-lint --report
python tools\wiki_maintain.py readability-lint --report
python tools\wiki_maintain.py tags-lint --report
python tools\wiki_maintain.py canonical-guard --report
python tools\wiki_maintain.py coverage --report
python tools\wiki_maintain.py duplicates --report

# Apply-style commands (require --apply flag)
python tools\wiki_maintain.py promote-ready --apply --limit 10
python tools\wiki_maintain.py author-fix --apply
python tools\wiki_maintain.py bare-link-fix --apply
python tools\wiki_maintain.py audit-resolve content-audit-2026-05-29.md --apply --summary "Done"

# Operational
python tools\wiki_maintain.py blocked-report
python tools\wiki_maintain.py audit-list --include-resolved
python tools\wiki_maintain.py handoff --task "batch-name" --next "next-step"
```

---

### Subcommand reference

| Subcommand | Type | Severity | Purpose | Output |
|---|---|---|---|---|
| `scan` | report | — | Aggregate all report-only checks into one report | `audit/maintenance-reports/maintenance-report-YYYY-MM-DD*.md` |
| `status-audit` | report | error | Detect missing/unknown `status`, author format violations | `audit/maintenance-reports/status-audit-YYYY-MM-DD*.md` |
| `index-lint` | report | error/warn | Check index links, stub markers, summary quality | `audit/maintenance-reports/index-lint-YYYY-MM-DD*.md` |
| `xref-lint` | report | warn/info | Broken wikilinks, orphan pages, broken xref sections, missing xref sections | `audit/maintenance-reports/xref-lint-YYYY-MM-DD*.md` |
| `readability-lint` | report | info | Detect undigested `status: wiki` pages (4 signal types) | `audit/maintenance-reports/readability-lint-YYYY-MM-DD*.md` |
| `tags-lint` | report | info | Audit `tags:` field: missing, empty, singleton tags; frequency stats | `audit/maintenance-reports/tags-lint-YYYY-MM-DD*.md` |
| `canonical-guard` | report | error | Detect stale canonical conflicts and author frontmatter violations | `audit/maintenance-reports/canonical-guard-YYYY-MM-DD*.md` |
| `coverage` | report | info | Find raw sources not yet ingested into wiki | `audit/maintenance-reports/ingest-candidates-YYYY-MM-DD*.md` |
| `duplicates` | report | error | Detect duplicate frontmatter URLs, suggest canonicals | `audit/maintenance-reports/duplicates-YYYY-MM-DD*.md` |
| `review-reconcile` | report | — | Bucket review findings into reconciliation categories | `audit/maintenance-reports/review-reconcile-YYYY-MM-DD*.md` |
| `blocked-report` | write | — | List pages that cannot be auto-promoted | `tasks/blocked-content-gaps.md` |
| `handoff` | write | — | Capture session state for next agent/session | `tasks/current-handoff.md` |
| `audit-list` | report | — | List open audit items; `--include-resolved` shows resolved count | stdout |
| `audit-resolve` | apply | — | Resolve audit item: move to `audit/resolved/`, append resolution | `audit/resolved/*.md` |
| `author-fix` | apply | — | Fix bare-string `作者` to canonical `["@handle"]` format | in-place wiki files |
| `bare-link-fix` | apply | — | Convert ambiguous bare `[[wikilinks]]` to explicit relative links | in-place index files |
| `pending-match` | report | — | Match external pending digest URLs against wiki URLs | stdout |
| `inject-pending` | apply | — | Inject pending digest content into matched wiki stubs | in-place wiki files |
| `promote-ready` | apply | — | Promote non-LingOrm stubs with sufficient content to `status: wiki` | in-place wiki files |

All report subcommands support `--report` to write a dated markdown file. All apply subcommands default to dry-run and require `--apply` to write.

---

### Tool usage & agent prompts

#### `xref-lint` — Cross-reference linting

Scans all non-index wiki pages for broken `[[wikilinks]]`, orphan pages (not referenced by any page or index), and broken links inside `## Cross References` sections.

```powershell
# Console output
python tools\wiki_maintain.py xref-lint

# Write dated report
python tools\wiki_maintain.py xref-lint --report
# → audit/maintenance-reports/xref-lint-YYYY-MM-DD.md
```

**Agent prompt (pair with report):**

```text
Read audit/maintenance-reports/xref-lint-YYYY-MM-DD.md and fix all xref issues.

How to handle each issue type:
- broken-xref-section: Fix broken wikilinks in Cross References blocks — change to correct relative links.
- broken-wikilink: For log.md historical broken links, remove [[]]; for shell code examples, use backticks; for session-note examples, use plain text.
- orphan-page: Add the page to the appropriate index.
- missing-xref-section: Add a ## Cross References section to wiki/reference pages that lack one, with at least 2-3 related page links. If there are many, process the first 20.

After fixing, verify with:
  python tools/wiki_maintain.py xref-lint
  pwsh tools/validate-wiki.ps1
```

See [`audit/example-reports/xref-lint-example.md`](audit/example-reports/xref-lint-example.md) for sample output.

---

#### `readability-lint` — Content readability check

Detects `status: wiki` pages that were never properly structured after ingestion. Four signal types:

| Signal | Meaning |
|--------|---------|
| `single-dump` | 0 meaningful headings + no format elements (pure paste) |
| `no-headings` | <2 meaningful headings + no format elements |
| `social-tone` | Emoji clusters or short-line social-media bursts |
| `no-formatting` | Has headings but no bullet lists, code blocks, tables, or blockquotes |

```powershell
# Console output
python tools\wiki_maintain.py readability-lint

# Write dated report
python tools\wiki_maintain.py readability-lint --report
# → audit/maintenance-reports/readability-lint-YYYY-MM-DD.md

# Included in full scan
python tools\wiki_maintain.py scan --report
```

**Agent prompt (pair with report):**

```text
Read audit/maintenance-reports/readability-lint-YYYY-MM-DD.md and batch-restructure the listed pages.

How to handle each signal:
- single-dump: Only has ## Main Content with no structure → reorganize into at least 2-3 meaningful H2 headings, add a summary paragraph.
- no-headings: Has some headings but not enough → add proper section structure.
- social-tone: Emoji/casual tone → rewrite in formal wiki voice, organize into paragraphs.
- no-formatting: Has headings but all prose → add bullet lists or tables where appropriate.

Before processing each page, check if the source URL is still accessible (Threads posts may be deleted). If source is gone and content < 300 chars, demote to stub.

Process the first 20 single-dump issues. After each batch, verify:
  python tools/wiki_maintain.py readability-lint
Confirm issue count decreases before continuing.
```

See [`audit/example-reports/readability-lint-example.md`](audit/example-reports/readability-lint-example.md) for sample output.

---

#### `tags-lint` — Tags field auditing

Audits the `tags:` frontmatter field across all non-index wiki pages. Three issue types:

| Issue | Severity | Meaning |
|-------|----------|---------|
| `missing-tags-field` | info | wiki/reference page has no `tags:` field at all |
| `empty-tags` | info | wiki/reference page has `tags: []` |
| `singleton-tag` | info | Tag appears only once across the entire wiki |

```powershell
python tools\wiki_maintain.py tags-lint
python tools\wiki_maintain.py tags-lint --report
# → audit/maintenance-reports/tags-lint-YYYY-MM-DD.md
```

**Agent prompt (pair with report):**

```text
Read audit/maintenance-reports/tags-lint-YYYY-MM-DD.md.

Phase A (low-cost): Add missing tags: field and fill empty tags for wiki/reference pages.
- Use page category + title + content to suggest 2-4 relevant tags.
- Prefer existing high-frequency tags from the report's frequency table.
- Format: tags: [tag1, tag2, tag3]

Process the first 20 missing-tags-field issues. After each batch, verify:
  python tools/wiki_maintain.py tags-lint
```

See [`audit/example-reports/tags-lint-example.md`](audit/example-reports/tags-lint-example.md) for sample output.

---

#### `scan` — Full maintenance scan

Runs all report-only checks in a single pass and produces a combined report.

```powershell
python tools\wiki_maintain.py scan --report
# → audit/maintenance-reports/maintenance-report-YYYY-MM-DD.md

# With external pending digest directory
python tools\wiki_maintain.py scan --report --pending-dir "D:\path\to\pending-digest"
```

The report includes a summary table, per-check details, and a suggested next-agent prompt. The CI gate (`validate-wiki.ps1`) parses the `totals:` line from scan output.

See [`audit/example-reports/scan-report-example.md`](audit/example-reports/scan-report-example.md) for sample output.

---

#### `audit-resolve` — Audit inbox lifecycle

Resolves open audit items by moving them to `audit/resolved/`, rewriting frontmatter, and appending a `# Resolution` section.

```powershell
# Dry-run (default)
python tools\wiki_maintain.py audit-resolve content-audit-2026-05-29.md --summary "Batches 1-7 complete"

# Apply
python tools\wiki_maintain.py audit-resolve content-audit-2026-05-29.md --summary "Batches 1-7 complete" --apply

# List with resolved count
python tools\wiki_maintain.py audit-list
python tools\wiki_maintain.py audit-list --include-resolved
```

---

### CI gate: `validate-wiki.ps1`

A PowerShell wrapper that runs `scan` and exits non-zero if any errors are found.

```powershell
pwsh tools\validate-wiki.ps1

# With pending directory
pwsh tools\validate-wiki.ps1 -PendingDir "D:\path\to\pending-digest"
```

The script parses the `totals: errors=N warnings=M info=P` line from scan output. Exit 0 = PASS (no errors), exit 1 = FAIL.

---

### Content quality triage: `gen_content_audit.py`

A one-shot tool that scans `wiki-pages/` for `status: wiki` or `reference` pages with short bodies (< 500 chars), detects content signals (video, GitHub, CTA, external URLs), and suggests triage actions.

```powershell
python tools\gen_content_audit.py
# → audit/content-audit-YYYY-MM-DD.md
```

**Signal types:** `video`, `github`, `cta`, `ext_url`, `tw_url_only`, `raw_gone`, `lingorm`

**Suggested actions:** `re-ingest`, `ocr-images`, `demote-stub`, `manual-review`

See [`audit/example-reports/content-audit-example.md`](audit/example-reports/content-audit-example.md) for sample output.

---

### Stub page generator: `fill_threads_stub_pages.py`

Batch-creates stub pages from `raw/threads-saved/` source files. Includes author extraction from Threads URLs and OCR sanity checks.

```powershell
# Dry-run
python tools\fill_threads_stub_pages.py

# Apply
python tools\fill_threads_stub_pages.py --apply --limit 10
```

---

### OCR fetch tool: `wiki_ocr/`

Reads content audit reports, finds wiki pages marked for OCR, fetches their original Threads post images via Playwright, OCRs them through Gemini, and appends a `## 圖片文字` section.

```powershell
# Dry-run
python tools\wiki_ocr\audit_ocr.py audit\content-audit-2026-05-29.md

# Apply with limit
python tools\wiki_ocr\audit_ocr.py audit\content-audit-2026-05-29.md --apply --limit 3

# Write report
python tools\wiki_ocr\audit_ocr.py audit\content-audit-2026-05-29.md --report
```

Requires `GEMINI_API_KEY` in `.env` and Playwright for browser-based image extraction.

---

### Public agent instructions sync

```powershell
# Regenerate AGENTS.md + AGENTS_en.md from private CLAUDE.md
python tools\sync_public_agents.py --source-ref master

# Check sync status without writing
python tools\sync_public_agents.py --source-ref master --check
```

---

### `wiki-maintenance` skill (Claude Code)

A Claude Code project skill (`.claude/commands/wiki-maintenance.md`) that automates the full maintenance workflow.

**Invoke:**

```text
/wiki-maintenance
```

**What it does:**

1. Runs `scan --report` and reads the latest report.
2. Presents a P0–P3 triage table, asks which priority to handle.
3. Batch-fixes issues: P0 all / P1 ≤20 / P2 ≤15 per batch.
4. Runs `pwsh tools/validate-wiki.ps1` after each batch (CI gate).
5. Updates `tasks/current-handoff.md` when done.

**Triage priority:**

| Priority | Issue types | Action |
|----------|------------|--------|
| **P0** | `status-audit` errors, `canonical-guard` conflicts, `duplicates` errors | Fix all immediately |
| **P1** | `index-lint` warnings, `xref-lint` broken links | Fix this session, ≤20/batch |
| **P2** | `readability-lint`, `tags-lint`, `xref-lint` orphans/missing-xref | Fix when time allows, ≤15/batch |
| **P3** | `coverage` ingest candidates, `blocked` records | Report only, no auto-fix |

**Agent prompts for skill:**

```text
/wiki-maintenance
```

After triage, specify priority:

```text
Handle P0 and P1.
```

Target specific issues:

```text
/wiki-maintenance

After triage, only fix P2 readability-lint single-dump issues, first 15.
Run validate-wiki.ps1 then stop.
```

---

### Current frontmatter constraints

The `作者` field is treated as a YAML list field:

```yaml
作者: ["@handle"]
作者: []
```

These are invalid and should not be reintroduced:

```yaml
作者: [@handle]
作者: [handle]
```

Surfaced through `status-audit` and `canonical-guard`.

---

## Example Reports

The `audit/example-reports/` directory contains sanitized sample outputs from each tool, demonstrating report formats without exposing private wiki content:

| Report | Tool | Shows |
|--------|------|-------|
| [`scan-report-example.md`](audit/example-reports/scan-report-example.md) | `scan --report` | Full aggregated maintenance report |
| [`xref-lint-example.md`](audit/example-reports/xref-lint-example.md) | `xref-lint --report` | Broken wikilinks, orphan pages, xref section issues |
| [`readability-lint-example.md`](audit/example-reports/readability-lint-example.md) | `readability-lint --report` | Undigested wiki pages with signal breakdown |
| [`tags-lint-example.md`](audit/example-reports/tags-lint-example.md) | `tags-lint --report` | Missing/empty tags, singleton tags, frequency stats |
| [`content-audit-example.md`](audit/example-reports/content-audit-example.md) | `gen_content_audit.py` | Content quality triage with signals and actions |

## Included Maintenance Outputs

In a private working vault, `tasks/` and `audit/` are the operational layers for handoffs, reports, and audit lifecycle. The public scaffold keeps only placeholder directories; generated reports are intentionally ignored so private maintenance state does not leak into showcase commits.

## Page Statuses

Each wiki page can be marked with a frontmatter status:

```yaml
status: stub | wiki | reference
```

- `stub`: A lightweight bookmark or placeholder that has not been fully digested.
- `wiki`: A synthesized, structured knowledge page.
- `reference`: A high-preservation page for technical documentation, GitHub repositories, APIs, or detailed how-to material.

Private working vaults may define category-specific exceptions or additional statuses. Those private exceptions are intentionally omitted from the public scaffold.

## Preservation Levels

The ingestion workflow chooses how much source detail to preserve:

- **Level 1: Opinion or short-form notes**: Summarize and condense.
- **Level 2: Tutorials and how-to material**: Preserve commands, steps, examples, and configuration details.
- **Level 3: Tool documentation and GitHub references**: Preserve technical detail almost completely, reorganizing structure instead of compressing content.

## Indexing Rules

Indexes live under `wiki-pages/index/` and serve as navigation, dashboards, and capability maps.

Common index types:

- A global index for the entire wiki.
- Category indexes for major knowledge areas.
- Capability indexes for cross-topic questions like "which tools help me reduce token usage?"
- Status dashboards that track how many pages are `stub`, `wiki`, or `reference`.

Index entries should contain meaningful summaries, not only URLs. A good summary includes a concrete method, tool list, number, or conclusion.

When an index entry may collide with a same-name file under `raw/`, the safer format is a Markdown relative link rather than a bare wikilink, for example:

```markdown
[Page Title](<../分類/Page Title.md>)
```

## Relationship To Personal Wiki

This repository is intentionally separate from [`hikaru-yeh/personal-wiki`](https://github.com/hikaru-yeh/personal-wiki). They are both LLM-maintained wiki systems, but they protect different kinds of knowledge and therefore need different rules.

| Area | This Repository: `knowledge-wiki` | Personal Wiki: [`hikaru-yeh/personal-wiki`](https://github.com/hikaru-yeh/personal-wiki) |
|---|---|---|
| Content type | External knowledge collection: saved posts, tool notes, AI workflows, tutorials, and reusable methods | Personal facts and history: identity, relationships, career records, interviews, courses, and life events |
| Sensitivity | Lower; mostly public or shareable sources | Higher; may include PII, relationships, career context, salary notes, and private records |
| Maintenance rhythm | Continuous ingestion whenever useful external material appears | Event-driven updates around interviews, jobs, courses, milestones, and personal changes |
| Privacy rules | Lightweight; focused on keeping the public scaffold free of private source material | Explicit privacy and sanitization rules for personal facts and records |
| Main audience | The owner and potentially shareable readers | The owner only in the private version |
| Agent-rule complexity | Medium; optimized for ingesting, indexing, querying, and maintenance reporting | Higher; includes privacy, lifecycle metadata, correction flows, and people/entity disambiguation |

Merging the two would create the wrong safety trade-off. Applying personal-wiki privacy rules here would make ordinary knowledge ingestion too heavy; applying this repository's lighter rules to a personal wiki would be unsafe.

The better pattern is one-way bridging: the personal wiki may reference methodology pages from this knowledge wiki, but each vault keeps its own rules, ownership, and privacy model. For example, a private interview-prep page can cite `[[knowledge-wiki::Resume Optimization]]` without copying that methodology page into the personal vault.

## Why This Exists

This repository is not a generic note dump. It is an example of using LLMs as knowledge maintainers: raw material stays untouched, curated pages become queryable and reusable, and the wiki gradually turns scattered personal inputs into an organized working memory.

The private version contains the actual notes. This public-facing scaffold is designed to show the system design, folder taxonomy, maintenance tooling, and skill-assisted workflow without exposing personal data.
