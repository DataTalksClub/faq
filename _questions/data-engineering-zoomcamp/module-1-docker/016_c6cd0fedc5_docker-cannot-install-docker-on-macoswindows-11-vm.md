---
id: c6cd0fedc5
question: 'Docker: Cannot install docker on MacOS/Windows 11 VM running on top of
  Linux (due to Nested virtualization).'
sort_order: 16
---

Before starting your VM, you need to enable nested virtualization. Run the following commands based on your CPU:

- **For Intel CPU:**
  
  ```bash
  modprobe -r kvm_intel
  modprobe kvm_intel nested=1
  ```

- **For AMD CPU:**
  
  ```bash
  modprobe -r kvm_amd
  modprobe kvm_amd nested=1
  ```