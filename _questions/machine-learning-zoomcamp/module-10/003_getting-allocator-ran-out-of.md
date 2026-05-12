---
id: '4693802714'
question: 'Allocator (GPU_0_bfc) ran out of memory'
sort_order: 3
---

If you are running TensorFlow on your own machine and you start getting the following errors:

```
Allocator (GPU_0_bfc) ran out of memory trying to allocate 6.88GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
```

Try adding this code in a cell at the beginning of your notebook:

```python
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
```

After doing this, most issues should be resolved. Occasionally, the error may still appear during high-demand epochs, but re-running the code should typically resolve it.