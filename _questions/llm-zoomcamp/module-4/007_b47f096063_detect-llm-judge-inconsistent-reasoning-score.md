---
id: b47f096063
question: How do I catch an inconsistent score from an LLM-as-judge evaluation?
sort_order: 7
---

When using LLM-as-a-judge, don't rely only on the numeric score — also read the judge's written reasoning next to the score. A distinct failure mode is a justification that says one thing while the numeric score contradicts it (e.g. the reasoning concludes the answer is correct, yet the score is low). This is invisible in aggregate statistics over large batches because it "averages out" — it only surfaces through case-level inspection, so spot-check a small sample (5-10 items) by hand.

To make the check easy, structure the judge output so reasoning and score always appear together:

```python
from pydantic import BaseModel

class JudgeScore(BaseModel):
    reasoning: str
    score: int  # e.g. 1-3
```

Then review a small sample manually:

```python
for result in sample:  # 5-10 scored items, checked by hand
    print(f"Reasoning: {result.reasoning}")
    print(f"Score: {result.score}")
    # does the reasoning's conclusion actually match the score?
```

If the judge returns only a bare number with no reasoning text, this check is impossible. See the [Module 4 LLM-as-judge lesson](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2026/04-evaluation/13-llm-as-judge.md) and [Hamel's LLM-judge guide](https://hamel.dev/blog/posts/llm-judge/).
