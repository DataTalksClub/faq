---
course: data-engineering-zoomcamp
id: d02af042b1
question: '''pip'' is not recognized as an internal or external command, operable
  program or batch file.'
section: 'Module 1: Docker and Terraform'
sort_order: 1760
---

If you use Anaconda (recommended for the course), it comes with pip, so the issues is probably that the anaconda’s Python is not on the PATH.

Adding it to the PATH is different for each operation system.

For Linux and MacOS:

Open a terminal.

Find the path to your Anaconda installation. This is typically `~/anaconda3` or `~/opt/anaconda3`.

Add Anaconda to your PATH with the command: `export PATH="/path/to/anaconda3/bin:$PATH"`.

To make this change permanent, add the command to your `.bashrc` (Linux) or `.bash_profile` (MacOS) file.

On Windows, python and pip are in different locations (python is in the anaconda root, and pip is in Scripts). With GitBash:

Locate your Anaconda installation. The default path is usually `C:\Users\[YourUsername]\Anaconda3`.

Determine the correct path format for Git Bash. Paths in Git Bash follow the Unix-style, so convert the Windows path to a Unix-style path. For example, `C:\Users\[YourUsername]\Anaconda3` becomes `/c/Users/[YourUsername]/Anaconda3`.

Add Anaconda to your PATH with the command: `export PATH="/c/Users/[YourUsername]/Anaconda3/:/c/Users/[YourUsername]/Anaconda3/Scripts/$PATH"`.

To make this change permanent, add the command to your `.bashrc` file in your home directory.

Refresh your environment with the command: `source ~/.bashrc`.

For Windows (without Git Bash):

Right-click on 'This PC' or 'My Computer' and select 'Properties'.

Click on 'Advanced system settings'.

In the System Properties window, click on 'Environment Variables'.

In the Environment Variables window, select the 'Path' variable in the 'System variables' section and click 'Edit'.

In the Edit Environment Variable window, click 'New' and add the path to your Anaconda installation (typically `C:\Users\[YourUsername]\Anaconda3` and C:\Users\[YourUsername]\Anaconda3\Scripts`).

Click 'OK' in all windows to apply the changes.

After adding Anaconda to the PATH, you should be able to use `pip` from the command line. Remember to restart your terminal (or command prompt in Windows) to apply these changes.

