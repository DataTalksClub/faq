# Contributing to the DataTalks.Club FAQ

The FAQ collects the questions Zoomcamp students actually hit, and the answers
that unblocked them. There are two ways to add one: open a proposal issue and let
the bot file it for you, or edit `_questions/` and send a pull request yourself.

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

Whichever route you take, an entry is worth more when it's written the way the
student who needs it will go looking for it.

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

## Sending a pull request

Every answer is one markdown file:

```text
_questions/<course>/<section-id>/NNN_<id>_<slug>.md
```

with the id, the question, and the sort order in its frontmatter:

```markdown
---
id: eaa17a9dc6
question: My Module 2 homework cosine similarity (Q2) isn't any of the options, what am I doing wrong?
sort_order: 1
---

The most common cause is using a different embedding model than the homework
specifies.
```

The section directory is the `id` of a section in that course's `_metadata.yaml`.
Each section there carries a `comment` describing what it owns, so read those
before choosing rather than guessing from the section name.

The three parts of the filename:

- `NNN` is the `sort_order` padded to three digits, and it has to match the
  `sort_order` in the frontmatter
- `<id>` is the first 10 characters of the MD5 of the question and the answer
  joined by a space, and it repeats in the frontmatter as `id`
- `<slug>` comes from the question, lowercased, with punctuation removed, spaces
  turned into hyphens, and the result cut to 50 characters

Generate the id the same way the bot does:

```bash
python -c "import hashlib, sys; print(hashlib.md5(sys.argv[1].encode()).hexdigest()[:10])" \
  "How do I check my Python version? Run python --version in your terminal."
```

If the `sort_order` you want is already taken, either take the next free number in
the section or renumber the entries below it. The bot has `actions.py` to shift
existing entries down; a pull request has to do it by hand.

Check the result before you send it:

```bash
make website
make test
```

## Questions

Open an issue with the `question` or `bug` label.
