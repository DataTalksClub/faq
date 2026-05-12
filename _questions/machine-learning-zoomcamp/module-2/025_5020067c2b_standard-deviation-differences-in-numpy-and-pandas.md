---
id: 5020067c2b
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_38e67375.png
- description: 'image #2'
  id: image_2
  path: images/machine-learning-zoomcamp/image_8ad3d822.png
question: Standard Deviation Differences in Numpy and Pandas
sort_order: 25
---

Numpy and Pandas use different equations to compute the standard deviation. Numpy uses the population standard deviation by default, whereas Pandas uses the sample standard deviation.

**Numpy**

<{IMAGE:image_1}>

**Pandas**

<{IMAGE:image_2}>

Pandas computes the standard deviation using one degree of freedom by default. You can modify the degree of freedom in Numpy to achieve a similar result by using the `ddof` parameter:

```python
import numpy as np

np.std(df.weight, ddof=1)
```

The result will be similar if we set `ddof=1` in Numpy.