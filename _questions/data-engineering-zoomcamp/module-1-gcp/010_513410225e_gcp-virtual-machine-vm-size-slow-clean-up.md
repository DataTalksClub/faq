---
id: 513410225e
question: 'GCP: Virtual Machine (VM) Size, Slow, Clean Up'
sort_order: 10
---

If you are progressing through the course and find that your VM is starting to become slow, you can run the following commands to inspect and detect areas where you can improve:

**Recommended VM Size**

- Start with a 60GB machine. A 30GB machine may not be sufficient, as you might need to restart the project with a larger size.

**Commands to Inspect the Health of Your VM**

- **System Resource Usage**
  
  ```bash
  top
  htop
  ```
  Shows real-time information about system resource usage, including CPU, memory, and processes.

  ```bash
  free -h
  ```
  Displays information about system memory usage and availability.

  ```bash
  df -h
  ```
  Shows disk space usage of file systems.

  ```bash
  du -h <directory>
  ```
  Displays disk usage of a specific directory.

- **Running Processes**
  
  ```bash
  ps aux
  ```
  Lists all running processes along with detailed information.

- **Network**
  
  ```bash
  ifconfig
  ip addr show
  ```
  Shows network interface configuration.

  ```bash
  netstat -tuln
  ```
  Displays active network connections and listening ports.

- **Hardware Information**
  
  ```bash
  lscpu
  ```
  Displays CPU information.

  ```bash
  lsblk
  ```
  Lists block devices (disks and partitions).

  ```bash
  lshw
  ```
  Lists hardware configuration.

- **User and Permissions**
  
  ```bash
  who
  ```
  Shows who is logged on and their activities.

  ```bash
  w
  ```
  Displays information about currently logged-in users and their processes.

- **Package Management**
  
  ```bash
  apt list --installed
  ```
  Lists installed packages (for Ubuntu and Debian-based systems).
