---
id: d8b28c47a0
question: What can I use to extract text from PDFs (or scanned/OCR documents) for my
  RAG project?
sort_order: 16
---

The course doesn't prescribe a specific tool — use whatever works best for your data. Some options people in the community reach for:

- **[docling](https://github.com/docling-project/docling)** — converts PDFs (and other docs) to structured Markdown/JSON, good for RAG.
- **[pymupdf4llm](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/)** / **PyMuPDF** — fast text extraction, Markdown output.
- **[unstructured](https://github.com/Unstructured-IO/unstructured)** — handles many document types and layouts.
- **[pytesseract](https://github.com/madmaze/pytesseract)** (Tesseract OCR) — for scanned/image-based PDFs that have no text layer.
- **Hosted OCR** such as Mistral OCR — if you'd rather call an API than run OCR locally.

Try a couple on a sample of your documents and see which gives the cleanest text. For how to chunk/prepare the extracted text afterwards, see "[How should I prepare documents for RAG?](../module-1-rag/023_649c280e6d_how-should-i-prepare-documents-for-rag.md)".
