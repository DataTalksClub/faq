---
id: 663c1e915e
question: How do I check compatibility of local and container Spark versions?
sort_order: 27
---

You can check the version of your local Spark using:

```bash
spark-submit --version
```

In the `build.sh` file of the Python folder, ensure that `SPARK_VERSION` matches your local version. Similarly, ensure the PySpark you installed via pip also matches this version.