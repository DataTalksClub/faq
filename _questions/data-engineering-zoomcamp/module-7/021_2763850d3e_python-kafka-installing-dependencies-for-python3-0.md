---
id: 2763850d3e
question: 'Python Kafka: Installing dependencies for python3 06-streaming/python/avro_example/producer.py'
sort_order: 21
---

To install the necessary dependencies for running `producer.py` in the `avro_example` directory, use the following commands:

- Install `confluent-kafka`:
  - Using pip:
  ```bash
  pip install confluent-kafka
  ```
  - Using conda:
  ```bash
  conda install conda-forge::python-confluent-kafka
  ```

- Install `fastavro`:
  ```bash
  pip install fastavro
  ```
