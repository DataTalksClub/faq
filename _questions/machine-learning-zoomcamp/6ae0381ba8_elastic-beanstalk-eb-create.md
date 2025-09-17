---
id: 6ae0381ba8
question: Elastic Beanstalk ‘eb create’: ERROR   Creating Auto Scaling launch configuration failed Reason: Resource handler returned message: "The Launch Configuration creation operation is not available in your account. Use launch templates to create configuration templates for your Auto Scaling groups.
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 2300
---

Create your environment using the --enable-spot flag which automatically uses Launch Templates

Example: eb create med-app-env --enable-spot

Another option is to run only eb create and follow the wizard options:

Enter Environment Name

(default is churn-serving-dev): churn-serving-dev

Enter DNS CNAME prefix

(default is churn-serving-dev): churn-serving-dev

Select a load balancer type

1) classic

2) application

3) network

(default is 2): 1

Would you like to enable Spot Fleet requests for this environment? (y/N): y

Enter a list of one or more valid EC2 instance types separated by commas (at least two instance types are recommended).

(Defaults provided on Enter): just type ‘enter’

