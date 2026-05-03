---
id: 73c8de600c
question: 'WSL: Permissions too open at Windows'
sort_order: 29
---


Issue when trying to run the GPC VM through SSH via WSL2, likely because WSL2 isn’t looking for .ssh keys in the correct folder. The command attempted:

```bash
ssh -i gpc [username]@[my external IP]
```

### Solutions

1. **Use `sudo` Command**
   
   Try using `sudo` before executing the command:
   
   ```bash
   sudo ssh -i gpc [username]@[my external IP]
   ```

2. **Change Permissions**
   
   Navigate to your folder and change the permissions for the private key SSH file:
   
   ```bash
   chmod 600 gpc
   ```

3. **Create a `.ssh` Folder in WSL2**
   
   - Navigate to your home directory:
     
     ```bash
     cd ~
     ```
   
   - Create a `.ssh` folder:
     
     ```bash
     mkdir .ssh
     ```
   
   - Copy the content from the Windows `.ssh` folder to the newly created `.ssh` folder:
     
     ```bash
     cp -r /mnt/c/Users/YourUsername/.ssh/* ~/.ssh/
     ```
   
   - Adjust the permissions of the files and folders in the `.ssh` directory if necessary.