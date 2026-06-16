---
id: 4b30b918bc
question: 'Error: How to fix requests library only installs v2.28 instead of v2.32
  required for lancedb?'
sort_order: 8
---

If you encounter a 401 Client Error, it may indicate the need to grant access to the key or that the key is incorrect.

To install the correct version directly from the source, use the following command:

```bash
pip install "requests @ https://github.com/psf/requests/archive/refs/tags/v2.32.3.zip"
```
