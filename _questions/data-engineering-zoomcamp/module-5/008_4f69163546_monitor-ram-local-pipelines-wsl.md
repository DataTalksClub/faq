---
id: 4f69163546
question: How to monitor RAM usage when running data pipelines locally?
sort_order: 8
---

Monitoring RAM usage when running data pipelines locally is important to prevent out-of-memory failures. The following steps show how to monitor memory on Windows with WSL (Ubuntu by default):

1) Install Windows Subsystem for Linux with Ubuntu as the default distribution:

```
wsl --install
```

2) To see static memory usage (RAM) consumed up to the current time (within WSL):

```
free -h
```

3) To see memory usage in real time while a process is running (refreshes at your chosen interval):

```
watch -n 1 free -h
```

4) If you are using Windows, allocate resources to WSL by configuring the .wslconfig file in your Windows home directory (e.g., C:\\Users\\<your_user>\\.wslconfig). A simple setup:

```
[wsl2]
memory=6GB           # Memory to be allocated
processors=4         # Processors to be allocated
swap=10GB            # Disk memory used to avoid crashes (slower but safer)
```

5) Restart WSL to apply changes:

```
wsl --shutdown
```
