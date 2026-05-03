---
id: 1075e9e2b6
question: Make DLT comply with the XDG Base Dir Specification
sort_order: 8
---

You can set the environment variable in your shell init script:

For Bash or ZSH:

```bash
export DLT_DATA_DIR=$XDG_DATA_HOME/dlt
```

For Fish (in `config.fish`):

```bash
set -x DLT_DATA_DIR "$XDG_DATA_HOME/dlt"
```