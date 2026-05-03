---
id: 00e8093b90
question: Running out of storage when using Kestra with Postgres on a GCP VM
sort_order: 6
---

Backfilling can blow through a small VM's disk surprisingly fast. The default 30 GB GCP VM disk fills quickly. To find and reclaim space:

## Find what's using disk

```bash
sudo du -h --max-depth=1 / 2>/dev/null | sort -h | tail -20
```

Common culprits:

- Docker images and unused volumes (often several GB) — clean up with `docker system prune -af --volumes`.
- Old backfill artifacts in `/tmp` or your project working dir.
- Postgres data that's grown over many runs (table bloat from repeated backfills).

## Clean up Kestra's stored executions

Kestra keeps execution metadata and logs that grow over time. Use a [Purge flow](https://kestra.io/docs/administrator-guide/purge) to delete old executions. To purge immediately rather than wait for the scheduled trigger, set `endDate` to `"{{ now() }}"` and run it manually. You can choose whether to also remove FAILED-state executions.

## Clean up PostgreSQL tables

If you backfilled the same dataset multiple times into different tables, drop the ones you don't need (manually in pgAdmin, or via a Kestra flow). For tables you want to keep but compact, run `VACUUM FULL` on them.

If after all this you still don't have enough room, increase the boot disk size from the GCP console (Compute Engine → VM details → Edit → Boot disk → Resize).
