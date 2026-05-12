---
id: 5d9aed1fd0
question: 'Docker: Save Docker Image to local machine and view contents'
sort_order: 21
---

The Docker image can be saved/exported to tar format on a local machine using the following command:

```bash
docker image save <image-name> -o <name-of-tar-file.tar>
```

The individual layers of the Docker image for the filesystem content can be viewed by extracting the `layer.tar` present in the `<name-of-tar-file.tar>` created from above.