---
id: fb9fab513f
question: 'Docker - Error response from daemon: invalid mode: \Program Files\Git\var\lib\postgresql\data.'
sort_order: 700
---

Change the mounting path. Replace it with one of following:

-v /e/zoomcamp/...:/var/lib/postgresql/data

-v /c:/.../ny_taxi_postgres_data:/var/lib/postgresql/data\ (leading slash in front of c:)

