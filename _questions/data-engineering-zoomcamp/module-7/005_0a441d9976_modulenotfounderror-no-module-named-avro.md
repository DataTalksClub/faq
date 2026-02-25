---
id: 0a441d9976
question: 'ModuleNotFoundError: No module named ''avro'''
sort_order: 5
---

### Solution

To resolve the error, install the Avro module using the following command:

```bash
pip install confluent-kafka[avro]
```

Note: This issue may occur because Conda does not include the Avro module when installing `confluent-kafka` via pip.

### Additional Resources

For more information on Anaconda and `confluent-kafka` issues, visit the following links:

- [GitHub Issue 590](https://github.com/confluentinc/confluent-kafka-python/issues/590)
- [GitHub Issue 1221](https://github.com/confluentinc/confluent-kafka-python/issues/1221)
- [StackOverflow Discussion](https://stackoverflow.com/questions/69085157/cannot-import-producer-from-confluent-kafka)