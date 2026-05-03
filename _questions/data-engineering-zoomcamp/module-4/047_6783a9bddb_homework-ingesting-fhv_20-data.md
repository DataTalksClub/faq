---
id: 6783a9bddb
question: 'Homework: Ingesting FHV data from the course''s GitHub mirror'
sort_order: 47
---

If you're loading FHV trip data from the course's GitHub mirror into GCS / BigQuery and the input file isn't recognised as parquet, two things to check:

1. Append `?raw=true` to the URL so GitHub serves the raw file rather than its HTML preview page. For a templated URL, append `?raw=true` after the `.parquet`:

   ```
   .../fhv_tripdata_<YYYY>-<MM>.parquet?raw=true
   ```

2. Use the `blob` URL, not `tree` — the prefix should look like:

   ```
   https://github.com/alexeygrigorev/datasets/blob/master/nyc-tlc/fhv
   ```

   If your URL has `tree` instead of `blob`, replace it.

The `curl -sSLf` (or `wget`) call you use to download the file doesn't need to change.
