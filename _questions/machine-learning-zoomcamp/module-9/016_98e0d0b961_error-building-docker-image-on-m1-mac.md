---
id: 98e0d0b961
question: Error building docker image on M1 Mac
sort_order: 16
---

While trying to build the Docker image in Section 9.5 with the command:

```bash
docker build -t clothing-model .
```

It throws a pip install error for the tflite runtime `.whl` file:

```
ERROR: failed to solve: process "/bin/sh -c pip install https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl" did not complete successfully: exit code: 1
```

1. Try using this direct link for the `.whl` file:
   - [tflite_runtime-2.14.0](https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl)

2. If the link above does not work:
   - The problem occurs due to the ARM architecture of the M1. You may need to run the code on a PC or Ubuntu OS.

3. You can also try the commands below:
   
   - To build the Docker image:
     
     ```bash
     docker build --platform linux/amd64 -t clothing-model .
     ```

   - To run the built image:
     
     ```bash
     docker run -it --rm -p 8080:8080 --platform linux/amd64 clothing-model:latest
     ```