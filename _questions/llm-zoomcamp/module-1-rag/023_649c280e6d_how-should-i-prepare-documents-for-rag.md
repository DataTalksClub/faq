---
id: 649c280e6d
question: How should I prepare documents for RAG?
sort_order: 23
---

Prepare the data so it is clean, structured, and easy to chunk and retrieve.

Common steps:

- Remove obvious noise such as broken HTML, duplicate text, boilerplate, OCR errors, repeated headers, and repeated footers.
- Preserve useful context such as titles, section names, dates, page numbers, speaker names, and Q&A structure.
- Store the result in a structured format that is easy to process. JSON is often convenient, but it is not mandatory.
- Chunk the documents in a way that keeps related context together.
- Keep metadata that may help filtering or ranking later.

The exact format depends on the source data. The goal is not just to make the text shorter, but to make retrieval more accurate.
