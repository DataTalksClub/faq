---
id: a8563f2c5c
question: Port-Forwarding with SSH
sort_order: 11
---

If you prefer using the terminal for port forwarding, configure it in your SSH config file.

1. Open your SSH config file:
   ```bash
   nano ~/.ssh/config
   ```

2. Add the following line to forward your Jupyter server:
   ```
   LocalForward 8888 localhost:8888
   ```