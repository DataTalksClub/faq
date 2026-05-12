---
id: 01514d66d5
question: 'Docker: Dockerfile missing when creating the AWS ElasticBean environment'
sort_order: 47
---

I encountered this error when creating an AWS ElasticBean environment using the command:

```bash
eb create tumor-diagnosis-env
```

**Error Message:**

```bash
ERROR   Instance deployment: Both 'Dockerfile' and 'Dockerrun.aws.json' are missing in your source bundle. Include at least one of them. The deployment failed.
```

The error occurred because I had not committed the files used to build the container, particularly the `Dockerfile`. After performing the following Git operations, the command worked properly:

1. Add the modified files to staging:
   
   ```bash
   git add .
   ```

2. Commit the changes:
   
   ```bash
   git commit -m "Add Dockerfile and necessary files"
   ```