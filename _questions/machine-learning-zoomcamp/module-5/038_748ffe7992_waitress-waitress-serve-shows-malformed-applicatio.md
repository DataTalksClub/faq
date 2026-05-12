---
id: 748ffe7992
question: 'Waitress: waitress-serve shows Malformed application'
sort_order: 38
---

When running the command:

```bash
pipenv run waitress-serve --listen=localhost:9696 q4-predict:app
```

You may encounter the following error message:

```
There was an exception (ValueError) importing your module.

It had these arguments:

1. Malformed application 'q4-predict:app'
```


Waitress doesn’t accept a dash in the Python file name.

To resolve this, rename the file by replacing the dash with an underscore, for example, use `q4_predict.py`.