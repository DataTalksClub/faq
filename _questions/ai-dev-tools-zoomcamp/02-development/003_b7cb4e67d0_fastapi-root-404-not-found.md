---
id: b7cb4e67d0
question: 'Why does `http://localhost:8000` return `{ "detail": "Not Found" }` after
  starting my FastAPI backend?'
sort_order: 3
---

When you start a FastAPI server, FastAPI will only respond to routes you explicitly define. The `{"detail":"Not Found"}` response means your app has no endpoint registered for the root path (`/`), so FastAPI returns a `404`.

To confirm the server is up, use the built-in docs or an existing endpoint:
- `http://localhost:8000/docs`
- `http://localhost:8000/<your_defined_route>`

If you want `http://localhost:8000/` to return something, add a root route:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "API is running"}
```

Common cause: you’re hitting `/` but your main routes are under a prefix (e.g. `/v1/...`), or you haven’t added any `@app.get("/")` handler yet.