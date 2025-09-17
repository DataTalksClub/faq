---
id: 8b082e74c0
question: Error: error starting userland proxy: listen tcp4 0.0.0.0:8080: bind: address already in use
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1770
---

Resolution: You need to stop the services which is using the port.

Run the following:

```

sudo kill -9 `sudo lsof -t -i:<port>`

```

<port> being 8080 in this case. This will free up the port for use.

~ Abhijit Chakraborty

Error: error response from daemon: cannot stop container: 1afaf8f7d52277318b71eef8f7a7f238c777045e769dd832426219d6c4b8dfb4: permission denied

Resolution: In my case, I had to stop docker and restart the service to get it running properly

Use the following command:

```

sudo systemctl restart docker.socket docker.service

```

~ Abhijit Chakraborty

Error: docker build Error checking context: 'can't stat '<path-to-file>'

Resolution: This happens due to insufficient permission for docker to access a certain file within the directory which hosts the Dockerfile.

1. You can create a .dockerignore file and add the directory/file which you want Dockerfile to ignore while build.

2. If the above does not work, then put the dockerfile and corresponding script, `	1.py` in our case to a subfolder. and run `docker build ...`

from inside the new folder.

~ Abhijit Chakraborty

Docker-Compose - it is illegal to have any blank spaces between the environment argument in docker-compose.yml

The following ways of configuring it will not work:

- PGADMIN_DEFAULT_EMAIL = 
- PGADMIN_DEFAULT_PASSWORD = root

- PGADMIN_DEFAULT_EMAIL=
- PGADMIN_DEFAULT_PASSWORD=root

