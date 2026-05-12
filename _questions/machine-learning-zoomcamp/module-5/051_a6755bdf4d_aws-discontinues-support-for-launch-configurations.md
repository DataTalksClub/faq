---
id: a6755bdf4d
question: 'AWS: Discontinues Support for Launch Configurations'
sort_order: 51
---

Starting on October 1, 2024, the Amazon EC2 Auto Scaling service will no longer support the creation of launch configurations for new accounts. This change is due to launch configurations being phased out and replaced by launch templates by the Amazon EC2 Auto Scaling service.

For more details refer to: [AWS Documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-launch-templates.html)

This replacement of launch configurations by launch templates is what caused the error described previously (“...use launch templates to create configuration templates for your Auto Scaling groups).