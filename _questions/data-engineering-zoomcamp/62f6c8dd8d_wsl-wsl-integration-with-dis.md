---
course: data-engineering-zoomcamp
id: 62f6c8dd8d
question: WSL - WSL integration with distro Ubuntu unexpectedly stopped with exit
  code 1.
section: 'Module 1: Docker and Terraform'
sort_order: 1030
---

![Image](images/data-engineering-zoomcamp/image_bc654841.png)

Up restarting the same issue appears. Happens out of the blue on windows.

Solution 1: Fixing DNS Issue (credit: ) this worked for me personally

reg add "HKLM\System\CurrentControlSet\Services\Dnscache" /v "Start" /t REG_DWORD /d "4" /f

Restart your computer and then enable it with the following

reg add "HKLM\System\CurrentControlSet\Services\Dnscache" /v "Start" /t REG_DWORD /d "2" /f
Restart your OS again. It should work.

Solution 2: right click on running Docker icon (next to clock) and chose "Switch to Linux containers" n

bash: conda: command not found

Database is uninitialized and superuser password is not specified.

Database is uninitialized and superuser password is not specified.

