---
id: 2d8973e9a3
question: Why does my Flask app return “Method Not Allowed” (405) after I submit a
  form and refresh the page?
sort_order: 79
---

When you submit an HTML form, the browser sends a `POST` request. If your Flask route is declared with `methods=['POST']` only, then a refresh (or opening the URL directly) triggers a `GET` request, and Flask returns `405 Method Not Allowed`.

Fix: update the route to accept both methods and redirect visitors back to the form on `GET`.

Common mistake: if you use `redirect(url_for(...))` but forget to import `redirect` and `url_for`, you’ll get a different error (often `500 Internal Server Error` / `NameError`).

Example pattern:

```python
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "form page"

@app.route("/predict-form", methods=["GET", "POST"])
def predict_form():
    if request.method == "GET":
        return redirect(url_for("home"))
    return "result"
```

Your API client (e.g., Postman) may still work because it sends `POST`, but browsers use `GET` on refresh unless the route allows it.