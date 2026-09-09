---
id: 0407213397
question: 'There is an error when opening the table using `dbtable = db.open_table("notion_pages___homework")`:
  `FileNotFoundError: Table notion_pages___homework does not exist. Please first call
  db.create_table(notion_pages___homework, data)`'
sort_order: 3
---

The error indicates that the table you open doesn't match the table the dlt pipeline created.

Make sure you changed all instances of "employee_handbook" to "homework" in your pipeline settings, then open the table the pipeline actually created:

```python
dbtable = db.open_table("notion_pages___homework")
```