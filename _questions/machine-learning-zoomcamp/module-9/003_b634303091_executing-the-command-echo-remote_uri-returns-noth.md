---
id: b634303091
question: Executing the command echo ${REMOTE_URI} returns nothing.
sort_order: 3
---

In Unit 9.6, the command `echo ${REMOTE_URI}` is used to print the URI address, but if it returns nothing, the variable may not be set correctly. Here's a solution to address this:

- Set a local variable and assign the URI address in the terminal:

   ```bash
   REMOTE_URI=2278222782.dkr.ecr.ap-south-1.amazonaws.com/clothing-tflite-images
   ```

- Use this variable to log in to the registry. Note that this variable will be lost once the session is terminated.

Here's a step-by-step example on Ubuntu terminal, which faced the same issue:

1. Execute the following command to set the environment variable:

   ```bash
   export REMOTE_URI=1111111111.dkr.ecr.us-west-1.amazonaws.com/clothing-tflite-images:clothing-model-xception-v4-001
   ```

2. Display the value of the variable:

   ```bash
   echo $REMOTE_URI
   ```

   This should print:

   ```
   111111111.dkr.ecr.us-west-1.amazonaws.com/clothing-tflite-images:clothing-model-xception-v4-001
   ```

**Note:**
- The command `echo $REMOTE_URI` does not require curly brackets, unlike in video 9.6.
- Replace `REMOTE_URI` with your actual URI.
