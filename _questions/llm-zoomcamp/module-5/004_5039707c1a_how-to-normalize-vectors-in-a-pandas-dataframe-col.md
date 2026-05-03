---
id: 5039707c1a
question: How to normalize vectors in a Pandas DataFrame column (or Pandas Series)?
sort_order: 4
---

To normalize vectors in a Pandas DataFrame column, you can use the following approach:

```python
import numpy as np

normalize_vec = lambda v: v / np.linalg.norm(v)

df["new_col"] = df["org_col"].apply(normalize_vec)
```