---
id: a8219681ec
question: 'GCP for the course: free trial vs sandbox, paying, country restrictions,
  why GCP'
sort_order: 4
---

## Why GCP and not AWS / Azure?

For uniformity across the cohort. The course uses BigQuery, which is GCP-only, and most students already have a Google account that works for sign-up. The concepts (data warehouse, object storage, IaC) translate to AWS/Azure, but the lessons are recorded against GCP. You can use a different cloud — see [the environment FAQ](#4f1fe161b1) for tradeoffs.

## Do I have to pay?

No. GCP offers a free trial with $300 in credits for new accounts. The course materials fit comfortably within that budget if you destroy unused resources (VMs, datasets, buckets) after each module. Check your billing dashboard daily, especially after spinning up Compute Engine VMs.

To sign up for the free trial you need a valid credit/debit card; GCP uses it to verify identity but doesn't charge it without your consent.

## Free Trial vs Sandbox — which one?

GCP has two free options. They are not equivalent for this course:

- Free Trial ($300 credit, 90 days). Required for the course — gives you VMs, GCS buckets, and full BigQuery functionality.
- Sandbox (free, no credit card). Limited services. It does not include VMs or GCS, and BigQuery features are restricted, so you cannot complete the course on Sandbox alone.

Use the Free Trial.

## My country isn't supported / my card isn't accepted

GCP isn't available in some countries, and some cards are rejected even where it is. Workarounds students have used:

- Try a different card. Cards from some banks (e.g. Kazakhstan-based Kaspi) sometimes don't work; cards from other banks/countries (e.g. TBC in Georgia) do.
- Pyypl and similar virtual cards have worked for some.
- If you can't get a GCP account at all, you can still complete most of the course locally — only Module 3's homework strictly requires BigQuery. See the environment FAQ for which parts have local alternatives.
