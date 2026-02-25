---
id: cd5d3e8423
question: hadoop “wc -l” is giving a different result than shown in the video
sort_order: 42
---

If you are using `wc -l fhvhv_tripdata_2021-01.csv.gz` with the gzip file as the file argument, you will get a different result, obviously, since the file is compressed.

Unzip the file and then use:

```bash
wc -l fhvhv_tripdata_2021-01.csv
```

to get the right results.