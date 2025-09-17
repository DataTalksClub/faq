---
course: data-engineering-zoomcamp
id: 25b0348672
question: GCP - Unable to add Google Cloud SDK PATH to Windows
section: 'Module 1: Docker and Terraform'
sort_order: 1420
---

Unable to add Google Cloud SDK PATH to Windows

Windows error: The installer is unable to automatically update your system PATH. Please add  C:\tools\google-cloud-sdk\bin

if you are constantly getting this feedback. Might be that you needed to add Gitbash to your Windows path:

One way of doing that is to use conda: ‘If you are not already using it

Download the Anaconda Navigator

Make sure to check the box (add conda to the path when installing navigator: although not recommended do it anyway)

You might also need to install git bash if you are not already using it(or you might need to uninstall it to reinstall it properly)

Make sure to check the following boxes while you install Gitbash

Add a GitBash to Windows Terminal

Use Git and optional Unix tools from the command prompt

Now open up git bash and type conda init bash This should modify your bash profile

Additionally, you might want to use Gitbash as your default terminal.

Open your Windows terminal and go to settings, on the default profile change Windows power shell to git bash

