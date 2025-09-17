---
id: bac852d170
question: SQL - SELECT * FROM zones_taxi WHERE Zone='Astoria Zone'; Error Column Zone doesn't exist
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1720
---

For the HW1 I encountered this issue. The solution is

SELECT * FROM zones AS z WHERE z."Zone" = 'Astoria Zone';

I think columns which start with uppercase need to go between “Column”. I ran into a lot of issues like this and “ ” made it work out.

Addition to the above point, for me, there is no ‘Astoria Zone’, only ‘Astoria’ is existing in the dataset.

SELECT * FROM zones AS z WHERE z."Zone" = 'Astoria’;

