---
name: add-faq-record
description: Add or update a single FAQ entry in this repository, or identify when fixing unclear canonical source material is the better solution. Use when asked to add something to the FAQ, create an FAQ record, document a recurring course question, or turn a question, screenshot, chat thread, issue, or other source into durable guidance.
---

# Add an FAQ Record

Create durable guidance in the right place without duplicating existing coverage or masking a fixable problem in the canonical source.

## Workflow

1. Read `CONTRIBUTING.md` and inspect the supplied source. Extract the reusable question and its verified answer; do not copy chat-specific wording that will not help future readers.
2. Check the canonical course instructions, code, or configuration behind the question. Decide whether the confusion is a recurring edge case that belongs in the FAQ or an avoidable ambiguity or defect in the original material.
3. Prefer fixing the canonical source when a focused clarification or correction would prevent the problem for future students. Do not also create an FAQ unless it remains useful after the source fix. If editing the source is outside the authorized scope or repository, explain the root-cause fix and get approval before changing it.
4. If an FAQ is still warranted, identify the course and section. Confirm the section id and topic in `_questions/<course>/_metadata.yaml`; never infer module numbering from another course.
5. Search `_questions/<course>/` for the question's main concepts and likely synonyms. If an existing entry fully answers it, do not add a duplicate. If the source adds useful information, update the existing entry instead.
6. Inspect every file in the target section. Set `sort_order` to one more than the highest existing value and use the same zero-padded number as the filename prefix. Avoid collisions in both `sort_order` and filename prefix.
7. Generate a fresh 10-character lowercase hexadecimal id. Use this exact file format:

   ```text
   _questions/<course>/<section>/<NNN>_<id>_<short-slug>.md
   ```

8. Write the record with matching frontmatter:

   ```markdown
   ---
   id: <10-character-id>
   question: "<clear, searchable question>"
   sort_order: <number without zero padding>
   ---

   <direct answer first, followed only by details needed to act on it>
   ```

9. Keep the answer accurate, concise, and self-contained. Add runnable code or authoritative links only when useful. Preserve established terminology and formatting in neighboring records. Do not create a new metadata section unless the user explicitly requests it.
10. Validate each changed repository with its relevant checks. For FAQ changes, run `git diff --check` and `make test-website`. Inspect `git status --short` and report whether the result was a source fix, an FAQ change, or both. Do not commit unless the user asks.

## Decision Rules

- Make a reasonable placement choice when the course and section are clear from context; ask only when different choices would materially change the record.
- Treat an FAQ as supplementary documentation, not a substitute for correcting misleading, incomplete, or broken canonical material.
- Prefer a source fix when the original instructions cause the confusion and can explain the required action at the point where students need it.
- Keep an FAQ when the problem can still occur despite correct source material, spans multiple sources, or provides reusable troubleshooting that would distract from the main instructions.
- Treat screenshots and chat threads as source material, not assets to publish, unless the image itself is necessary to understand the answer.
- Verify technical or time-sensitive claims against the course repository or authoritative documentation rather than guessing.
- Preserve unrelated working-tree changes.
