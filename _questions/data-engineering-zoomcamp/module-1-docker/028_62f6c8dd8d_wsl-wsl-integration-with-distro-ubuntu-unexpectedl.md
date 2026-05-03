---
id: 62f6c8dd8d
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_bc654841.png
question: 'WSL: WSL integration with Ubuntu unexpectedly stopped with exit code 1'
sort_order: 28
---

<{IMAGE:image_1}>

If WSL integration keeps stopping with exit code 1, try these in order.

## Toggle the DNS cache service

This [Reddit fix](https://www.reddit.com/r/docker/comments/p98xq6/docker_failed_to_start_exit_code_1/) works for some users:

```bash
reg add "HKLM\System\CurrentControlSet\Services\Dnscache" /v "Start" /t REG_DWORD /d "4" /f
```

Restart Windows, then re-enable it:

```bash
reg add "HKLM\System\CurrentControlSet\Services\Dnscache" /v "Start" /t REG_DWORD /d "2" /f
```

Restart Windows again.

## Switch Docker Desktop to Linux containers

Right-click the Docker tray icon and choose "Switch to Linux containers" if it isn't already.
