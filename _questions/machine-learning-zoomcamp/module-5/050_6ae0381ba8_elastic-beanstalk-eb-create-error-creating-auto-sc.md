---
id: 6ae0381ba8
question: 'Elastic Beanstalk ‘eb create’: ERROR   Creating Auto Scaling launch configuration
  failed Reason: Resource handler returned message: "The Launch Configuration creation
  operation is not available in your account. Use launch templates to create configuration
  templates for your Auto Scaling groups."'
sort_order: 50
---

To resolve this issue, you can create your environment using the `--enable-spot` flag, which automatically uses Launch Templates.

Example:

```bash
eb create med-app-env --enable-spot
```

Another option is to run `eb create` and follow the wizard options:

1. Enter Environment Name:
   - Default: `churn-serving-dev`
   - Example: `churn-serving-dev`

2. Enter DNS CNAME prefix:
   - Default: `churn-serving-dev`
   - Example: `churn-serving-dev`

3. Select a load balancer type:
   
   ```
   1) classic
   2) application
   3) network
   (default is 2): 1
   ```

4. Would you like to enable Spot Fleet requests for this environment? 
   - Prompt: `(y/N):`
   - Example: `y`

5. Enter a list of one or more valid EC2 instance types separated by commas (at least two instance types are recommended).
   - Defaults provided on Enter: Press `Enter`