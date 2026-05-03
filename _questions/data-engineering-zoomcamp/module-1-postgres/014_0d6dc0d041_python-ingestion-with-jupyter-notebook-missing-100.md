---
id: 0d6dc0d041
question: 'Python: Ingestion with Jupyter notebook - missing 100000 records'
sort_order: 14
---

If you follow the video [1.2.2 - Ingesting NY Taxi Data to Postgres](https://www.youtube.com/watch?v=2JM-ziJt0WI&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=5) and execute the same steps, you will ingest all the data (~1.3 million rows) into the table `yellow_taxi_data`. However, running the whole script in the Jupyter notebook for a second time from top to bottom will result in missing the first chunk of 100,000 records. This occurs because a call to the iterator appears before the while loop, leading to the second chunk being ingested first.

### Solution:

- Remove the cell `df=next(df_iter)` located higher up in the notebook than the while loop.
- Ensure the first `w(df_iter)` call is within the while loop.

📔 **Note:** The notebook is used to test the code and is not intended to be run top to bottom. The logic is organized in a later step when inserted into a `.py` file for the pipeline.