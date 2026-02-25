---
id: b2c1c1d0ec
question: 'Python Kafka: ‘KafkaTimeoutError: Failed to update metadata after 60.0
  secs.’ when running stream-example/producer.py'
sort_order: 16
---

Restarting all services worked for me:

```bash
docker-compose down

docker-compose up
```