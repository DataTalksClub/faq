---
id: c1135885e3
question: Why does wget fail to download the CloudFront parquet file even with --no-check-certificate,
  and how can I work around network blocks?
sort_order: 8
---

The download may fail not because of SSL verification but because the network blocks requests to the CloudFront domain. In some networks, requests to the dataset URL are redirected to a block page such as https://blocked.sbmd.cicc.gov.ph/.

Solution 1 — Skip certificate check (SSL verification disabled)

```
!wget --no-check-certificate https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-11.parquet
```

Solution 2 — If your network blocks CloudFront entirely, connect to a VPN and run the original command again:

```
!wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-11.parquet
```

Using a VPN successfully bypassed the network block.
