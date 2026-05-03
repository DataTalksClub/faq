---
id: bceb4aa421
question: 'Docker: docker pull dbpage'
sort_order: 3
---

Whenever a `docker pull` is performed (either manually or by `docker-compose up`), it attempts to fetch the given image name from a repository. If the repository is public, the fetch and download occur without any issues.

For instance:

```bash
docker pull postgres:13
docker pull dpage/pgadmin4
```

**Be Advised:** The Docker images we'll be using throughout the Data Engineering Zoomcamp are all public, unless otherwise specified. This means you are not required to perform a `docker login` to fetch them.

If you encounter the message:

```
docker login': denied: requested access to the resource is denied.
```

This is likely due to a typo in your image name. For instance:

```bash
$ docker pull dbpage/pgadmin4
```

This command will throw an exception:

```
Error response from daemon: pull access denied for dbpage/pgadmin4, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
```

This occurs because the actual image name is `dpage/pgadmin4`, not `dbpage/pgadmin4`.

**How to fix it:**

```bash
$ docker pull dpage/pgadmin4
```

**Extra Notes:** In some professional environments, the Docker image may be in a private repository that your DockerHub username has access to. In this case, you must:

1. Execute:
   ```bash
   $ docker login
   ```
2. Enter your username and password.
3. Then perform the `docker pull` against that private repository.