---
course: data-engineering-zoomcamp
id: b2c1c1d0ec
question: 'Python Kafka: ‘KafkaTimeoutError: Failed to update metadata after 60.0
  secs.’ when running stream-example/producer.py'
section: 'Module 6: streaming with kafka'
sort_order: 4060
---

Restarting all services worked for me:

docker-compose down

docker-compose up

