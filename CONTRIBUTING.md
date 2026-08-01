# Contributing to the DataTalks.Club FAQ

The FAQ collects the questions Zoomcamp students actually hit, and the answers
that unblocked them. There are two ways to help: propose an answer that isn't
there yet, or open a pull request to fix one that is.

## Proposing an answer

Open a [FAQ proposal](https://github.com/DataTalksClub/faq/issues/new?template=faq-proposal.yml)
and fill in the course, the question, and the answer.

A bot takes it from there. It compares your proposal against the existing entries
for that course, and either opens a pull request for a maintainer to review or
closes the issue with a comment saying why: the question is already answered, or
the proposal belongs to a different Zoomcamp. Pick the course carefully, since the
bot only ever looks at the one you chose. The [README](README.md#the-agent)
describes how it decides.

## Writing a good entry

Either way, an entry is worth more when it's written the way the student who needs
it will go looking for it.

Ask the question in the words a student would search:

- ✅ "How do I install Python dependencies using uv?"
- ❌ "Dependencies"

Start with a question word (How, What, Why, When) and use the vocabulary of the
error message or the course material. Search across the FAQ is keyword-based, so a
question that shares no words with the way people phrase the problem won't be
found, however good the answer under it is.

Keep one problem per entry. When an entry answers two things, neither is findable
by its own symptoms, and someone hitting only the second one scrolls past it.

Answer with the fix first and the explanation after. Whoever is reading is blocked
right now.

Make the code runnable as written: every variable defined, every import present,
and the same package versions the course uses. A snippet that needs repair is
worse than no snippet, because it costs the reader time before they find that out.

Link the canonical source instead of paraphrasing it. When the tool changes, a
link still points at the truth and a paraphrase has quietly gone stale.

If the confusion came from unclear course material, say so in the issue. Fixing
the material is usually better than writing an FAQ entry around it.

## Updating an existing entry

An answer that's already published but wrong, outdated, or thin doesn't need an
issue. Edit the file and open a pull request.

Every answer is one markdown file under `_questions/<course>/<section-id>/`, with
the id, the question, and the sort order in its frontmatter:

```markdown
---
id: eaa17a9dc6
question: My Module 2 homework cosine similarity (Q2) isn't any of the options, what am I doing wrong?
sort_order: 1
---

The most common cause is using a different embedding model than the homework
specifies.
```

Leave the `id` as it is. It's the anchor the entry's URL is built from, so
changing it breaks every link pointing at that answer. The filename can stay as it
is too, even if you reword the question.

New entries go through the proposal form rather than a hand-written file, because
ids and sort order have to be assigned against everything already in the section.

Check the result before you send it:

```bash
make website
make test
```

## Questions

Open an issue with the `question` or `bug` label.
