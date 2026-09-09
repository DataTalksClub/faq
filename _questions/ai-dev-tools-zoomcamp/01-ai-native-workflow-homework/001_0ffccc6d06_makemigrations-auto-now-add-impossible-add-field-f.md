---
id: 0ffccc6d06
question: '`makemigrations` fails with “impossible to add the field ... auto_now_add=True”
  — how do I fix it?'
sort_order: 1
---

This error happens when you add `created_at = models.DateTimeField(auto_now_add=True)` to a Django model that already has rows in the database. Django can't invent timestamps for the existing rows, so it stops and asks for a default.

It's easy to miss because the prompt is interactive. If your coding agent runs `makemigrations` non-interactively, it crashes with `EOFError: EOF when reading a line` instead of showing the question — which looks like an unrelated bug.

Three common fixes:

1) Answer the interactive prompt
Run `uv run python manage.py makemigrations` yourself and choose the option that sets the default (often Django suggests `timezone.now`).

2) Recreate the database (if it's disposable)
For early homework/dev scenarios where the DB can be thrown away (the sqlite file should be in `.gitignore` anyway):

```bash
rm -f db.sqlite3
rm -f chores/migrations/0*.py     # only if those migrations are also throwaway
uv run python manage.py makemigrations
uv run python manage.py migrate
```

3) Avoid `auto_now_add` and use a default instead
If you want a timestamp without hitting the prompt, use a default value:

```python
from django.utils import timezone

created_at = models.DateTimeField(default=timezone.now)
```

Note: `auto_now_add=True` sets the value only on insert and is effectively read-only on updates. If you need to override timestamps in a seed script or tests, prefer `default=timezone.now`.

Tip for AI agents: if your agent evolves the models multiple times in one session, run `makemigrations` after each meaningful model change—small migrations are easier to interpret and revert.
