---
id: 32a878b1d5
question: 'Errors when I start the server in dbt cloud: Failed to start server. Permission
  denied (publickey)'
sort_order: 8
---

```
Failed to start server. Permission denied (publickey). fatal: Could not read from remote repository. Please make sure you have the correct access rights and the repository exists.
```

Use the deploy keys in dbt repo details to create a public key in your repo, the issue will be solved.

Steps in detail:

1. **Find dbt Cloud’s SSH Key**
   - In dbt Cloud, go to **Settings > Account Settings > SSH Keys**
   - Copy the public SSH key displayed there.

2. **Add It to GitHub**
   - Go to **GitHub > Settings > SSH and GPG Keys**
   - Click "New SSH Key", name it "dbt Cloud", and paste the key.
   - Click "Add SSH Key".

3. **Try Restarting dbt Cloud**