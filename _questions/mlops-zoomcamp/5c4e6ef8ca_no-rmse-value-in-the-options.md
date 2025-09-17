---
course: mlops-zoomcamp
id: 5c4e6ef8ca
question: No RMSE value in the options
section: 'Module 1: Introduction'
sort_order: 470
---

The evaluation RMSE I get doesn’t figure within the options!

If you’re evaluating the model on the entire February data, try to filter outliers using the same technique you used on the train data (0≤duration≤60) and you’ll get a RMSE which is (approximately) in the options. Also don’t forget to convert the columns data types to str before using the DictVectorizer.

Another option: Along with filtering outliers, additionally filter on null values by replacing them with -1.  You will get a RMSE which is (almost same as) in the options. Use ‘.round(2)’ method to round it to 2 decimal points.

Warning deprecation

The python interpreter warning of modules that have been deprecated  and will be removed in future releases as well as making suggestion how to go about your code.

For example

C:\ProgramData\Anaconda3\lib\site-packages\seaborn\distributions.py:2619:

FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).

warnings.warn(msg, FutureWarning)

To suppress the warnings, you can include this code at the beginning of your notebook

import warnings

warnings.filterwarnings("ignore")

