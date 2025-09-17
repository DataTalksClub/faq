---
course: machine-learning-zoomcamp
id: 0b20afa7bb
question: Deploying to Digital Ocean
section: Miscellaneous
sort_order: 4190
---

You may quickly deploy your project to DigitalOcean App Cloud. The process is relatively straightforward. The deployment costs about 5 USD/month. The container needs to be up until the end of the project evaluation.

Steps:

Register in DigitalOcean

Go to Apps -> Create App.

You will need to choose GitHub as a service provider.

Edit Source Directory (if your project is not in the repo root)

IMPORTANT: Go to settings -> App Spec and edit the Dockerfile path so it looks like ./project/Dockerfile path relative to your repo root

Remember to add model files if they are not built automatically during the container build process.

By Dmytro Durach

