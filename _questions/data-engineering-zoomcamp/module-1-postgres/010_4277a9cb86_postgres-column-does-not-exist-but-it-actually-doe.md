---
id: 4277a9cb86
question: 'Postgres: "Column does not exist" but it actually does (Pyscopg2 error
  in MacBook Pro M2)'
sort_order: 10
---

In join queries, if you mention the column name directly or enclose it in single quotes, you'll encounter an error saying "column does not exist".

**Solution:** Enclose the column names in double quotes, and it will work correctly.