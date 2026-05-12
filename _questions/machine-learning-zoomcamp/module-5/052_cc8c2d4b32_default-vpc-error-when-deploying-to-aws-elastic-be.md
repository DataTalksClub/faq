---
id: cc8c2d4b32
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_a34a34fc.png
question: 'Default VPC Error when deploying to AWS Elastic Beanstalk:'
sort_order: 52
---

When encountering a VPC configuration error during the deployment to AWS Elastic Beanstalk, follow these steps:

1. Execute the command:
   ```bash
   eb create churn-prediction-env
   ```
   
2. If the environment creation initially appears successful but later shows an error related to VPC configuration, it likely means there is no default VPC for the selected region.

3. Go to the AWS Console and select your region from the top bar (e.g., `us-east-2`).

4. Search for "VPC" and from the left menu, navigate to "Your VPCs".

5. If no VPCs are present, the option to create a default VPC will be available. Click on it.

6. Once the default VPC is created, rerun the command.

<{IMAGE:image_1}>
