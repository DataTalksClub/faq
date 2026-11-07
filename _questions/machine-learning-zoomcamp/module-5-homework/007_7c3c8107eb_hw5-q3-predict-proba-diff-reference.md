---
id: 7c3c8107eb
question: In Homework 5 (2026), why does my Question 3 `predict_proba` result differ
  from the reference probability even though my script runs?
sort_order: 7
---

For Homework 5 (2026) Question 3, differing probabilities usually mean you’re not using the exact frozen artifact and the exact input preprocessing that the grader expects.

1) Verify you’re using the checked-in frozen model artifact
- Go to `cohorts/2026/homework/05-deployment/` and do not regenerate the lockfile.
- Check the model file matches the homework metadata:

```bash
cd cohorts/2026/homework/05-deployment
sha256sum pipeline.bin
```

- The SHA-256 you get must match the value shown in `homework.md` and in `model_metadata.json` under `model_sha256`.

2) Call `predict_proba` the same way as the homework
- Load the exact checked-in artifact (the `pipeline.bin` you validated above).
- For Question 3, pass the exact lead dictionary from the homework to:

`pipeline.predict_proba([lead])[0, 1]`

- Report the probability rounded to three decimals.
- Don’t “snap” to a multiple-choice option; the grader expects the computed value (allowed absolute error is `0.005`).

3) Make sure you didn’t change the missing-value normalization behavior
If you call the provided code/API with missing fields:
- `predict.py` uses `normalize_record` from `model.py`.
- Missing categorical values become `NA`.
- Missing numeric values use the training-set medians.
- Do not replace missing numeric values with `0`.

4) Cross-check with the container (Question 6 consistency)
- For Question 6, send the same request used in Question 4 to the container.
- The container’s probability should match Question 4 within absolute tolerance `0.005`.
- If it doesn’t, use `/health` to compare which model/features-default hashes the API loaded against `model_metadata.json`.