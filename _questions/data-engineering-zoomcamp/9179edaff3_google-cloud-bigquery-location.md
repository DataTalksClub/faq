---
course: data-engineering-zoomcamp
id: 9179edaff3
question: Google Cloud BigQuery Location Problems
section: 'Module 4: analytics engineering with dbt'
sort_order: 3060
---

When running a query on BigQuery sometimes could appear a this table is not on the specified location error.

For this problem there is not a straightforward solution, you need to dig a little, but the problem could be one of these:

Check the locations of your bucket, datasets and tables. Make sure they are all on the same one.

Change the query settings to the location you are in: on the query window select more -> query settings -> select the location

Check if all the paths you are using in your query to your tables are correct: you can click on the table -> details -> and copy the path.

