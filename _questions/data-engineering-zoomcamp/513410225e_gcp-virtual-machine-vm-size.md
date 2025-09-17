---
id: 513410225e
question: GCP Virtual Machine (VM) Size, Slow, Clean Up
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1500
---

If you are progressing through the course and find that your VM is starting to become slow you can run the following commands to inspect and detect areas where you can improve this.

NB: What size VM should I start with? I started with 30GB but this wasn’t enough, I had to restart the project with a 60GB machine so I’d recommend choosing the 60GB version.

Commands to inspect the health of your VM:

System Resource Usage:

top or htop: Shows real-time information about system resource usage, including CPU, memory, and processes.

free -h: Displays information about system memory usage and availability.

df -h: Shows disk space usage of file systems.

du -h <directory>: Displays disk usage of a specific directory.

Running Processes:

ps aux: Lists all running processes along with detailed information.

Network:

ifconfig or ip addr show: Shows network interface configuration.

netstat -tuln: Displays active network connections and listening ports.

Hardware Information:

lscpu: Displays CPU information.

lsblk: Lists block devices (disks and partitions).

lshw: Lists hardware configuration.

User and Permissions:

who: Shows who is logged on and their activities.

w: Displays information about currently logged-in users and their processes.

Package Management:

apt list --installed: Lists installed packages (for Ubuntu and Debian-based systems)

