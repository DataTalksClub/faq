---
id: 66ccbb7da0
question: How can I remove all Docker containers, images, and volumes, and builds
  from the terminal?
sort_order: 6
---

1. Delete all containers (including running ones):

```bash
docker rm -f $(docker ps -aq)
```

2. Remove all images:

```bash
docker rmi -f $(docker images -q)
```

3. Delete all volumes:

```bash
docker volume rm $(docker volume ls -q)
```