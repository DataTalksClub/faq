---
course: mlops-zoomcamp
id: 9f6380d76b
question: AWS costs
section: 'Module 1: Introduction'
sort_order: 360
---

I am worried about the cost of keeping an AWS instance running during the course.

With the instance specified during working environment setup, if you remember to Stop Instance once you finished your work for the day.  Using that strategy, in a day with about 5 hours of work you will pay around $0.40 USD which will account for $12 USD per month, which seems to be an affordable amount.

You must remember that you would have a different IP public address every time you Restart your instance, and you would need to edit your ssh Config file.  It's worth the time though.

Additionally, AWS enables you to set up an automatic email alert if a predefined budget is exceeded.

.

Also, you can estimate the cost yourself, using  (to use it you don’t even need to be logged in).
At the time of writing (20.05.2023) t3a.xlarge instance with 2 hr/day usage (which translates to 10 hr/week that should be enough to complete the course) and 30GB EBS monthly cost is 10.14 USD

Here’s

Added by Alex Litvinov ()

