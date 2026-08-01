# Contributing to the DataTalks.Club FAQ

The FAQ collects the questions Zoomcamp students actually hit, and the answers
that unblocked them. Two ways to help: propose an answer that isn't there yet, or
fix one that is.

## Proposing an answer

Open a [FAQ proposal](https://github.com/DataTalksClub/faq/issues/new?template=faq-proposal.yml),
pick the course it belongs to, and write the question and the answer.

The rest is automatic. Your proposal gets drafted into an entry and a maintainer
reviews it before it goes live, and you get a comment on the issue either way,
including when the question turns out to be answered already.

## Writing a good entry

Either way, an entry is worth more when it's written the way the student who needs
it will go looking for it.

Ask the question in the words a student would search:

- ✅ "How do I install Python dependencies using uv?"
- ❌ "Dependencies"

Start with a question word (How, What, Why, When) and use the words from the error
message or the course material rather than a summary of them.

Keep one problem per entry, so each stays findable by its own symptoms.

Answer with the fix first and the explanation after. Whoever is reading is blocked
right now.

Make the code runnable as written: every variable defined, every import present,
and the same package versions the course uses.

Link the canonical source instead of paraphrasing it, so the entry doesn't go
stale when the tool changes.

If the confusion came from unclear course material, say so. Fixing the material is
usually better than writing an FAQ entry around it.

## Fixing an existing entry

An answer that's wrong, outdated, or thin doesn't need an issue. Edit the file
under `_questions/` and open a pull request.

Leave the `id` in the frontmatter as it is, since that's what links to the entry
point at. New answers go through the proposal form instead, so they land in the
right section in the right order.

## Questions

Open an issue with the `question` or `bug` label.
