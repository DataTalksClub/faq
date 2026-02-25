---
id: 05dc43cda8
question: Jupyter Notebook or SparkUI not loading properly at localhost after port
  forwarding from VS code?
sort_order: 50
---

**Possible Solution:** Try to forward the port using SSH CLI instead of VS Code. 

Run the following command:

```bash
ssh -L <local port>:<VM host/ip>:<VM port> <ssh hostname>
```

- `ssh hostname` is the name you specified in the `~/.ssh/config` file.

For example, in case of Jupyter Notebook, run:

```bash
ssh -L 8888:localhost:8888 gcp-vm
```

from your local machine’s CLI.

**Note:** If you logout from the session, the connection would break. While creating the Spark session, check the block's log because sometimes it fails to run at 4040 and switches to 4041.

If you are having trouble accessing localhost ports from a GCP VM, consider adding the forwarding instructions to the `.ssh/config` file as follows:

```bash
Host <hostname>
  Hostname <external-gcp-ip>
  User xxxx
  IdentityFile yyyy
  LocalForward 8888 localhost:8888
  LocalForward 8080 localhost:8080
  LocalForward 5432 localhost:5432
  LocalForward 4040 localhost:4040
```

This should automatically forward all ports and will enable accessing localhost ports.