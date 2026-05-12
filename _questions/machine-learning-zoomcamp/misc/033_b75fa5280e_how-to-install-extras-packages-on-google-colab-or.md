---
id: b75fa5280e
question: How do I install extra packages on Google Colab or Kaggle?
sort_order: 33
---

In a notebook cell, prefix `pip install` with `!`:

```bash
!pip install tensorflow[and-cuda]==2.14
```

For packages with extras you want installed silently, use `-q`:

```bash
!pip install -q xgboost==2.1.0
```

Restart the runtime if a package overrides one that's already imported (Runtime → Restart runtime).
