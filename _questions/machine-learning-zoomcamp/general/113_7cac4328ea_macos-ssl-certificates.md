---
id: 7cac4328ea
question: 'MacOS: SSL certificate verification failed when reading a CSV from a URL
  in Python'
sort_order: 113
---

On MacOS, Python may fail to verify SSL certificates when fetching a URL due to missing CA certificates in the Python SSL store. The fix is to run the certificates installer that ships with the Python installation:

```bash
/Applications/Python\ 3*/Install\ Certificates.command
```

After this completes, try running your Python script again to read the CSV from the URL.
