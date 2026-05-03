---
id: d87e3d2a14
question: 'Docker: ERRO[0000] error waiting for container: context canceled'
sort_order: 12
---

You might have installed Docker via snap. Run the following command to verify:

```bash
sudo snap status docker
```

If you receive the response:

```
error: unknown command "status", see 'snap help'.
```

Then uninstall Docker and install it via the [official website](https://docs.docker.com/engine/install/ubuntu/).

Error message: "Bind for 0.0.0.0:5432 failed: port is already allocated."