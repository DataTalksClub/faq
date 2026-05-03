---
id: 16d0d756c3
question: 'WSL: Could not resolve host name'
sort_order: 30
---

WSL2 may not be referencing the correct `.ssh/config` path from Windows. You can create a config file in the home directory of WSL2 by following these steps:

1. Navigate to your home directory:
   
   ```bash
   cd ~
   ```

2. Create the `.ssh` directory:
   
   ```bash
   mkdir .ssh
   ```

3. Create a `config` file in the `.ssh` folder with the following content:

   ```
   HostName [GPC VM external IP]
   User [username]
   IdentityFile ~/.ssh/[private key]
   ```