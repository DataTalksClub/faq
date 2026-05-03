---
id: 49e1ec9d84
question: 'dbt: Where should we create `profiles.yml`?'
sort_order: 56
---

For local environments using dbt-core, the profile configuration is valid for all projects. Note: dbt Cloud doesn’t require it.

The `~/.dbt/profiles.yml` file should be located in your user's home directory. On Windows, this would typically be:

```
C:\Users\<YourUsername>\.dbt\profiles.yml
```

Replace `<YourUsername>` with your actual Windows username. This file is used by dbt to store connection profiles for different projects.

Here's how you can create the `profiles.yml` file in the appropriate directory:

1. Open File Explorer and navigate to `C:\Users\<YourUsername>\`.
2. Create a new folder named `.dbt` if it doesn't already exist.
3. Inside the `.dbt` folder, create a new file named `profiles.yml`.

Usage example can be found [here](https://gist.github.com/pizofreude/ff4d0601f1eb353683d8af8f4b5aac27?permalink_comment_id=5457712#gistcomment-5457712).