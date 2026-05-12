---
id: 814a8657e2
question: Running out of space for AWS instance.
sort_order: 22
---

Due to experimenting extensively, I've run out of space on my 30-GB AWS instance. Deleting Docker images alone does not free up the space as expected. After removing Docker images, you need to run the following command:

```bash
docker system prune
```