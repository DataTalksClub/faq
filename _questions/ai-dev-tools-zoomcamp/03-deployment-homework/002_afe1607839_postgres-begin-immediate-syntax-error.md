---
id: afe1607839
question: Why does swapping SQLite for PostgreSQL in Agent Relay (Homework 3, Question
  4) break authenticated requests with a syntax error?
sort_order: 2
---

`immediate_transaction()` in `database.py` starts every write with `BEGIN IMMEDIATE`, which is SQLite-only syntax. PostgreSQL rejects it, so every endpoint that goes through it fails (`authenticate`, `create_task`, `claim_one`, `heartbeat`, `commit_terminal`).

This is the storage seam that Question 4 asks you to port:

1. Emit `BEGIN IMMEDIATE` only for SQLite. `database.py` already has `_is_sqlite(DATABASE_URL)` for this.
2. On PostgreSQL, keep claims safe with row locking. Add `.with_for_update(skip_locked=True)` to the `select(Task)` in `storage.claim_one()`. SQLAlchemy leaves the clause out on SQLite, so the same code works on both.

If you skip step 2, concurrent workers can claim the same task, and a concurrent-claims test will be flaky.
