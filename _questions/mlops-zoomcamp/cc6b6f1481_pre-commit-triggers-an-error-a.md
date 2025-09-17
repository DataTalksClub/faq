---
id: cc6b6f1481
question: Pre-commit triggers an error at every commit: “mapping values are not allowed in this context”
section: Module 6: Best practices
course: mlops-zoomcamp
sort_order: 2250
---

At every commit the above error is thrown and no pre-commit hooks are ran.

Make sure the indentation in .pre-commit-config.yaml is correct. Especially the 4 spaces ahead of every `repo` statement

Added by M. Ayoub C.

