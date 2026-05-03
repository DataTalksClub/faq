---
id: 8b082e74c0
question: 'Error: error starting userland proxy: listen tcp4 0.0.0.0:8080: bind: address
  already in use'
sort_order: 31
---

Resolution: You need to stop the service using the port.

Run the following:

```bash
sudo kill -9 `sudo lsof -t -i:<port>`
```

Replace `<port>` with `8080` in this case. This will free up the port for use.