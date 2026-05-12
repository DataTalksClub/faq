---
id: 47408c61b9
question: 'TypeError: Descriptors cannot not be created directly.'
sort_order: 10
---


You may encounter the following error when running `gateway.py`:

```
TypeError: Descriptors cannot not be created directly.
```

This error appears in the following context:

```
File "C:\Users\Asia\Data_Science_Code\Zoompcamp\Kubernetes\gat.py", line 9, in <module>
  from tensorflow_serving.apis import predict_pb2
File "C:\Users\Asia\.virtualenvs\Kubernetes-Ge6Ts1D5\lib\site-packages\tensorflow_serving\apis\predict_pb2.py", line 14, in <module>
  from tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2
File "C:\Users\Asia\.virtualenvs\Kubernetes-Ge6Ts1D5\lib\site-packages\tensorflow\core\framework\tensor_pb2.py", line 14, in <module>
  from tensorflow.core.framework import resource_handle_pb2 as tensorflow_dot_core_dot_framework_dot_resource__handle__pb2
File "C:\Users\Asia\.virtualenvs\Kubernetes-Ge6Ts1D5\lib\site-packages\tensorflow\core\framework\resource_handle_pb2.py", line 14, in <module>
  from tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
File "C:\Users\Asia\.virtualenvs\Kubernetes-Ge6Ts1D5\lib\site-packages\tensorflow\core\framework\tensor_shape_pb2.py", line 36, in <module>
  _descriptor.FieldDescriptor(
File "C:\Users\Asia\.virtualenvs\Kubernetes-Ge6Ts1D5\lib\site-packages\google\protobuf\descriptor.py", line 560, in __new__
  _message.Message._CheckCalledFromGeneratedFile()

TypeError: Descriptors cannot not be created directly.
```

This message indicates that your generated protobuf code is out of date, and must be regenerated using `protoc >= 3.19.0`.


To resolve the issue, you have several options:

1. **Regenerate your Protocol Buffers:** If possible, regenerate your .proto files using `protoc >= 3.19.0`.

2. **Downgrade the protobuf package:**
   
   Downgrade the protobuf package to version 3.20.x or lower.

   ```bash
   pipenv install protobuf==3.20.1
   ```
   
3. **Use a different implementation:**
   
   Set the environment variable to use a slower, pure-Python implementation:

   ```bash
   set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
   ```

The issue can often be resolved by downgrading `protobuf` to version `3.20.1`. This was confirmed to work in the described scenario.