---
id: 05dc43cda8
question: Jupyter Notebook or SparkUI not loading properly at localhost after port forwarding from VS code?
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3770
---

Possible solution - Try to forward the port using ssh cli instead of vs code.

Run > “ssh -L <local port>:<VM host/ip>:<VM port> <ssh hostname>”

ssh hostname is the name you specified in the ~/.ssh/config file

In case of Jupyter Notebook run

“ssh -L 8888:localhost:8888 gcp-vm”

from your local machine’s cli.

NOTE: If you logout from the session, the connection would break. Also while creating the spark session notice the block's log because sometimes it fails to run at 4040 and then switches to 4041.

~Abhijit Chakrborty: If you are having trouble accessing localhost ports from GCP VM consider adding the forwarding instructions to .ssh/config file as following:

```

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

