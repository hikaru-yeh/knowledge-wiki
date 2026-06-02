# AGENTS_en.md

This file is the English companion to `AGENTS.md` for the public showcase
branch. Keep both files synchronized. If `AGENTS.md` changes, regenerate this
file in the same commit with:

```powershell
python tools\sync_public_agents.py
```

This public version intentionally omits private category exceptions, local
absolute paths, editor state, and project-only rules.

## Repository Structure

```text
knowledge-wiki/
├── AGENTS.md
├── AGENTS_en.md
├── README.md
├── raw/
│   ├── README.md
│   └── examples/
├── tasks/
│   └── maintenance-reports/
├── tools/
│   ├── wiki_maintain.py
│   └── sync_public_agents.py
└── wiki-pages/
    ├── README.md
    ├── index/
    │   └── example-index.md
    ├── example-topic/
    │   └── example-wiki-page.md
    └── log.example.md
```

Private working vaults may contain more category folders and operational task
files. Those files are intentionally ignored in the public showcase branch.

This repository is an LLM-maintained wiki scaffold.

Your job is to read source material under `raw/` and organize it into durable,
structured wiki pages under `wiki-pages/`.

## Source Of Truth

- `raw/` is the user-managed source pool.
- `wiki-pages/` is the LLM-maintained knowledge layer.
- Never modify files under `raw/`.
- Create, update, and maintain knowledge pages only under `wiki-pages/`.

## Raw Rules

- Treat `raw/` as read-only.
- Do not assume every file under `raw/` is pristine original material.
- `raw/` may contain original source files and imported Markdown pages.

## Global Ignore Rules

Unless the user explicitly asks otherwise, do not ingest these files as
knowledge pages:

- tool state files
- cache files
- temporary files
- hidden files
- pure template files
- pure index files
- source-side helper indexes

## Ingest Preservation Levels

Before ingesting any source, classify its preservation level. The default is to
organize and compress, but technical content must preserve executable detail.

### Level 1: Opinion Or Short-Form Notes

- Summarize and condense.
- Preserve the author's main viewpoint.
- Use for personal reactions, short comments, and social discussion.
- If the source includes executable commands, step lists, configuration, or
  code, upgrade it to at least Level 2.

### Level 2: Tutorials And How-To Material

- Do not compress how-to steps, commands, parameters, or configuration examples.
- Summarize background and conclusion if useful.
- Preserve code snippets, CLI commands, config examples, decision trees, and
  ordered procedures.

### Level 3: Tool Documentation And Repository References

- Preserve nearly all technical detail; structure instead of summarizing.
- Preserve API signatures, command signatures, parameters, examples,
  dependencies, and usage scenarios.
- You may reorganize headings, but do not delete technical details.
- If the source is long, prefer a complete main page plus split-out supplement
  pages over heavy compression.

### Classification Rules

- GitHub repositories and official documentation are Level 3.
- Any source with executable commands, code, or configuration is at least Level 2.
- When uncertain, choose the higher preservation level.

## Page Statuses

Every wiki page should use frontmatter status:

```yaml
status: stub | wiki | reference
```

- `stub`: a lightweight bookmark or placeholder that has not been digested.
- `wiki`: a synthesized, structured knowledge page.
- `reference`: a high-preservation page for repositories, official docs, APIs,
  or detailed technical references.

### Default Ingest Status

- Short-form opinion posts, Level 1: `stub`
- Tutorial-like posts with steps, commands, or examples, Level 2: `wiki`
- Tutorials, Level 2: `wiki`
- GitHub repositories or official documentation, Level 3: `reference`

### Index Display Rules

- `wiki` and `reference` pages appear as normal `[[wikilinks]]`.
- `stub` pages add the marker `（📌 stub）` after the title.
- Bookmark rows with no wiki page add `（⚠️ 書籤）` and do not use `[[...]]`.
- Within one H2 section, list `wiki` / `reference` pages before `stub` pages.

## Frontmatter Rules

For pages ingested from saved social sources, use this shape:

```markdown
---
網址: []
作者: []
tags: []
status: stub
---

## Main Content

...
```

### Author Field

- The `作者:` field must remain a valid YAML list field.
- Treat it as a list field.
- Correct:
  - `作者: ["@account"]`
  - `作者: []`
