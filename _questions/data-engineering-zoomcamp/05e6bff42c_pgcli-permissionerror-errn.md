---
id: 05e6bff42c
question: PGCLI - PermissionError: [Errno 13] Permission denied: '/some/path/.config/pgcli'
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1090
---

I get this error

pgcli -h localhost -p 5432 -U root -d ny_taxi

Traceback (most recent call last):

File "/opt/anaconda3/bin/pgcli", line 8, in <module>

sys.exit(cli())

File "/opt/anaconda3/lib/python3.9/site-packages/click/core.py", line 1128, in __call__

return self.main(*args, **kwargs)

File "/opt/anaconda3/lib/python3.9/sitYe-packages/click/core.py", line

1053, in main

rv = self.invoke(ctx)

File "/opt/anaconda3/lib/python3.9/site-packages/click/core.py", line 1395, in invoke

return ctx.invoke(self.callback, **ctx.params)

File "/opt/anaconda3/lib/python3.9/site-packages/click/core.py", line 754, in invoke

return __callback(*args, **kwargs)

File "/opt/anaconda3/lib/python3.9/site-packages/pgcli/main.py", line 880, in cli

os.makedirs(config_dir)

File "/opt/anaconda3/lib/python3.9/os.py", line 225, in makedirspython

mkdir(name, mode)PermissionError: [Errno 13] Permission denied: '/Users/vray/.config/pgcli'

Solution 1:

This error indicates that your user doesn’t have the necessary permissions to access or modify the specified directory or file (/some/path/.config/pgcli).

This can happen in the context of Docker when privileges were assigned to root and not to the user you have.

For example, if a process inside the container creates the file as root, your user might not have write permissions to that file on the host.

To resolve this:

Check file permissions on the directory /some/path/.config/pgcli and ensure that your user has read/write access. You can do this with the command:

ls -l /some/path/.config/pgcli

Change ownership/permissions of the file or directory so that your user has the necessary permissions. For example, to grant your user read/write permissions, use:

sudo chown -R user_name /Users/user_name/.config

The sudo stands for Super User DO

The chown means change owner

-R is doing so recursively

User_name is the name you gave to your PC (e.g. vray)

Solution 2:

Make sure you install pgcli without sudo.

The recommended approach is to use conda/anaconda to make sure your system python is not affected.

If conda install gets stuck at "Solving environment" try these alternatives:

