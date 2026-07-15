---
name: add-faq-record
description: Add or update a single FAQ entry in this repository from a user-provided question, answer, screenshot, chat thread, issue, or other source. Use when asked to add something to the FAQ, create an FAQ record, document a recurring course question, or turn supplied context into a question file under `_questions/`.
---

# Add an FAQ Record

Create a concise, correctly placed FAQ entry without duplicating existing coverage or colliding with section numbering.

## Workflow

1. Read `CONTRIBUTING.md` and inspect the supplied source. Extract the reusable question and its verified answer; do not copy chat-specific wording that will not help future readers.
2. Identify the course and section. Confirm the section id and topic in `_questions/<course>/_metadata.yaml`; never infer module numbering from another course.
3. Search `_questions/<course>/` for the question's main concepts and likely synonyms. If an existing entry fully answers it, do not add a duplicate. If the source adds useful information, update the existing entry instead.
4. Inspect every file in the target section. Set `sort_order` to one more than the highest existing value and use the same zero-padded number as the filename prefix. Avoid collisions in both `sort_order` and filename prefix.
5. Generate a fresh 10-character lowercase hexadecimal id. Use this exact file format:

   ```text
   _questions/<course>/<section>/<NNN>_<id>_<short-slug>.md
   ```

6. Write the record with matching frontmatter:

   ```markdown
   ---
   id: <10-character-id>
   question: "<clear, searchable question>"
   sort_order: <number without zero padding>
   ---

   <direct answer first, followed only by details needed to act on it>
   ```

7. Keep the answer accurate, concise, and self-contained. Add runnable code or authoritative links only when useful. Preserve established terminology and formatting in neighboring records. Do not create a new metadata section unless the user explicitly requests it.
8. Validate with `git diff --check` and `make test-website`. Inspect `git status --short` and report the created or updated file plus the test result. Do not commit unless the user asks.

## Decision Rules

- Make a reasonable placement choice when the course and section are clear from context; ask only when different choices would materially change the record.
- Treat screenshots and chat threads as source material, not assets to publish, unless the image itself is necessary to understand the answer.
- Verify technical or time-sensitive claims against the course repository or authoritative documentation rather than guessing.
- Preserve unrelated working-tree changes.
