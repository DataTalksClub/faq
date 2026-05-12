---
id: 16af61862a
question: wget hangs on MacOS Ventura M1
sort_order: 17
---

Executing the following command hangs on MacOS Ventura M1:

```bash
wget https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv
```

If you encounter this and see IPv6 addresses in the terminal, follow these steps:

1. Go to **System Settings**.
2. Select **Network**.
3. Choose your network connection and click **Details**.
4. Set **Configure IPv6** to **Manually**.
5. Click **OK**.
6. Try the command again.