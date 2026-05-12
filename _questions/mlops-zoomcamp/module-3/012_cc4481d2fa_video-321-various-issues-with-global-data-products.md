---
id: cc4481d2fa
question: "Mage GDP block hangs or fails with `AttributeError: 'NoneType' object has
  no attribute 'to_dict'`"
sort_order: 12
---

If the Global Data Products block in Video 3.2.1 takes forever and eventually fails with:

```
Pipeline run xx for global data product training_set: failed
AttributeError: 'NoneType' object has no attribute 'to_dict'
```

Try these in order:

1. Check that the project and repo_path in the block config match your setup:

   ```python
   "project": "unit_2_training",
   "repo_path": "/home/src/mlops/unit_2_training",
   ```

2. Restart the kernel from the Run menu, then bring Docker down and back up via the script.

3. If it still fails, rebuild the block: remove the connections from the `hyperparameter_tuning/sklearn` block to its upstream blocks (click each connector → Remove Connection), delete the Global Data Product block from the Tree panel (right click → Delete Block, ignore dependencies), then drag a fresh Global Data Products block to be the first in the pipeline, rename it to match the video, and re-run it.

You can repeat the same recovery steps for the corresponding file in `unit_3_observability`.

Reference docs:

- [Project Management](https://docs.mage.ai/platform/projects/management)
- [Project Structure](https://docs.mage.ai/design/abstractions/project-structure)
- [Global Data Products Overview](https://docs.mage.ai/orchestration/global-data-products/overview)
