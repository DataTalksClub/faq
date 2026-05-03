---
id: b72ed00c7b
question: Warning when run load_yellow_data python script
sort_order: 48
---

### Warning Details:

```
RuntimeWarning: As the c extension couldn't be imported, google-crc32c is using a pure python implementation that is significantly slower. If possible, please configure a c build environment and compile extension warnings.warn(_SLOW_CRC32C_WARNING, RuntimeWarning)

Failed to upload ./yellow_tripdata_2024-01.parquet to GCS: Timeout of 120.0s exceeded, last exception: ('Connection aborted.', timeout('The write operation timed out'))

Failed to upload ./yellow_tripdata_2024-03.parquet to GCS: Timeout of 120.0s exceeded, last exception: ('Connection aborted.', timeout('The write operation timed out'))
```

### Issues:

1. **google-crc32c Warning**: The Google Cloud Storage library is using a slow Python implementation instead of the optimized C version.
2. **Upload Timeout Error**: Your file uploads are timing out after 120 seconds.

### Solutions:

1. **Install the C-optimized google-crc32c**
   
   ```bash
   pip install --upgrade google-crc32c
   ```

2. **Fix Google Cloud Storage Upload Timeout**
   
   - **Solution 1: Increase Timeout**
     
     ```python
     blob.upload_from_filename(file_path, timeout=300)  # Set timeout to 5 minutes
     ```