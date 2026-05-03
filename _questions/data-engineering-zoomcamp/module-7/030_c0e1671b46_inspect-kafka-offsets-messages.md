---
id: c0e1671b46
question: How to Inspect Messages in a Kafka Topic Using Offsets?
sort_order: 30
---

An offset in Kafka is a per-partition sequence number that uniquely identifies messages within that partition. There is no global offset for the entire topic, and consumers use offsets to track what they have processed.

Why inspecting offsets helps: when errors occur in a real-time stream, inspecting messages near a known offset helps you see what data caused the error, understand surrounding context, and reproduce the issue locally.

Viewing offsets and consumer lag

Use the Kafka CLI to see how far a consumer group has progressed:

```bash
kafka-consumer-groups \
  --bootstrap-server localhost:9092 \
  --describe \
  --group rides-to-postgres
```

You can also run this via Docker:

```bash
docker run --rm -it --network pyflink_default confluentinc/cp-kafka:7.6.0 kafka-consumer-groups \
--bootstrap-server redpanda:29092 \
--describe \
--group rides-to-postgres
```

Key fields to look at:

- CURRENT-OFFSET: last offset processed by the consumer
- LOG-END-OFFSET: last offset available in the topic
- LAG: messages pending to be processed

For more details, see the official docs: kafka-consumer-groups-sh

Consuming messages from the beginning of a topic

To inspect all messages in a topic, you can use kafka-console-consumer:

```bash
kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic rides \
  --from-beginning
```

Or via Docker:

```bash
docker run --rm -it --network pyflink_default confluentinc/cp-kafka:7.6.0 kafka-console-consumer \
--bootstrap-server redpanda:29092 \
--topic rides \
--from-beginning
```

Notes:
- This is useful for basic exploration but does not allow jumping to a specific offset.

Inspecting messages from a specific offset with kcat (formerly kafkacat)

A very handy tool is kcat for reading messages starting from a given offset:

```bash
kcat -C \
-b localhost:9092 \
-t rides \
-p 0 \
-o 25 \
-c 5
```

Docker usage:

```bash
docker run --network pyflink_default edenhill/kcat:1.7.1 -C \
-b redpanda:29092 \
-t rides \
-p 0 \
-o 25 \
-c 5
```

Options explained:

- consumer mode `-C`
- broker `-b` (host:port)
- topic `-t` the topic to read from
- partition `-p` the partition
- start at offset `-o` to begin reading
- read up to `-c` messages

This lets you see exactly what happens starting from a particular offset.

Notes:
- kcat is the successor to kafkacat; you can install or run it from Docker.
- Replace broker address and topic/partition as per your environment.

Conclusion

Knowing how to inspect messages with specific offsets is a fundamental skill for Kafka debugging. Use these commands to locate the data around a known offset, monitor consumer lag, and reproduce issues locally when needed.
