---
id: 51bc7e280d
question: 'GCP VM - mkdir: cannot create directory ‘.ssh’: Permission denied'
sort_order: 15
---

If you encounter an error while trying to create a directory:

```bash
User1@DESKTOP-PD6UM8A MINGW64 /

$ mkdir .ssh

mkdir: cannot create directory ‘.ssh’: Permission denied
```

This error occurs because you are attempting to create the directory in the root folder (`/`).

To resolve this, create the directory in your home directory instead. Use the following steps:

1. Navigate to your home directory using:
   
   ```bash
   cd ~
   ```

2. Create the `.ssh` directory:
   
   ```bash
   mkdir .ssh
   ```

For further guidance, watch [this video](https://www.youtube.com/watch?v=ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb).