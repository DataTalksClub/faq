---
id: 7889d2bad5
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_0f494026.png
question: 'SSH error in VS Code - “Could not establish connection to "de-zoomcamp":
  Permission denied (publickey).”'
sort_order: 24
---

If you are using Windows, try the following steps to resolve the error:

1. Copy the `.ssh` folder from the Linux file path to Windows.
2. In the `config` file, use:
   
   ```
   IdentityFile C:\Users\<username>\.ssh\gcp
   ```
   
   Instead of:
   
   ```
   IdentityFile ~/.ssh/gcp
   ```

3. Ensure the private key file located at `C:\Users\<username>\.ssh\gcp` has an extra line at the end:

   <{IMAGE:image_1}>
