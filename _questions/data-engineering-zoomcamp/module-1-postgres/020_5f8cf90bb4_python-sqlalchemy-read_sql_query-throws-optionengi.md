---
id: 5f8cf90bb4
question: Python - SQLAlchemy - read_sql_query() throws "'OptionEngine' object has
  no attribute 'execute'"
sort_order: 20
---

First, check the versions of SQLAlchemy and pandas — `pip install --upgrade sqlalchemy pandas` (or `uv add --upgrade sqlalchemy pandas`).

Then, try to wrap the query using `text`:

```python
from sqlalchemy import text

query = text("SELECT * FROM tbl")
df = pd.read_sql_query(query, conn)
```