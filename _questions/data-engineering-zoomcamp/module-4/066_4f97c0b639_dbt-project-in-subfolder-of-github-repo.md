---
id: 4f97c0b639
question: Can I keep my dbt project in a subfolder of my GitHub repo (instead of
  the root)?
sort_order: 66
---

Yes. The trick is to leave `dbt_project.yml` at the root of the repo and prefix every path inside it with your subfolder.

For example, to keep all the dbt files in a `Week_4/` folder of the repo:

1. Keep `dbt_project.yml` in the root of your repo. Edit it so every path is prefixed with your subfolder:

   ```yaml
   model-paths: ["Week_4/models"]
   analysis-paths: ["Week_4/analyses"]
   test-paths: ["Week_4/tests"]
   seed-paths: ["Week_4/seeds"]
   macro-paths: ["Week_4/macros"]
   snapshot-paths: ["Week_4/snapshots"]
   target-path: "Week_4/target"
   clean-targets:
     - "Week_4/target"
     - "Week_4/dbt_packages"
   ```

2. Save `dbt_project.yml`.
3. Review your `.gitignore` for any dbt-related entries and update paths if needed.
4. Delete the duplicate dbt files/folders that dbt initially created in the root of your repo — they aren't used now that paths are pointed at the subfolder. (The `target/` folder may re-appear when you run dbt commands; that's fine.)
5. If there's an older copy of `dbt_project.yml` inside the subfolder, delete it so you don't edit the wrong one by accident.
6. Test-run dbt commands from the subfolder to confirm everything works.
