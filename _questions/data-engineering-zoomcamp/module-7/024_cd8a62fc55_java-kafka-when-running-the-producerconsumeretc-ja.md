---
id: cd8a62fc55
question: 'Java Kafka: When running the producer/consumer/etc java scripts, no results
  retrieved or no message sent'
sort_order: 24
---

For example, when running `JsonConsumer.java`, you might see:

```
Consuming form kafka started

RESULTS:::0

RESULTS:::0

RESULTS:::0
```

Or when running `JsonProducer.java`, you might encounter:

```
Exception in thread "main" java.util.concurrent.ExecutionException: org.apache.kafka.common.errors.SaslAuthenticationException: Authentication failed
```

**Solution:**

1. Ensure the `StreamsConfig.BOOTSTRAP_SERVERS_CONFIG` in the scripts located at `src/main/java/org/example/` (e.g., `JsonConsumer.java`, `JsonProducer.java`) is pointing to the correct server URL (e.g., `europe-west3` vs `europe-west2`).

2. Verify that the cluster key and secrets are updated in `src/main/java/org/example/Secrets.java` (`KAFKA_CLUSTER_KEY` and `KAFKA_CLUSTER_SECRET`).