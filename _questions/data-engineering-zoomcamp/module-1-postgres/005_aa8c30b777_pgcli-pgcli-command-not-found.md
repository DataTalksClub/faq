---
id: aa8c30b777
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_b33cbd22.png
question: 'PGCLI - pgcli: command not found'
sort_order: 5
---

### Problem

If you have already installed `pgcli` but Bash or the Windows Terminal doesn't recognize the command:

- On Git Bash: 
  ```bash
  bash: pgcli: command not found
  ```
- On Windows Terminal: 
  ```
  pgcli: The term 'pgcli' is not recognized…
  ```

### Solution

Try adding the Python path to the Windows PATH variable:

1. Use the command to get the location:
   ```bash
   pip list -v
   ```
2. Copy the path, which looks like:
   ```
   C:\Users\...\AppData\Roaming\Python\Python39\site-packages
   ```
3. Replace `site-packages` with `Scripts`:
   ```
   C:\Users\...\AppData\Roaming\Python\Python39\Scripts
   ```

It might be that Python is installed elsewhere. For example, it could be under:

- `c:\python310\lib\site-packages`

In that case, you should add:

- `c:\python310\lib\Scripts` to PATH.

### Instructions

- Add the determined path to `Path` (or `PATH`) in System Variables.

<{IMAGE:image_1}>

### Reference

[Stack Overflow Reference](https://stackoverflow.com/a/68233660)