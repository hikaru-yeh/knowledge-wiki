# AGENTS.md

This public branch is a scaffold for an LLM-maintained knowledge wiki. It intentionally omits the private source inbox, private curated pages, editor state, and agent session state.

## Agent Guidelines

- Treat `raw/` as read-only evidence. Public examples may live under `raw/examples/`.
- Treat `wiki-pages/` as the curated knowledge layer. Public examples may live under `wiki-pages/example-topic/` and `wiki-pages/index/`.
- Keep private vault content, local editor config, and generated maintenance reports out of public commits.
- Prefer report-only maintenance commands before any apply-style cleanup.
- When adding frontmatter, keep YAML valid. In particular, author arrays should use quoted strings:

```yaml
作者: ["@example"]
```

Empty author arrays should be:

```yaml
作者: []
```

Do not introduce invalid forms such as `作者: [@example]` or `作者: [example]`.
