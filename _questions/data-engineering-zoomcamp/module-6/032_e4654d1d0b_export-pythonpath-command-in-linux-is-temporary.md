---
id: e4654d1d0b
question: Export PYTHONPATH command in Linux is temporary
sort_order: 32
---

To make the `export PYTHONPATH` command permanent, consider the following options:

1. **Add to `.bashrc`:** 
   - Open the `.bashrc` file located in your home directory using a text editor, such as `nano` or `vim`.
   
   ```bash
   nano ~/.bashrc
   ```
   
   - Add the `export PYTHONPATH` line, such as:
   
   ```bash
   export PYTHONPATH="/your/custom/path"
   ```
   
   - Save the changes and source the file to apply the changes:
   
   ```bash
   source ~/.bashrc
   ```

2. **Run specific commands in Python scripts:**
   - You can initialize the environment directly in a Python script using:
   
   ```python
   import findspark
   findspark.init()
   ```

By using these methods, you ensure that the `PYTHONPATH` is set up for every session automatically.