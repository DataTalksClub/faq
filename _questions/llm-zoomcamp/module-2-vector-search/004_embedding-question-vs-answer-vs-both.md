---
id: 5c4a8d2e60
question: 'Vector search: should I embed the question, the answer, or both?'
sort_order: 4
---

There's no single right answer — it's an experiment to run on your dataset. The course shows three options:

- Embed the answer (`text`) only — works because the model captures semantic similarity between questions and their answers.
- Embed the question only — works because user queries look like the indexed questions.
- Embed `question + " " + text` — often the best, but produces longer input and slightly more cost.

Pick whichever gives the best hit rate / MRR on your ground-truth set. The course materials include a side-by-side comparison.
