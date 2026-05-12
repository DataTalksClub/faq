---
id: 76e6d9e8ce
question: 'ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+'
sort_order: 45
---

If you're encountering this error while running `mlflow server` against S3 or Postgres (e.g. on an Amazon Linux 2 instance with OpenSSL 1.0.2):

```
ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.0.2k-fips  26 Jan 2017'.
```

Pin urllib3 to a compatible version:

```bash
pip3 install "urllib3<1.27"
```

Alternatively, upgrading `mlflow` itself often downgrades `urllib3` as a side effect, fixing the import:

```bash
pip3 install --upgrade mlflow
```
