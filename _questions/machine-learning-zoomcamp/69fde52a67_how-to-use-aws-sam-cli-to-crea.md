---
course: machine-learning-zoomcamp
id: 69fde52a67
question: How to Use AWS SAM CLI to Create a Lambda Function as a Container Image
section: 10. Kubernetes and TensorFlow Serving
sort_order: 3400
---

Set Up SAM CLI on Your Machine
Follow the installation guide for the AWS SAM CLI here:

Create a New Project
Open your command prompt and run the following command to generate boilerplate code:
sam init

Follow the SAM CLI Wizard

Select "AWS Quick Start Templates".

Choose "Machine Learning" as the application type.

Select the version of Python you will use for your runtime.

When prompted for the starter template, choose "TensorFlow Machine Learning Inference API".

After completing these steps, a new folder with the name you selected will be created. This will be your "SAM project folder" from now on. Inside this folder, you should see an "app" folder.

Add Required Files for Deployment
Move all the files you need for deployment (such as the TensorFlow Lite model and your Lambda function) into the "app" folder.

Modify the Following Files Inside the "app" Folder

requirements.txt
Replace the TensorFlow dependency with tflite-runtime, adjusting the version as necessary. You may also add any other dependencies you require, such as the requests library, and adjust the version of numpy if needed.
Example content for requirements.txt:

pillow==11.1.0

requests==2.32.3

numpy==1.26.4

tflite-runtime==2.7.0

Dockerfile
Modify the Dockerfile to copy the necessary files for your deployment after running pip install. In the default file created, it assumes that the Lambda function is in app.py and the model is inside the app/models folder. However, in this example, we assume the model is at the same level as the Lambda function.
Here's an example of an updated Dockerfile:

FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt ./

RUN python3.9 -m pip install -r requirements.txt -t .

COPY app.py ./

COPY class_indices.json ./

COPY classification_model.tflite ./

ENV MODEL_PATH ./classification_model.tflite

ENV CLASSES_PATH ./class_indices.json

CMD ["app.lambda_handler"]

Build the Lambda Function
From the SAM project directory, build the Lambda function by running:
sam build --build-dir .aws-build

After completing this step, the Docker image will be created. You can verify this by running:
docker images

Test the Lambda Function Locally
To test the image, you can run a container based on it and send a request to the service using a script, as we learned in class, or you can use SAM CLI as follows:

Modify the app/event/event.json file to include the JSON input expected by your Lambda function. For example:
{

"url": "http://bit.ly/mlbookcamp-pants"

}

From the SAM project folder, run the following command:

sam local invoke -t .aws-build/template.yaml -e events/event.json

This will start a container, send the event, and display the response. The output will also show the name of the Docker image used for the container.

Deploy the image

To deploy the image you can follow the instructions learned at classes or you can use this command and follow the prompt

sam deploy --guided

(AWS SAM takes care of creating and ECR repository)

(added by Karina)

