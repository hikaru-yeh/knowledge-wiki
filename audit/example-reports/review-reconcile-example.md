# Review Reconcile - 2026-06-01

Input: `tasks/review-findings.md`

This is a rule-based classification report. It does not modify wiki content.

## Summary

- Findings classified: 12

| Bucket | Count |
|---|---:|
| cleanup-caused | 3 |
| known-deferred | 2 |
| pre-existing | 4 |
| environmental | 1 |
| dismissed | 2 |

## cleanup-caused

- review-finding: Broken wikilink in index after page rename
- review-finding: Stub marker still present after promote
- review-finding: Author field reverted to bare string after batch edit

## known-deferred

- review-finding: Category stubs deferred by policy
- review-finding: Tags field empty on stub pages (not prioritized)

## pre-existing

- review-finding: Orphan page existed before current maintenance session
- review-finding: Missing Cross References section on old wiki page
- review-finding: Social-tone content in page ingested months ago
- review-finding: Duplicate URL group predating current tooling

## environmental

- review-finding: Threads post deleted, source URL now 404

## dismissed

- review-finding: False positive — heading inside code block counted as real heading
- review-finding: Singleton tag is intentional domain-specific term
