---
id: 4076e3f3a6
question: '''kind'' is not recognized as an internal or external command, operable
  program or batch file. (In Windows)'
sort_order: 20
---

**Problem:**

I downloaded `kind` using the following command:

```bash
curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.17.0/kind-windows-amd64
```

When I try to run:

```bash
kind --version
```

I receive the error:

```plaintext
'kind' is not recognized as an internal or external command, operable program or batch file.
```

**Solution:**

1. The default name of the executable is `kind-windows-amd64.exe`. Rename this file to `kind.exe`.
2. Place `kind.exe` in a specific folder.
3. Add this folder to the `PATH` environment variable.