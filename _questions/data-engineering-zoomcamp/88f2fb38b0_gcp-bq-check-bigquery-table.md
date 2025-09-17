---
id: 88f2fb38b0
question: GCP BQ - Check BigQuery Table Exist And Delete
section: Module 3: Data Warehousing
course: data-engineering-zoomcamp
sort_order: 2140
---

Reference:

Solution:

Combine with “Create External Table using Python”, use it before “client.create_table” function.

def tableExists(tableID, client):

"""

Check if a table already exists using the tableID.

return : (Boolean)

"""

try:

table = client.get_table(tableID)

return True

except Exception as e: # NotFound:

return False

