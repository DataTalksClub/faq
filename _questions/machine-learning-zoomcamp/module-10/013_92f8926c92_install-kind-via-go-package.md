---
id: 92f8926c92
question: Install Kind via Go package
sort_order: 13
---

If you are having challenges installing Kind through the Windows Powershell or Choco Library, you can install Kind through Go.

1. **Download and Install Go**: [https://go.dev/doc/install](https://go.dev/doc/install)

2. **Confirm installation**:
   ```bash
   go version
   ```
3. **Install Kind**:
   ```bash
   go install sigs.k8s.io/kind@v0.20.0
   ```
4. **Confirm Kind installation**:
   ```bash
   kind --version
   ```

It works perfectly.