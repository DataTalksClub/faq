---
id: cdbabdd71a
question: 'GCP VM: SSH suddenly stopped working after a restart'
sort_order: 22
---

A common cause is the VM running out of disk space, often from accumulated logs, Docker images/volumes, or pipeline artifacts. When the disk fills up, sshd may fail to write its session files and refuse new connections.

To diagnose and recover:

1. Open a serial console for the VM from the GCP console (Compute Engine → VM details → "Connect to serial console").
2. Check disk usage:
   ```bash
   df -h
   du -sh ~/* /var/log/* 2>/dev/null | sort -h
   ```
3. Free up space by clearing unused Docker resources and old logs:
   ```bash
   docker system prune -af --volumes
   sudo journalctl --vacuum-time=7d
   ```
4. If your pipeline tool keeps a local storage/log folder (e.g. dlt's `~/.dlt`, dbt's `target/`, Kestra's mounted volumes), prune the oldest content there too.

Once disk space is freed, restart sshd or reboot the VM and SSH access should work again.
