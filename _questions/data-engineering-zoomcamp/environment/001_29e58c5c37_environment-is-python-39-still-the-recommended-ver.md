---
id: 29e58c5c37
question: 'Environment: which Python version should I use?'
sort_order: 1
---

Python 3.10 or 3.11 is a safe default — it works with the libraries used across the course (pandas, SQLAlchemy, dbt, dlt, PySpark with recent Spark releases, etc.).

If you're following older recorded videos that use Python 3.9, that still works for everything except the very latest library versions; troubleshooting against the videos is easier on the version they use.

If a specific module uses a stricter requirement, the course repo's module README will say so.
