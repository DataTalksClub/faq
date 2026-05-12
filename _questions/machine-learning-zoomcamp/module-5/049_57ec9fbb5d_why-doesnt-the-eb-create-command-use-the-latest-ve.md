---
id: 57ec9fbb5d
question: Why doesn’t the eb create command use the latest version of my Dockerfile?
sort_order: 49
---

When you make local changes to the Dockerfile or any other files and do not commit these changes, AWS Elastic Beanstalk (EB) won’t deploy them. By default, the EB CLI deploys the latest commit in the current branch. 

If you want to deploy to your environment without committing, you can use the `–-stage` option to deploy changes that have been added to the staging area.

If the Docker image creation fails during the `eb create` process, you can still create the image and deploy it by running `eb deploy`.

**To deploy changes without committing:**

1. Add new and changed files to the staging area:
   
   ```bash
   ~/eb$ git add .
   ```

2. Deploy the staged changes with `eb deploy`:
   
   ```bash
   ~/eb$ eb deploy --staged
   ```