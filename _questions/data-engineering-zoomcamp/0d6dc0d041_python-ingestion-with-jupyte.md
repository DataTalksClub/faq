---
id: 0d6dc0d041
question: Python - Ingestion with Jupyter notebook - missing 100000 records
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1310
---

If you follow the video  and you execute all the same steps as Alexey does, you will ingest all the data (~1.3 million rows) into the table yellow_taxi_data as expected.
However, if you try to run the whole script in the Jupyter notebook for a second time from top to bottom, you will be missing the first chunk of 100000 records. This is because there is a call to the iterator before the while loop that puts the data in the table. The while loop therefore starts by ingesting the second chunk, not the first.

✅Solution: remove the cell “df=next(df_iter)” that appears higher up in the notebook than the while loop. The first time w(df_iter) is called should be within the while loop.

📔Note: As this notebook is just used as a way to test the code, it was not intended to be run top to bottom, and the logic is tidied up in a later step when it is instead inserted into a .py file for the pipeline

