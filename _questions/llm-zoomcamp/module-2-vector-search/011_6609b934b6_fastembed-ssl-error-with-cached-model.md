---
id: 6609b934b6
question: Why does FastEmbed raise an SSL error even though the model is cached?
sort_order: 11
---

During construction, FastEmbed normally checks the model source. A temporary
Hugging Face or network failure can therefore stop initialization even when
you previously downloaded the model.

After you have populated the cache once, load the model with the same cache
directory and enable local-only loading:

```python
from fastembed import TextEmbedding

model = TextEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    cache_dir="/models/fastembed",
    local_files_only=True,
)
```

Mount `/models/fastembed` into the container and use that same `cache_dir` when
initially downloading and later loading the model. A model stored only in
another cache directory, such as an unmounted host cache, won't be available
inside the container.

`SparseTextEmbedding` and `TextCrossEncoder` also accept `cache_dir` and
`local_files_only`.

If you downloaded and prepared the FastEmbed model directory yourself, you can
instead pass `specific_model_path`. Use retries only while initially
downloading the model. Catching every exception around normal offline
construction can hide configuration and model-format errors.

An incomplete Hugging Face cache can still trigger FastEmbed's fallback network
behavior. Use a complete, explicitly mounted cache or `specific_model_path` for
a fully offline deployment.
