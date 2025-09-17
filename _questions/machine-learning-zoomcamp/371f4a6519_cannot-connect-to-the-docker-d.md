---
course: machine-learning-zoomcamp
id: 371f4a6519
question: Cannot connect to the docker daemon. Is the Docker daemon running?
section: 5. Deploying Machine Learning Models
sort_order: 1830
---

Ensure Docker Daemon Is Running

On Windows:

Open Docker Desktop (admin rights may be required).

Check if it’s running, and restart Docker Desktop if necessary.

On Linux:

Run sudo systemctl start docker to start the Docker daemon.

Verify it’s running with sudo systemctl status docker.

Verify Docker Group Membership (Linux Only)

Check if your user is in the Docker group:

groups $USER

If "docker" isn’t listed, add yourself with:

sudo usermod -aG docker $USER

Log out and back in to apply changes.

Restart the Docker Service (Linux)

sudo systemctl restart docker

Check Docker Socket Permissions (Linux)

Run the following command to confirm Docker socket permissions:

sudo chmod 666 /var/run/docker.sock

Try Running Docker with sudo (Linux)

Run sudo docker ps to check if permissions are causing the issue.

Test Docker Setup

Run a test Docker command to verify connection:

docker run hello-world

Working on getting Docker installed - when I try running hello-world I am getting the error.

Docker: Cannot connect to the docker daemon at unix:///var/run/docker.sock. Is the Docker daemon running ?

Solution description

If you’re getting this error on WSL, re-install your docker: remove the docker installation from WSL and install Docker Desktop on your host machine (Windows).

On Linux, start the docker daemon with either of these commands:

sudo dockerd

sudo service docker start

Added by

