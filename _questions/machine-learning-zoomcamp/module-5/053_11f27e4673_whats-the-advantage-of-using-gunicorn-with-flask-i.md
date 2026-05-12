---
id: 11f27e4673
question: What's the advantage of using Gunicorn with Flask in Docker?
sort_order: 53
---

Gunicorn is a Python WSGI HTTP server that is more suitable for production than the default Flask development server:

- **Performance**: Better at handling multiple simultaneous requests.
- **Stability**: More robust and can manage worker processes.

**Usage**:

Modify the CMD in your Dockerfile:

```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:9696", "app:app"]
```