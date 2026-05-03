---
id: dcb8885c9b
question: 'VMs: What do I do if my VM runs out of space?'
sort_order: 13
---

- Delete intermediate data you saved on the VM during ETLs (raw extracts, parquet outputs you've already pushed elsewhere, downloaded archives).
- Kill processes still holding deleted files (their disk space isn't reclaimed until the process exits — `lsof | grep deleted` shows them).
- Install `ncdu` (`sudo apt install ncdu`) and use it to walk the filesystem visually:
  ```bash
  sudo ncdu /
  ```
- Common culprits: Docker images and volumes (`docker system prune -af --volumes`), pipeline working/cache directories, and old logs (`sudo journalctl --vacuum-time=7d`).
- If a pipeline tool's cache keeps regrowing (e.g. orchestrator working dir, dbt `target/`, dlt staging), consider disabling caching or pruning it on a schedule rather than only when the disk fills.
