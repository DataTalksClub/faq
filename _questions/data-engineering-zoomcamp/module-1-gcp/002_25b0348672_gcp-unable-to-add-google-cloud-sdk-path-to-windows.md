---
id: 25b0348672
question: 'GCP: "The installer is unable to automatically update your system PATH"
  on Windows'
sort_order: 2
---

The Google Cloud SDK Windows installer occasionally fails to update `PATH` automatically:

```
The installer is unable to automatically update your system PATH. Please add C:\tools\google-cloud-sdk\bin
```

Add the SDK's `bin/` directory to `PATH` manually:

1. Right-click "This PC" → Properties → Advanced system settings → Environment Variables.
2. Under "User variables" (or "System variables"), select `Path` → Edit → New.
3. Paste the directory the installer mentioned, e.g. `C:\tools\google-cloud-sdk\bin`.
4. Click OK in all dialogs.
5. Open a new terminal (existing ones won't pick up the change) and verify:

   ```bash
   gcloud --version
   ```

## Tips for a smoother Windows shell setup

The course's command-line examples assume a Unix-like shell. On Windows the easiest options are:

- WSL2 (recommended). Install via `wsl --install`, then run all course commands inside the WSL distro.
- Git Bash. During the Git for Windows installer, check "Add Git Bash to Windows Terminal" and "Use Git and optional Unix tools from the command prompt". Then make Git Bash the default profile in Windows Terminal (Settings → Default profile).

Either way, restart your terminal after editing `PATH` so the new value is picked up.
