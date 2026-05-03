---
id: 5b54567e89
question: Opening an HTML file with a Windows browser from Linux running on WSL
sort_order: 9
---

If you’re running Linux on Windows Subsystem for Linux (WSL) 2, you can open HTML files from the guest (Linux) with any Internet Browser installed on the host (Windows). Just install [wslu](https://wslutiliti.es/wslu/install.html) and open the page using `wslview`:

```bash
wslview index.html
```

You can customize which browser to use by setting the `BROWSER` environment variable first. For example:

```bash
export BROWSER='/mnt/c/Program Files/Firefox/firefox.exe'
```