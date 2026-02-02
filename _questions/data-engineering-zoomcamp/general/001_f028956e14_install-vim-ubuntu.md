---
id: f028956e14
question: How do I install vim (Vi Improved) on an Ubuntu Linux machine?
sort_order: 1
---

Install vim on Ubuntu using the following steps:

- Update your package list:
  ```bash
  sudo apt-get update
  ```

- Install vim:
  ```bash
  sudo apt-get install vim
  ```

- Verify the installation by checking the version:
  ```bash
  vim --version
  ```

Alternatively, you can run both commands in one line:
  ```bash
  sudo apt-get update && sudo apt-get install vim -y
  ```

Note: The -y flag automatically answers 'yes' to prompts during installation.