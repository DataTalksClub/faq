---
id: 6affd2987c
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_1813f02b.png
question: 'Taxi Data: Yellow Taxi Trip Records downloading error'
sort_order: 1
---

When attempting to download the 2021 data from the [TLC website](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page), you may encounter the following error:

```bash
ERROR 403: Forbidden
```

<{IMAGE:image_1}>

We have a backup, so use it instead: [nyc-tlc-data](https://github.com/DataTalksClub/nyc-tlc-data)

So the link should be [yellow_tripdata_2021-01.csv.gz](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz).

**Note:** Make sure to [unzip the "gz" file](https://linuxize.com/post/how-to-unzip-gz-file/) (no, the "unzip" command won’t work for this).