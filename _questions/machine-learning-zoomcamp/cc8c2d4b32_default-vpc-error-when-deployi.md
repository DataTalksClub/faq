---
course: machine-learning-zoomcamp
id: cc8c2d4b32
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_a34a34fc.png
question: 'Default VPC Error when deploying to AWS Elastic Beanstalk:'
section: 5. Deploying Machine Learning Models
sort_order: 2320
---

In case of encounter this error when following the tutorial about deploying app to AWS. When you enter the command “eb create churn-prediction-env” it will prompt created successfully but later shows an error of VPC configuration, there is no default VPC for the selected region, go to AWS Console, select your region from the top bar (example: us-east-2), search for VPC and from the left menu go to “Your VPCs”. It is possible that you dont have any at this point, the action to create default VPC will be available, click on it and run the command again.

<{IMAGE:image_1}>

(Added by Kelly Vergara)

