---
id: b943770904
question: Negsignal:SIGKILL while converting data files to parquet format
sort_order: 8
---

Got this error because the Docker container memory was exhausted. The data file was up to 800MB but my Docker container does not have enough memory to handle that.

**Solution:**

- Load the file in chunks with Pandas.
- Create multiple parquet files for each data file being processed.

This approach worked smoothly and resolved the issue.