---
id: '3549528659'
question: 'Docker: Docker won''t start or is stuck in settings (Windows 10 / 11)'
sort_order: 5
---

Ensure you are running the latest version of Docker for Windows. Download the updated version from [Docker's official site](https://docs.docker.com/desktop/install/windows-install/). If the upgrade option in the menu doesn't work, uninstall and reinstall with the latest version.

If Docker is stuck on starting, try switching the containers by right-clicking the [docker symbol](https://imgur.com/vsVUAzK) from the running programs, and switch the containers from Windows to Linux or vice versa.

For Windows 10 / 11 Pro Edition:

- **Hyper-V Backend:** ensure Hyper-V is enabled by following this [tutorial](https://www.c-sharpcorner.com/article/install-and-configured-docker-desktop-in-windows-10/).
- **WSL2 Backend:** follow the steps detailed in this [tutorial](https://pureinfotech.com/install-wsl-windows-11/).