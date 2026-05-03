---
id: a63d2734b2
question: 'GCP VM: VM connection request timeout'
sort_order: 17
---

**Question:** I connected to my VM perfectly fine last week (SSH) but when I tried again this week, the connection request keeps timing out.

**Answer:**

1. **Start Your VM:** Make sure the VM is running in your GCP console.

2. **Update External IP:**
   
   - Copy its External IP once the VM is running.
   - Update your SSH configuration file with this IP.

3. **Edit SSH Config:**
   
   ```bash
   cd ~/.ssh
   code config
   ```
   
   This command opens the config file in VSCode for editing.
