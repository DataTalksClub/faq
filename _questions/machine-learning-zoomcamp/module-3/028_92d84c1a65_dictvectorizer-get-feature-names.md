---
id: 92d84c1a65
question: 'DictVectorizer: ''object has no attribute get_feature_names'''
sort_order: 28
---

`get_feature_names()` was removed in sklearn 1.0+. Use `get_feature_names_out()` instead:

```python
list(dv.get_feature_names_out())
```
