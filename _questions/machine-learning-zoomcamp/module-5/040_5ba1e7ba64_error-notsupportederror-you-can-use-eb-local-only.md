---
id: 5ba1e7ba64
question: 'Error: NotSupportedError - You can use "eb local" only with preconfigured,
  generic, and multicontainer Docker platforms.'
sort_order: 40
---

When executing:

```bash
eb local run  --port 9696
```

You may encounter the following error:

```
ERROR: NotSupportedError - You can use "eb local" only with preconfigured, generic and multicontainer Docker platforms.
```


There are two options to fix this issue:

1. **Re-initialize the Environment:**
   - Run the initialization command:
     ```bash
     eb init -i
     ```
   - Choose the appropriate options from the list provided (the first default option for the Docker platform should suffice).

2. **Manually Edit Configuration:**
   - Open and edit the ‘.elasticbeanstalk/config.yml’ file.
   - Change `default_platform` from `Docker` to:
     ```yaml
     default_platform: Docker running on 64bit Amazon Linux 2023
     ```
   - Note that this option might not be available in the future.

Alternative Solution:

- Re-run the init command and change the `-p` flag value:
  ```bash
  eb init -p "Docker running on 64bit Amazon Linux" <appname>
  ```
- Then re-run:
  ```bash
  eb local run --port 9696
  ```

Original solution from [Stack Overflow](https://stackoverflow.com/a/75804355/24066976)