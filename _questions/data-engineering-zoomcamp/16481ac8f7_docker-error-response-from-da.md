---
course: data-engineering-zoomcamp
id: 16481ac8f7
question: 'docker: Error response from daemon: mkdir C:\Program Files\Git\var: Access
  is denied.'
section: 'Module 2: Workflow Orchestration'
sort_order: 1830
---

Description:

Running the command below in Bash with Docker running and WSL2 installed. Even running Bash as admin won’t work

```:

$ docker run --pull=always --rm -it -p 8080:8080 --user=root -v

/var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp kestra/kestra:latest server local

latest: Pulling from kestra/kestra

Digest: sha256:af02a309ccbb52c23ad1f1551a1a6db8cf0523cf7aac7c7eb878d7925bc85a62

Status: Image is up to date for kestra/kestra:latest

docker: Error response from daemon: mkdir C:\\Program Files\\Git\\var: Access is denied.

See 'docker run --help'.

```

The error mentioned above will appear and localhost wont shows the Kestra UI, the solution is to run Command Prompt as admin with the following command:

```

docker run --pull=always --rm -it -p 8080:8080 --user=root ^

-v "/var/run/docker.sock:/var/run/docker.sock" ^

-v "C:/Temp:/tmp" kestra/kestra:latest server local

```

This works flawlessly and localhost shows Kestra UI as usual.

