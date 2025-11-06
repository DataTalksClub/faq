---
id: 69e5f9cbf8
question: How to run a FastAPI app for serving a Python pickle-based model and resolve
  common startup errors (uvicorn/fastapi) when deploying on a local port?
sort_order: 63
---

The error described is typically due to using an incorrect command to start the FastAPI server. Use uvicorn to run the FastAPI app and specify the module and app object correctly. If your script is named `your_script_fastapi_app.py` and defines a FastAPI instance `app`, start the server with:

```bash
uvicorn your_script_fastapi_app:app --host 0.0.0.0 --port 9696 --reload
```

Notes:
- Ensure the script defines the app: `from fastapi import FastAPI; app = FastAPI()`.
- The syntax `uvicorn module:app` is required
- If you still get errors, verify the module imports succeed (no syntax/runtime errors) and that the port is not already in use.
- You can test the API by curling `http://localhost:9696/` or hitting your defined endpoints.
