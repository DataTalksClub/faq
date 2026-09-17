---
id: afe1607839
question: Why does swapping SQLite for PostgreSQL in Agent Relay (Homework 3, Question
  4) break authenticated requests with a syntax error?
sort_order: 4
---

This happens because the starter code’s `immediate_transaction()` issues SQLite-specific SQL: `BEGIN IMMEDIATE`. When `RELAY_DATABASE_URL` points at PostgreSQL, that statement is invalid, so every transaction that uses `immediate_transaction()` fails immediately (including calls made by `authenticate()`, `create_task()`, `claim_one()`, `heartbeat()`, and `commit_terminal()`).

Fix: only run `BEGIN IMMEDIATE` when the database URL is actually SQLite, and otherwise let SQLAlchemy use PostgreSQL’s normal transaction behavior (don’t emit the SQLite-only statement).

Example approach:
- Add an `_is_sqlite(database_url: str) -> bool` helper.
- In `immediate_transaction()`, call `connection.exec_driver_sql("BEGIN IMMEDIATE")` only if `_is_sqlite(DATABASE_URL)` is true.

Note: on SQLite, `BEGIN IMMEDIATE` also served as a concurrency/locking mechanism (preventing overlapping task claims). PostgreSQL’s default auto-begin doesn’t provide the same guarantee, so concurrent-claims behavior may still need follow-up hardening (e.g., using `SELECT ... FOR UPDATE SKIP LOCKED` on the claim query), as flagged by `SPEC.md`.