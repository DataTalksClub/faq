---
course: data-engineering-zoomcamp
id: 1075e9e2b6
question: Make DLT comply with the XDG Base Dir Specification
section: Workshop 1 - dlthub
sort_order: 4440
---

You can set the environment variable in your shell init script (for Bash or ZSH):

export DLT_DATA_DIR=$XDG_DATA_HOME/dlt

Or for Fish (in config.fish):

set -x DLT_DATA_DIR “$XDG_DATA_HOME/dlt”

