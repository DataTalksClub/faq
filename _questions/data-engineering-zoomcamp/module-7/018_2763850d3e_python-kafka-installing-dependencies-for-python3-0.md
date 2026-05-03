---
id: 2763850d3e
question: 'Streaming: installing dependencies for the Python avro example (producer.py)'
sort_order: 18
---

For the `06-streaming/python/avro_example/producer.py` script, install:

```bash
uv add confluent-kafka fastavro
# or, with pip:
pip install confluent-kafka fastavro
```

Then run with `uv run python producer.py` (or `python producer.py` from inside an activated venv).
