---
course: data-engineering-zoomcamp
id: 4277a9cb86
question: Postgres - "Column does not exist" but it actually does (Pyscopg2 error
  in MacBook Pro M2)
section: 'Module 1: Docker and Terraform'
sort_order: 1240
---

In the join queries, if we mention the column name directly or enclosed in single quotes it’ll throw an error says “column does not exist”.

✅Solution: But if we enclose the column names in double quotes then it will work

