---
id: 160cd7cf05
question: No Space Left on Device - OSError[Errno 28]
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 960
---

You do not have enough disk space to install the requirements. You can either increase the base EBS volume by following  or add an external disk to your instance and configure conda installation to happen on the external disk.

Abinaya Mahendiran

On GCP: I added another disk to my vm and followed  to mount the disk. Confirm the mount by running df -H (disk free) command in bash shell. I also deleted Anaconda and instead used miniconda. I downloaded miniconda in the additional disk that I mounted and when installing miniconda, enter the path to the extra disk instead of the default disk, this way conda is installed on the extra disk.

Yang Cao