- Incorrect:
  - `作者: [@account]`
  - `作者: [account]`
  - `作者: account`
  - `作者: @account`
- If an author can be inferred from a Threads URL, write it as a quoted
  single-item list: `作者: ["@account"]`.
- After editing frontmatter, ensure the frontmatter can still be parsed as YAML.

## Modes

### Ingest

Use ingest mode when the user wants to convert a `raw/` source into wiki pages.

Required flow:

1. Read the source file.
2. Classify its preservation level.
3. Before editing `wiki-pages/`, propose a plan covering:
   - pages to create, with status and preservation level
   - pages to modify
   - links and indexes to update
   - draft index summaries
4. Wait for user approval.
5. Create or update the wiki pages.
6. Apply quality gate (for pages with planned `status: wiki` only):
   - Must have at least 2 meaningful H2/H3 headings (not counting `## Main Content`
     or `## Cross References`)
   - Must have a summary paragraph or key-point extraction (do not open with the
     source's first sentence verbatim)
   - If the source is a social media post, reorganize conversational prose into
     structured paragraphs
   - If any condition fails → mark as `status: stub` for later promotion
7. Update cross references if needed.
8. Append a log entry:
   - `## [YYYY-MM-DD] ingest | <document name> | status: <stub/wiki/reference>`
9. If page creation or deletion changes indexes, update relevant indexes and
   the global dashboard.

### Promote

Use promote mode when the user wants to upgrade a `stub` into a full `wiki` or
`reference` page.

Required flow:

1. Read the target stub and get its URL.
2. If the URL is accessible, fetch the content. If not, stop and report.
3. Reclassify the source preservation level.
4. Propose a promote plan with:
   - intended section structure
   - target status (`wiki` or `reference`)
   - updated index summary
5. Wait for user approval.
6. Rewrite the page and update `status: stub` to `wiki` or `reference`.
7. Update indexes by removing `（📌 stub）` and improving the summary.
8. Update the dashboard.
9. Append a log entry:
   - `## [YYYY-MM-DD] promote | <page> | stub → <wiki/reference>`

For batch promotion, first list all candidate stubs, estimate scope, and wait
for approval. Update indexes and dashboards incrementally as each page finishes.

### Re-Ingest

Use re-ingest mode when an existing page is too compressed to answer reasonable
questions.

Required flow:

1. Find the corresponding raw source.
2. Reclassify its preservation level.
3. Propose a re-ingest plan that explains missing detail, new sections, and
   whether the page should split.
4. Wait for user approval.
5. Rewrite the page while preserving frontmatter metadata where appropriate.
6. Append:
   - `## [YYYY-MM-DD] re-ingest | <page> | reason: <missing detail>`

### Reorganization

Use reorganization mode when pages need moving, renaming, merging, splitting, or
index restructuring.

Required flow:

1. Identify pages to move, rename, merge, or restructure.
2. Propose a plan listing:
   - old path to new path
   - links to update
   - indexes to update
   - metadata impact
3. Wait for user approval.
4. Move or rename pages under `wiki-pages/`.
5. Update all affected links and indexes.
6. Do not rewrite facts unless explicitly asked.
7. Append:
   - `## [YYYY-MM-DD] reorganization | <summary>`

### Query

Use query mode when the user asks about existing wiki knowledge.

Required flow:

1. Search curated pages under `wiki-pages/` first.
2. Answer from the wiki content.
3. Cite related page names.
4. Report knowledge gaps when found:
   - details were over-compressed and need re-ingest
   - related pages are still stubs and should be promoted
   - information is scattered across three or more pages and needs a capability
     index
   - content appears outdated
5. If the query creates a durable new insight, propose a new wiki page.
6. If existing content is wrong, switch to correction/update mode rather than
   silently modifying it.
7. Append:
   - `## [YYYY-MM-DD] query | <question summary>`

### Update

Use update mode when the user directly provides durable information that should
be written into the wiki and the source is not a `raw/` file.

Required flow:

1. Decide whether the information belongs in long-term wiki memory.
2. Find pages to create or update.
3. Propose an update plan covering content changes, sensitivity handling, and
   index impact.
4. Wait for user approval.
5. Update relevant pages.
6. Update indexes if affected.
7. Append:
   - `## [YYYY-MM-DD] update | <summary>`

### Lint

Use lint mode when the user requests a wiki health check.

Check for:

- contradictions
- orphan pages
- missing cross references
- broken wikilinks
- outdated claims
- broken internal structure
- index summary violations, including URL-only summaries or summaries outside
  the target length
- status mismatches between frontmatter and index markers
- reference pages that over-compress technical detail

Append:

- `## [YYYY-MM-DD] lint | <issue count>`

## Index Maintenance

- All indexes live under `wiki-pages/index/`.
- Keep the global index and status dashboard current.
- Keep category indexes current when applicable.
- Do not treat source-side indexes as canonical knowledge.

### Index Format

```markdown
# Category Index

← [[總索引]]

## Subcategory

| 文件 | 重點 |
|------|------|
| [[Wiki Page]] | One concrete summary |
| [[Stub Page]]（📌 stub） | Default bookmark summary |
| Bookmark Title（⚠️ 書籤） | Bookmark without a wiki page |
```

Rules:

- The second line is a backlink to the parent index.
- H2 sections must have meaningful names.
- Rows with wiki pages use links plus a concrete summary.
- Stub rows use the stub marker.
- Bookmark-only rows do not use `[[...]]`.
- Do not place URLs in index rows.
- Each major category should have one category index unless it becomes large
  enough to require a second layer.

### Index Summary Rules

The `重點` summary column must not contain only a URL.

A valid summary should include at least one of:

- concrete methods or technique names
- useful numbers
- a core conclusion
- included tools or concepts

Target length: 15-50 Chinese characters. Shorter summaries are usually too
thin; longer summaries are usually not digested enough.

### Markdown Relative Links

When an index entry could collide with a same-name file under `raw/`, prefer a
Markdown relative link:

```markdown
[Page Title](<../分類/Page Title.md>)
```

## Subcategory Naming Rules

When a category contains fundamentally different content types, use H2 section
names that clearly indicate format or medium.

### Dimension: Format / Medium

When a topic has content in different media, prefix H2 sections by medium:

- `Video-XXX`: video clips, livestream segments, instructional recordings
- `Writing-XXX`: articles, stories, essays, long-form notes
- `Interview-XXX`: interviews, conversations, Q&A transcripts
- `Visual-XXX`: image sets, photo collections, visual material

Rules:

- If a category has only one format, skip the prefix and name by content meaning.
- Do not mix different media formats within one H2 section.

## Index Location Rules

- All indexes live under `wiki-pages/index/`, not inside category folders.
- Each major category should have exactly one index file; subcategories fold in
  as H2 sections.
- Do not create a separate index file for a subcategory unless the category
  grows too large for a single file.
- Capability indexes (`能力-*.md`) are horizontal cross-cutting indexes and exist
  separately; they do not replace vertical category indexes.

## Capability Indexes

When several pages support the same practical capability, maintain horizontal
capability indexes under `wiki-pages/index/`.

Suggested naming:

- `能力-程式拆模組.md`
- `能力-Agent優化.md`
- `能力-省 Token.md`

Create or suggest a capability index when:

- more than three pages accumulate around the same capability
- the user asks for recommendations, combinations, or alternatives

## Global Dashboard

The global index should contain a status dashboard:

```markdown
## 狀態儀表板

| 主題 | Wiki | Reference | Stub | 總計 |
|------|------|-----------|------|------|
| AI 工具 | 8 | 8 | 17 | 33 |
```

Update it after ingest, promote, and reorganization work.

## Roles

User responsibilities:

- decide what to ingest
- add new material to `raw/`
- ask questions
- request lint checks
- decide when stubs should be promoted

Agent responsibilities:

- read and understand source material
- choose ingest depth based on preservation level
- create and maintain pages under `wiki-pages/`
- maintain cross references
- maintain indexes, summaries, and dashboard counts
- report knowledge gaps during query work
- append operation logs
- never modify `raw/`

## Guardrails

- Do not create a new wiki page without updating indexes.
- Do not create duplicate overview pages due to hardcoded filenames.
- Do not treat helper files as knowledge content unless explicitly asked.
- When uncertain, preserve more source detail and structure it rather than
  compressing too much.
- Use conservative entity disambiguation.
- `reference` pages must preserve technical details.
- Index summaries must not be URL-only.
