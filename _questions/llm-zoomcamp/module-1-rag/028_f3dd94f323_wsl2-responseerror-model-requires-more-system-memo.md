---
id: f3dd94f323
question: 'WSL2: ResponseError: model requires more system memory (X.X GiB) than is
  available (Y.Y GiB). My system has more than X.X GiB.'
sort_order: 28
---

Your WSL2 is set to use Y.Y GiB, not all your computer memory. To allocate more RAM, follow these steps:

1. Create a `.wslconfig` file under your Windows user profile directory: `C:\Users\YourUsername\.wslconfig`.

2. Include the desired RAM allocation in the file:

   ```ini
   [wsl2]
   memory=8GB
   ```

3. Restart WSL using the command:

   ```bash
   wsl --shutdown
   ```

4. Run the `free` command in WSL to verify the changes.

For more details, read [this article](https://www.aleksandrhovhannisyan.com/blog/limiting-memory-usage-in-wsl-2/).
