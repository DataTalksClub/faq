---
id: 1c62848f3d
question: 'WARNING: You are using pip version 22.0.4; however, version 22.3.1 is available'
sort_order: 9
---

When running `docker build -t dino-dragon-model`, you might encounter the warning about an outdated pip version.

This warning often comes up due to a mismatch in the versions of the wheel file shown in Alex's video. The video might show a version compatible with Python 8, but you need a wheel for the version you are working on, such as Python 9.

Additionally, ensure you download the wheel file using its raw format link, as copying the link might cause errors. Use the following link:

[GitHub](https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl)

Ensure to address the pip version warning when possible by updating pip using:

```bash
pip install --upgrade pip
```