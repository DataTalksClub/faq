---
course: data-engineering-zoomcamp
id: f291e8d311
question: 'Postgres - bind: address already in use'
section: 'Module 1: Docker and Terraform'
sort_order: 1170
---

1.2.2 Postgres commandline for docker

Various errors when first pasting docker run command - make sure there is only 1 space before “\” and only a newline after “\”

Error - posgres post is already in use. This seems to happen every time i try to start the docker postgres container.

Option 1: Figure out what service is using the port (sudo lsof -i :5432) and stop that service:  sudo service postgresql stop.

Option 2: more long term.

I actually eventually ended up mapping to a different port, because this happened every time I restarted my VM. So I would map <local 5433: container 5432> in the docker file or docker compose file. Since i am using a VM, I also need to make sure that port 5433 is forwarded.

