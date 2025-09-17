---
id: cd8a62fc55
question: Java Kafka: When running the producer/consumer/etc java scripts, no results retrieved or no message sent
section: Module 6: streaming with kafka
course: data-engineering-zoomcamp
sort_order: 4110
---

For example, when running JsonConsumer.java, got:

Consuming form kafka started

RESULTS:::0

RESULTS:::0

RESULTS:::0

Or when running JsonProducer.java, got:

Exception in thread "main" java.util.concurrent.ExecutionException: org.apache.kafka.common.errors.SaslAuthenticationException: Authentication failed

Solution:

Make sure in the scripts in src/main/java/org/example/ that you are running (e.g. JsonConsumer.java, JsonProducer.java), the StreamsConfig.BOOTSTRAP_SERVERS_CONFIG is the correct server url (e.g. europe-west3 from example vs europe-west2)

Make sure cluster key and secrets are updated in src/main/java/org/example/Secrets.java (KAFKA_CLUSTER_KEY and KAFKA_CLUSTER_SECRET)

