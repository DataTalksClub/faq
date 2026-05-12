---
id: 16481ac8f7
question: 'docker: Error response from daemon: mkdir C:\Program Files\Git\var: Access
  is denied.'
sort_order: 4
---

When running the following Docker command in Bash with Docker and WSL2 installed, you may encounter an error. Running Bash as admin will not resolve the issue:

```bash
docker run \
  --pull=always \
  --rm \
  -it \
  -p 8080:8080 \
  --user=root \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp:/tmp \
  kestra/kestra:latest server local
```

```
latest: Pulling from kestra/kestra
Digest: sha256:af02a309ccbb52c23ad1f1551a1a6db8cf0523cf7aac7c7eb878d7925bc85a62
Status: Image is up to date for kestra/kestra:latest
docker: Error response from daemon: mkdir C:\\Program Files\\Git\\var: Access is denied.
See 'docker run --help'.
```

To resolve this issue, run Command Prompt as an administrator and use the following command:

```bash
docker run \
  --pull=always \
  --rm \
  -it \
  -p 8080:8080 \
  --user=root \
  -v "/var/run/docker.sock:/var/run/docker.sock" \
  -v "C:/Temp:/tmp" \
  kestra/kestra:latest server local
```

After executing the command as described, the localhost should display the Kestra UI as expected.