---
id: e95bfafc0e
question: 'There is an error when running main(): FileNotFoundError: Table notion_pages___homework
  does not exist. Please first call db.create_table(notion_pages___homework, data)'
sort_order: 4
---

Make sure you open the correct table in line 3:

```python
dbtable = db.open_table("notion_pages___homework")
```