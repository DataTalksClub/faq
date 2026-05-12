---
id: 884bb9afb7
question: 'Docker: Passing envs to my docker image'
sort_order: 24
---

**Problem Description:** 

I was having issues because my Python script was not reading AWS credentials from environment variables. After building the image, I was running it like this:

```bash
docker run -it homework-04 -e AWS_ACCESS_KEY_ID=xxxxxxxx -e AWS_SECRET_ACCESS_KEY=xxxxxx
```

1. **Environment Variables Order: **
   
   You can set environment variables like `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` (if using AWS STS). Ensure these variables are passed before the image name:

   ```bash
   docker run -e AWS_ACCESS_KEY_ID=xxxxxxxx -e AWS_SECRET_ACCESS_KEY=xxxxxx -it homework-04
   ```

2. **Using an Env File:**

   You can pass an env file by using the following command, assuming your env file is named `.env`:

   ```bash
   docker run -it homework-04 --env-file .env
   ```

3. **AWS Configuration Files:**

   If AWS credentials are not found, the AWS SDKs and CLI will check the `~/.aws/credentials` and `~/.aws/config` files for credentials. You can map these files into your Docker container using volumes:

   ```bash
   docker run -it --rm -v ~/.aws:/root/.aws homework:v1
   ```