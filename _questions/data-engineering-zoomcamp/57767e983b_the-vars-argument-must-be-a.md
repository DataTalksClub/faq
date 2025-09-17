---
course: data-engineering-zoomcamp
id: 57767e983b
question: The - vars argument must be a YAML dictionary, but was of type str
section: 'Module 4: analytics engineering with dbt'
sort_order: 2970
---

Remember to add a space between the variable and the value. Otherwise, it won't be interpreted as a dictionary.

It should be:

dbt run --var 'is_test_run: false'

Not able to change Environment Type as it is greyed out and inaccessibleYou don't need to change the environment type. If you are following the videos, you are creating a Production Deployment, so the only available option is the correct one.'

