---
id: 9ee43d55d0
question: Running multiple services in a Docker container
sort_order: 16
---

If you are trying to run Flask with Gunicorn and an MLFlow server from the same container, defining both services in the Dockerfile with CMD will only run MLFlow and not Flask.

1. **Create separate shell scripts with server run commands**:
   
   - **For Flask with Gunicorn:**
     
     Save as `script1.sh`:
     
     ```bash
     #!/bin/bash
     
gunicorn --bind=0.0.0.0:9696 predict:app
     ```

   - **For MLFlow server:**
     
     Save as `script2.sh`:
     
     ```bash
     #!/bin/bash
     
mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri=sqlite:///mlflow.db --default-artifact-root=g3://zc-bucket/mlruns/
     ```

2. **Create a wrapper script** to run the above two scripts:

   Save as `wrapper_script.sh`:
   
   ```bash
   #!/bin/bash

   # Start the first process
   ./script1.sh &

   # Start the second process
   ./script2.sh &

   # Wait for any process to exit
   wait -n

   # Exit with status of process that exited first
   exit $?
   ```

3. **Give executable permissions to all scripts**:
   
   ```bash
   chmod +x *.sh
   ```

4. **Define the last line of your Dockerfile** as:
   
   ```bash
   CMD ./wrapper_script.sh
   ```

5. **Don't forget to expose all ports defined by the services**.