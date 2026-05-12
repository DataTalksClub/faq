---
id: cb7c81f796
question: 'Docker: Temporary failure in name resolution'
sort_order: 26
---


Add the following lines to your Docker daemon configuration file using `vim /etc/docker/daemon.json`:

```json
{
    "dns": ["8.8.8.8", "8.8.4.4"]
}
```

Then, restart Docker using the command:

```bash
sudo service docker restart
```