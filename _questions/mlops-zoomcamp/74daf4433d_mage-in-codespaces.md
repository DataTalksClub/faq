---
id: 74daf4433d
question: Mage in Codespaces
section: Module 3: Orchestration
course: mlops-zoomcamp
sort_order: 1330
---

The below errors seem to occur only when using mage in Codespaces.

Errors (1)

Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

Errors (2)

Error response from daemon: invalid volume specification: '/workspaces/mage-mlops:/:rw': invalid mount config for type "bind": invalid specification: destination can't be '/'

Solution for (1) & (2): stay tuned…still testing

docker info and docker –version runs fine. 
But when I do docker compose down, stop codespaces, and reconnect, the errors went away. Not sure if it is reproducible for everyone, though.

Errors (3)

warning: unable to access '/home/codespace/.gitconfig': Is a directory

Solution (3) via Office Hours:

this is targeted for 3.5.x Deploying with Mage

If not deploying,

Comment line#20 in docker-compose.yml

place a dummy empty file named .gitconfig in your repo’s root folder and copy it in the Dockerfile with this line, place it below line#9

COPY .gitconfig /root/.gitconfig

The reason this happens is that when the file is missing, Docker auto-creates it as a Directory instead of a file. So creating a dummy file prevents this

