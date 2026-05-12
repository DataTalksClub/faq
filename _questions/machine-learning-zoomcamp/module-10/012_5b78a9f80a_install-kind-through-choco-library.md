---
id: 5b78a9f80a
question: Install kind through choco library
sort_order: 12
---

First, launch a PowerShell terminal with administrator privileges.

To install the choco library, use the following command in PowerShell:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```