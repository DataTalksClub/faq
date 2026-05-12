---
id: b062fc29e5
question: 'TypeError: __init__() got an unexpected keyword argument ''unbound_message'' while importing Flask'
sort_order: 24
---


In video 10.3, while testing a Flask service, the following error occurred:

```
TypeError: __init__() got an unexpected keyword argument 'unbound_message'
```

This error was encountered when running `docker run ...` in one terminal and then executing `python gateway.py` in another terminal.



This issue is related to the versions of Flask and Werkzeug.

To debug the issue:

1. Run `pip freeze > requirements.txt` to check the installed versions of Flask and Werkzeug.
   - Example output:
     ```
     Flask==2.2.2
     Werkzeug==2.2.2
     ```
2. The error occurs when using an old version of Werkzeug (2.2.2) with a new version of Flask (2.2.2).
3. To resolve, pin the version of Flask to an older version:
   
   ```bash
   pipenv install Flask==2.1.3
   ```

This should resolve the compatibility issue.