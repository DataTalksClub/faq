---
id: 9e5f381432
question: 'AWS Elastic Beanstalk: I can’t create the environment with the command
  proposed during the video'
sort_order: 46
---

I struggled with the command:

```bash
 eb init -p docker tumor-diagnosis-serving -r eu-west-1
```

Which resulted in an error when running:

```bash
eb local run --port 9696
```

```
ERROR: NotSupportedError - You can use "eb local" only with preconfigured, generic and multicontainer Docker platforms.
```

I replaced it with:

```bash
eb init -p "Docker running on 64bit Amazon Linux 2" tumor-diagnosis-serving -r eu-west-1
```

This allowed the recognition of the Dockerfile and the build/run of the docker container.