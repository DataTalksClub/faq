---
id: e5ceadc2f4
question: 'Matplotlib: When I plotted using Matplotlib to check if the median has
  a tail, I got the error "FutureWarning: is_categorical_dtype is deprecated and will
  be removed in a future version. Use isinstance(dtype, CategoricalDtype) instead".
  How can I bypass this?'
sort_order: 24
---

To resolve this issue, you can try the following methods:

1. **Upgrade Pandas:**
   
   You can resolve this by installing the latest version of Pandas. Execute the following command in a Jupyter code cell:
   
   ```bash
   !pip install --upgrade pandas
   ```

2. **Suppress Warnings:**

   If you prefer not to change your Pandas version, you can suppress the warnings in your code:
   
   ```python
   import warnings
   import pandas as pd
   
   # Suppress FutureWarning messages
   warnings.simplefilter(action='ignore', category=FutureWarning)
   ```