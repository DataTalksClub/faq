---
id: 48ce1d02df
question: 'Which is the correct BigQuery Partition Limit: 4000 or 10000?'
sort_order: 45
---

- The current BigQuery partition limit is 10,000 partitions per table (as of 2026). The playlist listing 4,000 is outdated.
- Time-based partitioning implications:
  - Daily partitions: 10,000 partitions cover over 27 years of data; 4,000 partitions covered about 11 years.
  - Hourly partitions: 10,000 partitions cover about 416 days (a little over a year); 4,000 partitions covered about 166 days.
  - Monthly partitioning with the 10,000 limit can cover over 830 years of data.
- Job operations limit: A single job operation (query or load) cannot modify or affect more than 4,000 partitions at once.
- Reference: Cloud BigQuery quotas documentation: https://docs.cloud.google.com/bigquery/quotas#partitioned_tables