---
id: 687d54c6ba
question: 'Docker: Docker-compose takes infinitely long to install zip unzip packages
  for linux, which are required to unpack datasets.'
sort_order: 33
---

To resolve the issue, you can try the following solutions:

1. Add the `-Y` flag to `apt-get` to automatically agree to install additional packages.
   
   ```bash
   sudo apt-get install -y zip unzip
   ```

2. Use the Python `ZipFile` package, which is included in all modern Python distributions. This can bypass the need to install `zip` and `unzip` packages.

   ```python
   from zipfile import ZipFile

   with ZipFile('file.zip', 'r') as zip_ref:
       zip_ref.extractall('destination_folder')
   ```