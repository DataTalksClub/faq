---
id: 950192cbcc
question: 'GCS Bucket: Fix Error when importing FHV data to GCS'
sort_order: 3
---

If you receive the error 

```python
gzip.BadGzipFile: Not a gzipped file (b'\n\n')
```

this is because you have specified the wrong URL to the FHV dataset. Make sure to use:

```
https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/{dataset_file}.csv.gz
```

Emphasize the `/releases/download` part of the URL.