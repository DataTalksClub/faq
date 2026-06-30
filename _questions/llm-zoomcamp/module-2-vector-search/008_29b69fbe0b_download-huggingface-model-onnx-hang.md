---
id: 29b69fbe0b
question: Why does download.py hang at 0% when downloading model.onnx from HuggingFace?
sort_order: 8
---

This can happen due to a slow or blocked connection to HuggingFace's CDN. Fix: download the file directly from your browser at https://huggingface.co/Xenova/all-MiniLM-L6-v2/resolve/main/onnx/model.onnx and save it to models/Xenova/all-MiniLM-L6-v2/model.onnx. The script checks if the file exists locally before re-downloading, so it'll skip straight past once it's there.