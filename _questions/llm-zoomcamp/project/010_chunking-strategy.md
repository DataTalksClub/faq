---
id: 6f2a8b3d10
question: 'Project: my corpus is large (long PDFs, many paragraphs). What''s a good
  chunking strategy?'
sort_order: 10
---

Don't try to find the perfect chunker upfront — iterate.

- Start simple: fixed-size chunking (~1000 tokens with some overlap) and run a small ground-truth eval.
- Try smart chunking: ask an LLM to split each document into logical sections, then index each section.
- Add a short LLM-generated summary per chunk and index it alongside, or use it to boost retrieval.
- For long, structured documents (legal, financial), prefer hybrid search (BM25 + dense) so exact wording isn't lost during semantic matching.

Useful tools for parsing PDFs to clean markdown before chunking:

- [`pymupdf4llm`](https://pypi.org/project/pymupdf4llm/) — fast, decent quality.
- [Docling](https://github.com/docling-project/docling) — slower but higher quality on tables/figures.
- [GROBID](https://github.com/kermitt2/grobid) — for academic papers, extracts structure (sections, refs, etc.).

Run the eval again after each change. The goal is measurable improvement on hit rate / MRR for your ground-truth set, not a "perfect" chunker in the abstract.
