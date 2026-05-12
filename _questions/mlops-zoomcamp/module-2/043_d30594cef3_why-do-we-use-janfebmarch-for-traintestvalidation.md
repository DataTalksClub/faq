---
id: d30594cef3
question: Why do we use Jan/Feb/March for Train/Test/Validation Purposes?
sort_order: 43
---

We use this type of split approach instead of a random split to address specific needs in model evaluation, primarily focusing on seasonality and preventing data leakage.

1. **"Out of Time" Validations:**
   - **Check for Seasonality:**
     - By using specific periods like Jan/Feb/March, we can assess if there are seasonal effects in the data.
     - Example: If the RMSE for the test period is 5, but the RMSE for validation is 20, this indicates significant seasonality. This might suggest switching to Time Series approaches.
   
2. **Prevent Data Leakage:**
   - When predicting future outcomes, a "random sample" train/test split can introduce data leakage, resulting in overfitting and poor model performance in production.
   - It's crucial not to use future information when predicting the present in a model context.

- **Train:** January
- **Test:** February
- **Validate:** March

The validation process is essential for reporting model metrics to leadership, regulators, auditors, and for analyzing target drift in the models.

<Problem and approach discussed were provided by an internal source.>