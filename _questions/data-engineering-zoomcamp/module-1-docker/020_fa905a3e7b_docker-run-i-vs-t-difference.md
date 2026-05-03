---
id: fa905a3e7b
question: What's the difference between -i and -t in docker run -it?
sort_order: 20
---

```markdown
## Difference between -i and -t in docker run (-it)

When running containers interactively, Docker provides two commonly used flags:

- `-i` (interactive): keeps the container’s STDIN open, even if it is not attached to a terminal. This allows you to send input to the process inside the container.
  Example:
  ```bash
  echo "print(2+2)" | docker run -i python
  ```

- `-t` (tty): allocates a pseudo-terminal (TTY) for the container. This provides proper terminal formatting (line breaks, colors, prompts).
  Example:
  ```bash
  docker run -t ubuntu date
  ```

Using both flags together (`-it`) gives you both an open input stream and a real terminal interface. This is typically what you want for an interactive shell session:
  
  ```bash
  docker run -it ubuntu bash
  ```

In short:
- `-i` = keep STDIN open
- `-t` = allocate a TTY
- `-it` = both, for interactive shells
```