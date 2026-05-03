---
id: 0a441d9976
question: "ModuleNotFoundError: No module named 'avro'"
sort_order: 3
---

The `confluent-kafka` package doesn't bring in Avro support by default. Install the `[avro]` extra:

```bash
uv add "confluent-kafka[avro]"
# or, with pip:
pip install "confluent-kafka[avro]"
```

References:

- [confluent-kafka-python issue #590](https://github.com/confluentinc/confluent-kafka-python/issues/590)
- [confluent-kafka-python issue #1221](https://github.com/confluentinc/confluent-kafka-python/issues/1221)
