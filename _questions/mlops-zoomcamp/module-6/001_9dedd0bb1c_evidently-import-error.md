---
id: 9dedd0bb1c
question: 'Evidently: Import Error'
sort_order: 1
---

When running the command:

```python
from evidently import ColumnMapping
```

The following import error occurs:

```plaintext
ImportError: cannot import name 'ColumnMapping' from 'evidently'
```

1. Uninstall the latest version of `evidently`:
   
   ```bash
   pip uninstall evidently -y
   ```

2. Install an older compatible version:
   
   ```bash
   pip install evidently==0.4.18
   ```

3. Restart the kernel to reload the environment.