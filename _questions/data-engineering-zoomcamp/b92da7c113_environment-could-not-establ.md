---
id: b92da7c113
question: Environment - Could not establish connection to "MyServerName": Got bad result from install script
section: Course Management Platform for Homeworks, Project and Certificate
course: data-engineering-zoomcamp
sort_order: 270
---

This happens when attempting to connect to a GCP VM using VSCode on a Windows machine. Changing registry value in registry editor

1. To open Run command window, you can either:

(1-1) Use the shortcut keys: 'Windows + R', or

(1-2) Right Click "Start", and click "Run" to open.

2. Registry Values Located in Registry Editor, to open it: Type 'regedit' in the Run command window, and then press Enter.' 3. Now you can change the registry values "Autorun" in "HKEY_CURRENT_USER\Software\Microsoft\Command Processor" from "if exists" to a blank.

Alternatively, You can simplify the solution by deleting the fingerprint saved within the known_hosts file. In Windows, this file is placed at  C:\Users\<your_user_name>\.ssh\known_host

