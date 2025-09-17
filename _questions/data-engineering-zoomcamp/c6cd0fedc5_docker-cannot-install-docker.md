---
id: c6cd0fedc5
question: Docker - Cannot install docker on MacOS/Windows 11 VM running on top of Linux (due to Nested virtualization).
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 790
---

terraformRun this command before starting your VM:

On Intel CPU:

modprobe -r kvm_intel

modprobe kvm_intel nested=1

On AMD CPU:

modprobe -r kvm_amd

modprobe kvm_amd nested=1

