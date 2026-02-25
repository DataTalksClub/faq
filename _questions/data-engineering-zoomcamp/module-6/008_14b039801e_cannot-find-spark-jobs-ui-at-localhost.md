---
id: 14b039801e
question: Cannot find Spark jobs UI at localhost
sort_order: 8
---

This is because the current port is in use, so the Spark UI will run on a different port. You can check which port Spark is using by running this command:

```
spark.sparkContext.uiWebUrl
```

If it indicates a different port, you should access that specific port instead. Additionally, ensure that there are no other notebooks or processes that might be using the same port. Clean up unused resources to avoid port conflicts.