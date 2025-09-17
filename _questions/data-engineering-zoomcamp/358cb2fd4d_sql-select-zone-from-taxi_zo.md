---
id: 358cb2fd4d
question: SQL - SELECT Zone FROM taxi_zones Error Column Zone doesn't exist
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1730
---

It is inconvenient to use quotation marks all the time, so it is better to put the data to the database all in lowercase, so in Pandas after

df = pd.read_csv(‘taxi+_zone_lookup.csv’)

Add the row:

df.columns = df.columns.str.lower()

