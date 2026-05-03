---
id: ed8dcfbb5a
question: 'Docker: The input device is not a TTY (Docker run for Windows)'
sort_order: 7
---

You may encounter this error:

```bash
$ docker run -it ubuntu bash
the input device is not a TTY. If you are using mintty, try prefixing the command with 'winpty'
```

Solution:

- Use `winpty` before the Docker command:
  
  ```bash
  $ winpty docker run -it ubuntu bash
  ```

- Alternatively, create an alias:
  
  ```bash
  echo "alias docker='winpty docker'" >> ~/.bashrc
  ```
  
  or
  
  ```bash
  echo "alias docker='winpty docker'" >> ~/.bash_profile
  ```
  
Source: [Stack Overflow](https://stackoverflow.com/a/49965690)