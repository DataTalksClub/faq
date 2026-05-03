---
id: 5db9bca6a9
question: Getting SIGILL in JRE when running latest kestra image on Mac M4 MacOS 15.2/3
sort_order: 11
---

SIGILL in Java Runtime Environment on MacOS M4

Add the following environment variable to your Kestra container: `-e JAVA_OPTS="-XX:UseSVE=0"`:

```bash
docker run --rm -it \
  --pull=always \
  -p 8080:8080 \
  --user=root \
  -e JAVA_OPTS="-XX:UseSVE=0" \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp:/tmp \
  kestra/kestra:latest server local
```
The same in a Docker Compose file:

```yaml
services:
  kestra:
    image: kestra/kestra:latest
    environment:
      JAVA_OPTS: "-XX:UseSVE=0"
```