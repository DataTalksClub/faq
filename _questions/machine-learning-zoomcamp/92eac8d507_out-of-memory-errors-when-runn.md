---
course: machine-learning-zoomcamp
id: 92eac8d507
question: Out of memory errors when running tensorflow
section: 8. Neural Networks and Deep Learning
sort_order: 2990
---

I found this code snippet fixed my OOM errors, as I have an Nvidia GPU. Can't speak to OOM errors on CPU, though.

```

physical_devices = tf.configlist_physical_devices('GPU')

try:

tf.config.experimental.set_memory_growth(physical_devices[0],True)

except:

# Invalid device or cannot modify virtual devices once initialized.

pass

```

