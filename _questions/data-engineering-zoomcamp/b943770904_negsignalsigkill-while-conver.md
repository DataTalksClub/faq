---
id: b943770904
question: Negsignal:SIGKILL while converting data files to parquet format
section: Module 6: streaming with kafka
course: data-engineering-zoomcamp
sort_order: 3950
---

Got this error because the docker container memory was exhausted. The data file was up to 800MB but my docker container does not have enough memory to handle that.

Solution was to load the file in chunks with Pandas, then create multiple parquet files for each dat file I was processing. This worked smoothly and the issue was resolved.

