---
id: bcedbb12fe
question: 'Windows pip install: "OSError [WinError 5] Access is denied"'
sort_order: 9
---

```
ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied
Consider using the `--user` option or check the permissions.
```

This means pip is trying to write into a system-wide Python install where you don't have write permission.

Two fixes:

- Install into your user site instead:
  ```bash
  pip install --user grpcio==1.42.0 tensorflow-serving-api==2.7.0
  ```
- Better: install into a project venv (no admin needed, no `--user` workaround):
  ```bash
  uv venv && source .venv/bin/activate    # or .venv\Scripts\activate on Windows
  uv add grpcio==1.42.0 tensorflow-serving-api==2.7.0
  ```
