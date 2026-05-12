---
id: e3c5c81223
question: Running ‘nvidia-smi’ in a loop without using ‘watch’
sort_order: 18
---

The command `nvidia-smi` has a built-in function that allows it to run in a loop, updating every N seconds, without using the `watch` command.

```bash
nvidia-smi -l <N seconds>
```

For example, the following command will run `nvidia-smi` every 2 seconds until interrupted by pressing `CTRL+C`:

```bash
nvidia-smi -l 2
```