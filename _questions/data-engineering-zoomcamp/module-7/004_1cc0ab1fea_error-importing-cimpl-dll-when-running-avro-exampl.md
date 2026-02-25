---
id: 1cc0ab1fea
question: 'Error: Importing cimpl DLL when running Avro examples'
sort_order: 4
---


```
ImportError: DLL load failed while importing cimpl: The specified module could not be found
```

### Steps to Resolve:

1. **Verify Python Version:**
   
   Ensure you are using a compatible version of Python with the Avro library. Check the Python version and compatibility requirements specified by the Avro library documentation.

2. **Load Required DLL:**
   
   You may need to load `librdkafka-5d2e2910.dll` in your code before importing Avro. Add the following:
   
   ```python
   from ctypes import CDLL

   CDLL("C:\\Users\\YOUR_USER_NAME\\anaconda3\\envs\\dtcde\\Lib\\site-packages\\confluent_kafka.libs\\librdkafka-5d2e2910.dll")
   ```
   
   Note that this error may occur depending on the OS and Python version installed.

3. **Alternative Solution:**

   If you encounter `ImportError: DLL load failed while importing cimpl`, you can try the following solution in PowerShell:

   ```bash
   $env:CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
   ```

   This sets the DLL manually in the Conda environment.

### Source:

[Confluent-Kafka Python Issue #1186](https://githubhot.com/repo/confluentinc/confluent-kafka-python/issues/1186?page=2)
