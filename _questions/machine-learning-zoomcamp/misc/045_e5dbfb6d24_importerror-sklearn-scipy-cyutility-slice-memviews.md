---
id: e5dbfb6d24
question: 'ImportError importing `sklearn`: `scipy._cyutility` does not export expected
  C function `slice_memviewslice`'
sort_order: 45
---

This usually means your `scipy` installation is broken or incompatible with the installed `numpy` / `scikit-learn` versions (often after installing something with `pip` into a `conda` environment).

Try reinstalling the core scientific packages together, then restart your kernel:

```bash
python -m pip install --force-reinstall --no-cache-dir scipy numpy scikit-learn
```

After reinstalling, restart the Jupyter kernel.

If you keep running into package conflicts, consider using a dedicated `conda` environment (and try to avoid mixing `conda` and `pip` installs as much as possible).