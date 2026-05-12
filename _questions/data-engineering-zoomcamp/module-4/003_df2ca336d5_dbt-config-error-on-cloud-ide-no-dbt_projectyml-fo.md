---
id: df2ca336d5
question: 'DBT-Config ERROR on CLOUD IDE: No dbt_project.yml found at expected path'
sort_order: 3
---

```
No dbt_project.yml found at expected path /usr/src/develop/user-70471823426120/environment-70471823422561/repository-70471823410839/dbt_project.yml
```

1. **Verify Packages**:
   - Confirm that every entry in `packages.yml` (and their transitive dependencies) includes a `dbt_project.yml` file.

2. **Initialize Project**:
   - Use the UI to initialize a new project.

3. **Import Git Repo**:
   - For importing a Git repository of an existing dbt project, follow the instructions available at:
   
     [Import a project by Git URL](https://docs.getdbt.com/docs/cloud/git/import-a-project-by-git-url)