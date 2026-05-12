---
id: b074e82488
question: Evidently service exit with code 2
sort_order: 6
---

When running the command `docker-compose up –build` and sending data to the real-time prediction service, the service returns "Max retries exceeded with url: /api". This issue occurs because the evidently service exits with code 2 due to "app.py" in the evidently service being unable to import `from pyarrow import parquet as pq`.

1. **Install the pyarrow module**:
   
   ```bash
   pip install pyarrow
   ```

2. **Restart your machine**.

3. **If the first and second solutions don’t work**:
   - Comment out the `pyarrow` module in "app.py" of the evidently service, as it may not be used, which resolved the issue in some cases.

