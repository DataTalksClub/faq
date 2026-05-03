---
id: b8f2d6a30c
question: 'Evaluation: Jupyter kernel crashes when embedding the ground-truth set'
sort_order: 2
---

Small-RAM machines (Codespaces default, low-end laptops) run out of memory when an embedding model is loaded alongside the rest of the notebook state.

Workarounds:

- Switch to a smaller embedder. `sentence-transformers/all-MiniLM-L6-v2` (384-dim) is a common drop-in. Note: switching models will change your hit-rate / MRR numbers, so re-run the eval after the switch.
- Move the embedding step into a separate Python script that you run from the terminal, then load the saved vectors back into the notebook.
- Use a Codespaces machine type with more RAM (Settings → "Machine type" on a Codespace), or run locally.
- Process the ground-truth set in batches and free memory between batches (`del`, `gc.collect()`).
