---
id: 76e6d9e8ce
question: 'ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+'
sort_order: 1220
---

If encountering an error while running s3 buckets make sure to resolve dependencies issue by downgrading urllib3 to a compatible version: pip3 install "urllib3<1.27"

Added by Maximilien Eyengue

