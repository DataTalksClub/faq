---
course: data-engineering-zoomcamp
id: 950192cbcc
question: GCS Bucket - Fix Error when importing FHV data to GCS
section: 'Module 3: Data Warehousing'
sort_order: 2010
---

If you receive the error gzip.BadGzipFile: Not a gzipped file (b'\n\n'), this is because you have specified the wrong URL to the FHV dataset. Make sure to use 
Emphasising the ‘/releases/download’ part of the URL.

