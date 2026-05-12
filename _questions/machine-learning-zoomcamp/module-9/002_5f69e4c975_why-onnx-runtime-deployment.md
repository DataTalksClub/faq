---
id: 5f69e4c975
question: Why ONNX Runtime for DL deployment?
sort_order: 2
---

ONNX Runtime provides a cross-framework inference engine for models exported to the ONNX format. If you train in TensorFlow or PyTorch, you can export your model to ONNX and run it with ONNX Runtime, enabling a common deployment path across different environments. This can simplify Lambda/Kubernetes serving by reducing the need to maintain separate framework-specific runtimes (such as TensorFlow Serving or TorchServe) and by providing optimizations available in ONNX Runtime.