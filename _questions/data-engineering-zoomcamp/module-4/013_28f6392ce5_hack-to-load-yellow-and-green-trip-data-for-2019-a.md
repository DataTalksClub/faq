---
id: 28f6392ce5
question: Hack to load yellow and green trip data for 2019 and 2020
sort_order: 13
---

I initially followed [this script](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/03-data-warehouse/extras/web_to_gcs.py) but it was taking too long for the yellow trip data. When I downloaded and uploaded the Parquet files directly to GCS, it worked, but there was a schema inconsistency issue when creating the BigQuery table.

I found another solution shared on YouTube, which was suggested by Victoria. You can watch it here:

[[Optional] Hack for loading data to BigQuery for Week 4 - YouTube](https://www.youtube.com/watch?v=Mork172sK_c&t=22s&ab_channel=Victoria)

Make sure to watch until the end, as there are some required schema changes.