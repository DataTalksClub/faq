---
id: f685b2fddc
question: 'GitHub Codespaces: what uses up memory and storage?'
sort_order: 24
---

Most of what you add across the modules barely touches your Codespace. The one exception is **data files**.

- **Terraform** doesn't consume Codespace memory or storage. It only makes API calls to provision infrastructure on GCP - the resources it creates live in the cloud, not on your machine, so you free nothing by moving it to another repo.
- **Code files** are tiny (kilobytes), so accumulating notebooks and scripts across modules is a non-issue. You don't need a separate repo per module - keep everything in one repo.
- **Data files** (CSV, Parquet, JSON) are what actually take up space. Keep them out of git with `.gitignore` (see *How do I use Git/GitHub for this course?*).
- **Running Docker containers** do use Codespace RAM while they're up, so stop the containers you've finished with for a module rather than leaving them idling.
