---
id: cc4d23c338
question: Why does the Homework 5 predict API accept unknown categories and out-of-range values?
sort_order: 8
---

The Homework 5 request model declares field types but no allowed categories or numeric ranges. A value with the expected type, such as `tiktok` or `-3`, passes request validation. `DictVectorizer` silently ignores features it didn't see during `fit`, so an unknown category can produce a prediction without raising an error.

For a service with real users, add category validators and numeric constraints based on your application rules. Keep the provided `predict.py` unchanged when you run the graded Homework 5 checks. To try stricter validation without changing the reference behavior, use a separate app.

See the [Homework 5 API and prediction instructions](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/homework.md#question-4), the [provided API](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/predict.py), and the [DictVectorizer documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html).
