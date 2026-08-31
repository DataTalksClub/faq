---
id: b47f096063
question: How can I detect when an LLM judge gives inconsistent scores compared to
  its own reasoning in LLM-as-judge evaluation?
sort_order: 7
---

When using LLM-as-a-judge, don’t rely only on the numeric score—also read the judge’s written reasoning next to the score, especially during spot-checks on a small sample (e.g., 5–10 items).

A distinct failure mode is when the judge’s justification says one thing, but the numeric score contradicts it (e.g., reasoning concludes the answer is correct, yet it assigns a low score). This can be invisible in aggregate statistics over large batches because it may “average out,” so you need case-level inspection.

To make this easier to check, structure the judge output so the reasoning and score always appear together, for example with a structured schema like:

```python
class JudgeScore(BaseModel):
    reasoning: str
    score: int  # e.g. 1-3
```

Then after scoring, manually review a small sample:

```python
for result in sample:
    print(f"Reasoning: {result.reasoning}")
    print(f"Score: {result.score}")
```

If your judge returns only a bare number (no accompanying reasoning text), this inconsistency check becomes much harder or impossible.