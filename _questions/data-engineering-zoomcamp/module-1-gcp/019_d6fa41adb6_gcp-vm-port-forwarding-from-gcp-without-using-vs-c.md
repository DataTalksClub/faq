---
id: d6fa41adb6
question: 'GCP VM: Port forwarding from GCP without using VS Code'
sort_order: 19
---

You can easily forward the ports of pgAdmin, PostgreSQL, and Jupyter Notebook using the built-in tools in Ubuntu without any additional client:

1. **On the VM machine:**
   - Launch Docker and Jupyter Notebook in the correct folder using:
     ```bash
     docker-compose up -d
     jupyter notebook
     ```

2. **From the local machine:**
   - Execute:
     ```bash
     ssh -i ~/.ssh/gcp -L 5432:localhost:5432 username@external_ip_of_vm
     ```
   - Execute the same command for ports 8080 and 8888.

3. **Accessing Applications Locally:**
   - For pgAdmin, open a browser and go to `localhost:8080`.
   - For Jupyter Notebook, open a browser and go to `localhost:8888`.
     - If you encounter issues with credentials, you may need to copy the link with the access token from the terminal logs on the VM when you launched the Jupyter Notebook.

4. **Forwarding Both pgAdmin and PostgreSQL:**
   - Use:
     ```bash
     ssh -i ~/.ssh/gcp -L 5432:localhost:5432 -L 8080:localhost:8080 modito@35.197.218.128
     ```