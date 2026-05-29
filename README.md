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
- A lightweight maintenance tool layer for reporting wiki health, blocked pages, duplicate URLs, and ingest coverage before any apply workflow is allowed.

## Repository Structure

```text
knowledge-wiki/
├── AGENTS.md
├── AGENTS_en.md
├── raw/                             # User-managed source material, treated as read-only
│   ├── README.md
│   └── examples/                    # Synthetic publishable source examples
├── tasks/
│   └── maintenance-reports/         # Placeholder for generated local reports
├── tools/                           # Repo-specific maintenance scripts
│   ├── sync_public_agents.py        # Regenerate public AGENTS.md from private CLAUDE.md
│   ├── wiki_maintain.py
│   └── wiki_ocr/                    # Standalone audit-driven OCR fetch tool
│       ├── _gemini_client.py        # Gemini API wrapper (cloned from crawl-the-threads)
│       ├── _image_ocr.py            # Image OCR pipeline (Gemini-only, pruned clone)
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

## Maintenance Tooling

The repository includes a repo-specific report-first maintenance CLI:

```powershell
python tools\wiki_maintain.py <subcommand> [options]
```

Current rule of thumb:

- `raw/` is read-only.
- Current tooling is primarily report-only.
- Use reports to decide the next bounded cleanup batch.
- Do not run apply-style maintenance blindly from tooling.

### Maintenance architecture status

The maintenance architecture is inspired by:

- [`kfchou/wiki-skills`](https://github.com/kfchou/wiki-skills)
- [`lewislulu/llm-wiki-skill`](https://github.com/lewislulu/llm-wiki-skill)

The implementation is still a work in progress. The current public scaffold
shows the **report-first maintenance layer**, not a fully automated wiki
rewriter.

Implemented:

- public/private agent instruction sync: `AGENTS.md` and `AGENTS_en.md`
- session handoff report generation
- blocked content gap reporting
- status/frontmatter auditing
- index linting
- review finding reconciliation
- raw-to-wiki coverage reporting
- duplicate URL detection
- canonical guard checks for stale files and author frontmatter rules
- one-command `scan` aggregator
- pending raw-to-wiki matching (`pending-match`) and digest injection (`inject-pending --apply`)
- safe apply flows for promote (`promote-ready --apply`) and author field repair (`author-fix`)
- audit-list generation (`audit-list`)
- CI gate (`tools/validate-wiki.ps1`) that enforces 0 errors before publishing
- standalone audit-driven OCR fetch tool (`tools/wiki_ocr/`)

Not implemented yet:

- canonical cleanup automation
- delegate integration for multi-agent maintenance batches

### Common commands

```powershell
python tools\wiki_maintain.py status-audit --report
python tools\wiki_maintain.py canonical-guard --report
python tools\wiki_maintain.py index-lint --report
python tools\wiki_maintain.py coverage --report
python tools\wiki_maintain.py duplicates --report
python tools\wiki_maintain.py blocked-report
python tools\wiki_maintain.py handoff --task "batch-name" --next "next-step"
```

### Public agent instructions sync

The public branch keeps `AGENTS.md` as the sanitized version of the private working-vault `CLAUDE.md`, with `AGENTS_en.md` as the English companion. After changing `CLAUDE.md` on the private branch, regenerate both public instruction files from the public branch:

```powershell
python tools\sync_public_agents.py --source-ref master
```

To check whether either `AGENTS.md` or `AGENTS_en.md` is out of sync without writing:

```powershell
python tools\sync_public_agents.py --source-ref master --check
```

The sync script removes private category/project-only rules and keeps paths relative for public display. If `AGENTS.md` changes, `AGENTS_en.md` must be updated in the same commit.

### Subcommand reference

| Subcommand | Main purpose | Writes report/file | Output path | Changes `wiki-pages/` |
|---|---|---|---|---|
| `handoff` | Capture current session state for the next agent/session | Yes | `tasks/current-handoff.md` | No |
| `blocked-report` | List blocked pages that should not be promoted yet | Yes | `tasks/blocked-content-gaps.md` | No |
| `status-audit` | Audit `status` frontmatter and frontmatter schema issues | Optional with `--report` | `tasks/maintenance-reports/status-audit-YYYY-MM-DD*.md` | No |
| `index-lint` | Check index links, ambiguous bare links, missing targets, and stub marker mismatches | Optional with `--report` | `tasks/maintenance-reports/index-lint-YYYY-MM-DD*.md` | No |
| `review-reconcile` | Bucket review findings into cleanup-caused / deferred / pre-existing / environmental / dismissed | Yes | `tasks/maintenance-reports/review-reconcile-YYYY-MM-DD*.md` | No |
| `coverage` | Find raw source pages not yet ingested into the wiki | Optional with `--report` | `tasks/maintenance-reports/ingest-candidates-YYYY-MM-DD*.md` | No |
| `duplicates` | Detect duplicate frontmatter URLs and suggest canonicals | Optional with `--report` | `tasks/maintenance-reports/duplicates-YYYY-MM-DD*.md` | No |
| `canonical-guard` | Detect stale canonical conflicts and frontmatter author rule violations | Optional with `--report` | `tasks/maintenance-reports/canonical-guard-YYYY-MM-DD*.md` | No |

### OCR fetch tool

A standalone CLI under `tools/wiki_ocr/` that reads content audit reports, finds wiki pages marked for OCR, fetches their original Threads post images via Playwright, OCRs them through Gemini, and appends a `## 圖片文字` section to the wiki page.

```powershell
# dry-run: lists targets without making API calls or writes
python tools\wiki_ocr\audit_ocr.py audit\content-audit-2026-05-29.md
python tools\wiki_ocr\audit_ocr.py tasks\content-quality-audit.md

# apply: fetch images, OCR, write to wiki pages
python tools\wiki_ocr\audit_ocr.py audit\content-audit-2026-05-29.md --apply --limit 3
```

The tool supports two audit report formats (legacy free-text and standardized `ocr-images` token). It requires `GEMINI_API_KEY` in `.env` and Playwright for browser-based image extraction. Key components (`_gemini_client.py`, `_image_ocr.py`) are pruned clones from the companion `crawl-the-threads` pipeline, keeping only the Gemini OCR path.

### Current frontmatter constraints

The maintenance tooling treats frontmatter rules as hard constraints. In particular, the `作者` field is treated as a YAML list field:

```yaml
作者: ["@handle"]
作者: []
```

These are considered invalid and should not be reintroduced by future tooling:

```yaml
作者: [@handle]
作者: [handle]
```

This rule is surfaced through `status-audit` and `canonical-guard`, and future normalize/rewrite flows are expected to preserve valid list syntax.

## Included Maintenance Outputs

In a private working vault, `tasks/` is the operational layer for handoffs, blocked-page reports, promote inventories, and dated scan outputs. The public scaffold keeps only `tasks/maintenance-reports/.gitkeep`; generated reports are intentionally ignored so private maintenance state does not leak into showcase commits.

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
