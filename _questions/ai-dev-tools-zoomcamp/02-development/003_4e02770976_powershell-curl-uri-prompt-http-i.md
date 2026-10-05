---
id: 4e02770976
question: Why does `curl -i http://localhost:8000/...` prompt me to supply a URI on
  Windows PowerShell?
sort_order: 3
---

In Windows PowerShell 5.1, `curl` is an alias for PowerShell’s `Invoke-WebRequest`, not the real `curl` executable. As a result, flags like `-i` don’t behave like they do on Linux/macOS.

Fixes:
- Call the real `curl` explicitly:

```powershell
curl.exe -i http://localhost:8000/api/orders/standard-1002
```

- Or use PowerShell’s command directly:

```powershell
Invoke-WebRequest -Uri http://localhost:8000/api/orders/standard-1002
```

Note: On PowerShell 7 and later, `curl` is no longer the `Invoke-WebRequest` alias.