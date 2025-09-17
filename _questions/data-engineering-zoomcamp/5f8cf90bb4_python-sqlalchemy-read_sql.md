---
course: data-engineering-zoomcamp
id: 5f8cf90bb4
question: Python - SQLAlchemy - read_sql_query() throws "'OptionEngine' object has
  no attribute 'execute'"
section: 'Module 1: Docker and Terraform'
sort_order: 1400
---

First, check SQLAlchemy and Pandas version. Make sure they are both up-to-date. Upgrade them using pip/conda if needed.

Then, try to wrap the query using text:

from sqlalchemy import text

query = text("""SELECT * FROM tbl""") df = pd.read_sql_query(query, conn)

