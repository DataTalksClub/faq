---
id: 3d51ece7b9
question: 'dbt CI: setting up Continuous Integration with GitHub'
sort_order: 25
---

To enable CI jobs (running dbt on pull requests), dbt Cloud needs a native integration with GitHub, GitLab, or Azure DevOps — the generic "Git Clone" / SSH connection method does not unlock the "Run on Pull Requests" trigger and you'll see:

```
Triggered by pull requests
This feature is only available for dbt repositories connected through dbt Cloud's native integration with Github, Gitlab, or Azure DevOps
```

The dbt Cloud Developer plan also doesn't support CI jobs — you need Team or Enterprise. (See the [dbt Cloud CI prerequisites](https://docs.getdbt.com/docs/deploy/ci-jobs#prerequisites).)

## Switch from Git Clone to native GitHub integration

1. Connect your GitHub account in dbt Cloud: Profile Settings → Linked Accounts → connect GitHub and grant the requested permissions. ([dbt docs](https://docs.getdbt.com/docs/collaborate/git/connect-github))

2. Disconnect the existing Git Clone connection: Account Settings → Projects → your project → Repository → Disconnect.

3. Reconfigure with the GitHub option, selecting the repository.

4. (If your dbt project lives in a subfolder of the repo) set Project Subdirectory in the project settings to point to that folder.

5. In Deploy → Job → Configuration → Triggers, you should now see "Run on Pull Requests" as an available toggle.

## CI job runs but says "valid dbt project was not found"

Usually one of:

- Project is in a subfolder, but Project Subdirectory isn't set.
- The CI environment is configured to run on a custom branch that doesn't exist.
- Uncommitted/unpushed changes.

In Deploy → Environments → your environment → Settings, set "Custom branch" if you're not on the default branch, and confirm it matches a real branch in GitHub.
