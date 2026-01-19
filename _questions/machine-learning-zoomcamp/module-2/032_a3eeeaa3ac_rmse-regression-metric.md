---
id: a3eeeaa3ac
question: How is RMSE a performance metric relevant to regression?
sort_order: 32
---

Root Mean Squared Error (RMSE) is a common metric to evaluate regression models. It measures the typical magnitude of prediction errors in the same units as the target variable and is the square root of the Mean Squared Error (MSE).

Example:

Consider five houses with the following actual prices and model predictions:

| House | Actual | Prediction |
|---|---:|---:|
| H1 | 100 | 120 |
| H2 | 150 | 140 |
| H3 | 200 | 230 |
| H4 | 250 | 280 |
| H5 | 300 | 240 |

Baseline (mean as prediction): the mean Actual is 200. The squared spread from the mean is

= (100-200)^2 + (150-200) + (200-200)^2 + (250-200)^2 + (300-200)^2

= 20,000 USD

Now, compute the same with the model predictions to obtain the Mean Squared Error (MSE):

= (100-120)^2 + (150-140) + (200-230)^2 + (250-280) + (300-240)^2

= 4,880

When R2 is calculated, 1 - (Total spread from mean / total spread of predictions) => 1 - 4,880 / 20,000 = 0.75 or 75%.

What does this mean in practical terms?
The model has reduced the uncertainty in house prices by 75%. Without the model, our best guess for any house is the mean ($200) and the typical deviation from the mean is the standard deviation (which is the square root of the variance, i.e., sqrt(20000/5) ≈ 200 dollars). With the model, the typical error (root mean squared error) is sqrt(4880/5) = sqrt(976) ≈ 31 dollars. So, the model has reduced the typical error from about $200 to about $31.

Another explanation for R2:
If you look at all the reasons why house prices in our dataset differ from the average price, our model (using features like size, location, bedrooms, etc.) can explain 75% of those reasons. 25% of the price differences remain mysterious.

In essence, in addition to RMSE (which you want to minimize), R2 should be between 0 and 1, and a higher value is better. (If it is too high, it may indicate overfitting.)