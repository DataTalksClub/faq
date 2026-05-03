---
id: 87fddc59b7
question: 'Setup: Failed to clone repository.'
sort_order: 7
---



Error: Failed to clone repository.

```
$ git clone git@github.com:DataTalksClub/data-engineering-zoomcamp.git /usr/src/develop/...

Cloning into '/usr/src/develop/...

Warning: Permanently added '[github.com](http://github.com/),140.82.114.4' (ECDSA) to the list of known hosts.

git@github.com: Permission denied (publickey).

fatal: Could not read from remote repository.
```

**Issue:** You don’t have permissions to write to `DataTalksClub/data-engineering-zoomcamp.git`

**Solutions:**

1. **Clone the Forked Repository**
   
   Clone the repository using your forked repo, which contains your GitHub username. Then, specify the path as:
   
   ```
   [your github username]/data-engineering-zoomcamp.git
   ```

2. **Create a Fresh Repo for dbt-lessons**
   
   Create a new repository for dbt-lessons. This approach is beneficial as it allows for branching and pull requests without affecting your other repositories. There's no need to create a subfolder for the dbt project files.

3. **Use HTTPS Link**
   
   Switch to using an HTTPS link for cloning the repository if SSH access is not configured.