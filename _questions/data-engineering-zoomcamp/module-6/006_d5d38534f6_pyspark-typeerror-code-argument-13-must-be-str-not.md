---
id: d5d38534f6
question: 'PySpark: TypeError: code() argument 13 must be str, not int, while executing
  `import pyspark`  (Windows/ Spark 3.0.3 - Python 3.11)'
sort_order: 6
---

This error occurs because Python 3.11 has some inconsistencies with the older Spark 3.0.3 version.

### Solutions:

1. **Downgrade Python Version:**
   - Use Python 3.9. A conda environment can help in managing different Python versions.

2. **Upgrade PySpark Version:**
   - Install a newer PySpark version, such as 3.5.1 or above, which is compatible with Python 3.11.

```bash
# Example commands
conda create -n pyspark_env python=3.9
conda activate pyspark_env
pip install pyspark==3.5.1
```

Ensure that your environment is set up correctly to avoid version mismatches.