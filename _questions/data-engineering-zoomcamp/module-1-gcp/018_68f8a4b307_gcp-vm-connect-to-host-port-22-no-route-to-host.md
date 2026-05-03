---
id: 68f8a4b307
question: 'GCP VM: connect to host port 22 no route to host'
sort_order: 18
---

Go to edit your VM.

1. Navigate to the **Automation** section.
2. Add the following Startup script:
   
   ```bash
   #!/bin/bash
   sudo ufw allow ssh
   ```
3. Stop and Start the VM.