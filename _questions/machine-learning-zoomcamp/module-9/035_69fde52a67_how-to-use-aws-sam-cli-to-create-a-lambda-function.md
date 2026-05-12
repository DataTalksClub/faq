---
id: 69fde52a67
question: How to Use AWS SAM CLI to Create a Lambda Function as a Container Image
sort_order: 35
---

**Set Up SAM CLI on Your Machine**

Follow the installation guide for the AWS SAM CLI: [AWS SAM CLI Installation Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

Additional reference: [Getting started with AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html)

**Create a New Project**

Open your command prompt and run the following command to generate boilerplate code:

```bash
sam init
```

Follow the SAM CLI Wizard:

1. Select "AWS Quick Start Templates".
2. Choose "Machine Learning" as the application type.
3. Select the version of Python you will use for your runtime.
4. When prompted for the starter template, choose "TensorFlow Machine Learning Inference API".

After these steps, a new folder will be created with your selected name. This is your "SAM project folder". Inside, you'll find an "app" folder.

**Add Required Files for Deployment**

Move all the deployment files (such as the TensorFlow Lite model and your Lambda function) into the "app" folder.

**Modify Files Inside the "app" Folder**

**requirements.txt**

Replace the TensorFlow dependency with tflite-runtime, and add any other dependencies. Example content:

```
pillow==11.1.0
requests==2.32.3
numpy==1.26.4
tflite-runtime==2.7.0
```

**Dockerfile**

Modify the Dockerfile to copy the necessary files for deployment. Example Dockerfile:

```dockerfile
FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt ./

RUN python3.9 -m pip install -r requirements.txt -t .

COPY app.py ./
COPY class_indices.json ./
COPY classification_model.tflite ./

ENV MODEL_PATH ./classification_model.tflite
ENV CLASSES_PATH ./class_indices.json

CMD ["app.lambda_handler"]
```

**Build the Lambda Function**

From the SAM project directory, build the Lambda function:

```bash
sam build --build-dir .aws-build
```

After building, verify the Docker image by running:

```bash
docker images
```

**Test the Lambda Function Locally**

Modify the `app/event/event.json` file to include the expected JSON input:

```json
{
  "url": "http://bit.ly/mlbookcamp-pants"
}
```

Run the following command from the SAM project folder:

```bash
sam local invoke -t .aws-build/template.yaml -e events/event.json
```

This command will start a container, send the event, and display the response. The Docker image name used for the container will be shown.

**Deploy the Image**

To deploy the image, follow classroom instructions or use:

```bash
sam deploy --guided
```

AWS SAM will handle creating an ECR repository.