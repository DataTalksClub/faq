---
id: 2490b9e786
question: Reproducibility in different OS
sort_order: 25
---

When trying to rerun the Docker file in Windows, as opposed to developing in WSL/Linux, I encountered the following error:

```bash
Warning: Python 3.11 was not found on your system…

Neither ‘pipenv’ nor ‘asdf’ could be found to install Python.

You can specify specific versions of Python with:

$ pipenv –python path\to\python
```

The solution was to add the Python 3.11 installation folder to the PATH, restart the system, and run the Docker file again. This solved the error.