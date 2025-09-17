---
course: mlops-zoomcamp
id: 4aa018f478
question: Activating Anaconda env in .bashrc
section: 'Module 1: Introduction'
sort_order: 660
---

Problem: For me, Installing anaconda didn’t modify the .bashrc profile. That means Anaconda env was not activated even after exiting and relaunching the unix shell.

Solution:

For bash : Initiate conda again, which will add entries for anaconda in .bashrc file.

$ cd YOUR_PATH_ANACONDA/bin $ ./conda init bash

That will automatically edit your .bashrc.

Reload:

$ source ~/.bashrc

Ahamed Irshad ()

