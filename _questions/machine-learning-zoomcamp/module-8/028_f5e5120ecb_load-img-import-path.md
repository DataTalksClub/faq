---
id: f5e5120ecb
question: 'ImportError: cannot import name ''load_img'' from ''tensorflow.keras.preprocessing.image'''
sort_order: 28
---

The import path moved in newer TF/Keras. Use:

```python
from tensorflow.keras.utils import load_img
```

instead of the older `tensorflow.keras.preprocessing.image` path shown in the videos.
