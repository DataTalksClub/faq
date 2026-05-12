---
id: c8d2668615
question: 'Fix warning: Python 3.12 was not found on your system… Neither ''pyenv''
  nor ''asdf'' could be found to install Python.'
sort_order: 54
---

This warning occurs because the Pipfile is expecting Python 3.12, but the local container is likely running an older version, such as Python 3.8.12-slim, as shown in the video [5.6 - Environment Management : Docker](https://www.youtube.com/watch?v=wAtyYZ6zvAs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=57).

To resolve this issue, update the `Dockerfile` to use the appropriate version:

```dockerfile
FROM python:3.12.7-slim
```

Ensure that both Python versions (the local version shown in the Pipfile and the container version) match to guarantee compatibility.