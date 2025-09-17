---
id: 1bc7beaf5d
question: Install docker in WSL2 without installing Docker Desktop
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 710
---

If you don’t want to install docker desktop and run docker in WSL2 on Windows you can try the following:

Install docker and docker compose and give the user the right privileges (you do not need

# Install Docker, you can ignore the warnings

curl -fsSL -o get-docker.sh

sudo sh get-docker.sh

# Add your user to the Docker group

sudo usermod -aG docker $USER

Then you need to start the service:

sudo systemctl enable docker.service

Then you can test both are installed:

# Sanity check that both tools were installed successfully

docker --version

docker compose version

docker run hello-world

if after restarting WSL the service is not started automatically, you will need to change your .profile o .zprofile file and include something like this:

if grep -q "microsoft" /proc/version > /dev/null 2>&1; then

if service docker status 2>&1 | grep -q "is not running"; then

wsl.exe --distribution "${WSL_DISTRO_NAME}" --user root \

--exec /usr/sbin/service docker start > /dev/null 2>&1

fi

fi

Added by Eduardo Munoz

