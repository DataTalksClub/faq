---
id: 0cf2421dca
question: Why do Grafana pie charts show `n` or only one feedback slice even when
  the PostgreSQL query returns separate relevance/feedback categories?
sort_order: 8
---

If your PostgreSQL query returns multiple categories as multiple rows (e.g., `feedback`, `n`), but your pie chart is configured/reducing to a single numeric field (often `n`), Grafana may collapse the rows and end up with only one slice.

Fix: use the `Rows to fields` transformation so each category becomes its own numeric field.

In the panel editor:
1) Set the PostgreSQL query `Format` to `Table` and ensure it returns one row per category, with:
   - a text category column (e.g., `feedback`)
   - a numeric count column (e.g., `n`)
2) Open `Transformations` → `Add transformation` → `Rows to fields`.
3) In the field mapping table:
   - set the category column (e.g., `feedback`) to `Use as` → `Field name`
   - set the count column (e.g., `n`) to `Use as` → `Field value`
4) Use the resulting fields in the pie chart.
   - With one count per field, use `Calculate` → `Last (not null)` to keep each category as its own slice.
   - Enable legend names/values to verify you get e.g. `thumbs up: 3` and `thumbs down: 2`.

Example read-only query (two feedback categories):
```SQL
WITH feedback_counts(feedback, n) AS (
VALUES ('thumbs up', 3), ('thumbs down', 2)
)
SELECT feedback, n
FROM feedback_counts;
```

Why this happens: Grafana can reduce a numeric column named `n` to a single value (often the last one), which produces one slice. Renaming labels alone doesn’t split the data into separate numeric fields per category—`Rows to fields` does.

Note: this kind of transform doesn’t populate an empty result; validate using real aggregates from the same DB and time range you’re charting.