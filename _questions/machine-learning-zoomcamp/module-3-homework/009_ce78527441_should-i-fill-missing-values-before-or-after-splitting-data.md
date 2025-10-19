---
id: ce78527441
question: Should I fill missing values before or after splitting data (Q4)?
sort_order: 9
---

When working on Q4, should I handle missing values (fillna) before splitting the data, or should I do it in each individual question?

This is an important ML workflow design decision. Here are the tradeoffs:

**Option A: Handle missing values before splitting**
- Clean data once, use everywhere. All future scripts for q3, q4, q5, q6, etc get clean data automatically.
- More efficient as we don't repeat cleaning logic
- CAUTION: You need to be careful about data leakage (see below)

**Option B: Handle missing values in each question script (after splitting)**
- Each script is self-contained
- More flexible if different questions need different fillna strategies
- You'd need to repeat cleaning logic multiple times

So the critical question comes to **"does your strategy means data leakage?"**:
- If you fill numerical with **mean** → you MUST compute mean from train only (so you need to do it after the split!)
- If you fill numerical with constant, like **0.0** → Safe to do before split! Because this means there would be no leakage.

For example, if the homework specifies specific `fillna` values:
- Categorical → 'NA' (constant)
- Numerical → 0.0 (constant)

It means that both strategies use constants, so it's **safe to fill missing values before splitting** and there's no data leakage risk! This is because we're not computing statistics from the data.

If the fillna in the homework uses constants as fills, filling before splitting the data is more efficient since you clean the data once and all subsequent scripts use clean data automatically. Otherwise, you need to be extremely very careful about the data splits and fillna in your scripts

In production systems, the source data is rarely filled in for misisng values during the initial ingestion step. This is because you likely want to be able to reproduce all transformation on your side starting from "source as is".
