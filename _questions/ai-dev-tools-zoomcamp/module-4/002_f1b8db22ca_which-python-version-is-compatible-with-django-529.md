---
id: f1b8db22ca
question: 'Which Python version is compatible with Django 5.2.9?'
sort_order: 2
---

Django 5.2.9 needs Python 3.10 or above; on older versions (3.9 or less) the server won't start.

Check your system Python version (macOS):
```
/usr/bin/python3 --version 2>&1
```
To fix it, create and use a virtual environment with Python 3.10+:
```
/usr/local/bin/python3.10 -m venv .venv --clear
source .venv/bin/activate
```
Then restart the Django server.
