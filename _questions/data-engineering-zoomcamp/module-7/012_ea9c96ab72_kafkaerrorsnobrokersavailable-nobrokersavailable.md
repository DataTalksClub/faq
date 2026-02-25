---
id: ea9c96ab72
question: 'kafka.errors.NoBrokersAvailable: NoBrokersAvailable'
sort_order: 12
---

If you encounter this error, it is likely that your Kafka broker Docker container is not running.

- Use the following command to check the running containers:

  ```bash
  docker ps
  ```

- Navigate to the folder containing your Docker Compose YAML file and execute the following command to start all instances:

  ```bash
  docker-compose up -d
  ```