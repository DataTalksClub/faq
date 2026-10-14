---
id: b1bd09b2d4
question: 'Why am I getting TypeError: ''list'' object is not callable when creating
  a NumPy array?'
sort_order: 41
---

This usually happens when `np.array` was accidentally overwritten by a `list` in an earlier Jupyter cell. Because the notebook kernel keeps variables/functions from previous runs, editing the cell that triggered the error may not be enough.

A typical cause is a cell like `np.array = [1100, 1300, 800]` (assignment instead of a call). Running `import numpy as np` again doesn't undo it, because the already-imported module is reused.

Quick fix:
1. Restart the Jupyter kernel (Kernel → Restart).
2. Re-import NumPy and re-create your array.

```python
import numpy as np

y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
```

After the restart, `np.array()` should refer back to NumPy's original function.

The same happens with built-ins: `list = [...]` or `sum = 0` shadow the function until you `del` the name or restart the kernel.
