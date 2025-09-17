---
id: 57ec9fbb5d
question: Why doesn’t the eb create command use the latest version of my Dockerfile?
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 2290
---

When you make local changes to Dockerfile or any other files and do not commit the changes, AWS won’t  deploy the changes. The reason is that by default, the EB CLI deploys the latest commit in the current branch. If you want to deploy to your environment without committing, you can use the –stage option to deploy changes that have been added to the staging area.

If the docker image creation fails during the “eb create” process, you can still create the image and deploy it by running eb deploy.

To deploy changes without committing

Add new and changed files to the staging area:

~/eb$ git add .

Deploy the staged changes with eb deploy:

~/eb$ eb deploy --staged

(added by Karina)

