---
id: 542abbcb6a
question: 'wget - ERROR: cannot verify <website> certificate  (MacOS)'
sort_order: 6
---

Firstly, make sure that you add `!` before `wget` if you’re running your command in a Jupyter Notebook or CLI. Then, you can check one of these two things (from CLI):

- **Using the Python library wget installed with pip:**

  ```bash
  python -m wget <url>
  ```

- **Use the usual command and add `--no-check-certificate` at the end:**

  ```bash
  !wget <website_url> --no-check-certificate
  ```