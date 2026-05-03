---
id: cef28035ac
question: How do you manually manage offsets in a Kafka consumer?
sort_order: 26
---

Kafka allows you to manually control when message offsets are committed. This is useful when you want to **commit offsets only after successful message processing**, ensuring reliable processing.

**Step 1: Disable Auto Commit**

```python
consumer = KafkaConsumer(
    'taxi-trips',
    bootstrap_servers=['localhost:9092'],
    enable_auto_commit=False  # Manual commit
)
```

Setting `enable_auto_commit=False` prevents Kafka from automatically committing offsets.

**Step 2: Process Messages and Commit Manually**

```python
for message in consumer:
    try:
        # Process the message
        process_trip(message.value)
        # Commit offset after successful processing
        consumer.commit()
    except Exception as e:
        print(f"Error: {e}")
        # Do not commit on failure → message will be reprocessed
```

Offsets are committed **only after** the message is successfully processed. If an error occurs, the offset is not committed, so the message can be consumed again.
