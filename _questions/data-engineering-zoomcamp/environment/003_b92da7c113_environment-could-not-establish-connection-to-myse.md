---
id: b92da7c113
question: 'Environment - Could not establish connection to "MyServerName": Got bad
  result from install script'
sort_order: 3
---

This issue occurs when attempting to connect to a GCP VM using VSCode on a Windows machine. You can resolve it by changing a registry value in the registry editor.

Open the Run command window:
- Use the shortcut keys `Windows + R`, or
- Right-click "Start" and click "Run".

Open the Registry Editor:
- Type `regedit` in the Run command window, then press Enter.

Change the registry value:
- Navigate to `HKEY_CURRENT_USER\Software\Microsoft\Command Processor`.
- Change the "Autorun" value from "if exists" to a blank.

Alternatively, you can delete the saved fingerprint within the known_hosts file:

In Windows, locate the file at `C:\Users\<your_user_name>\.ssh\known_hosts` and remove the entry for the server.