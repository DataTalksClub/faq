---
id: 92f8926c92
question: Install Kind via Go package
sort_order: 3530
---

If you are having challenges installing Kind through the Windows Powershell as provided on the website and Choco Library as I did, you can simply install Kind through Go.

> Download and Install Go ([https://go.dev/doc/install](https://go.dev/doc/install))

> Confirm installation by typing the following in Command Prompt -  go version

> Proceed by installing Kind by following this command - go install sigs.k8s.io/kind@v0.20.0

>Confirm Installation kind --version

It works perfectly.

