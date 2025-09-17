---
id: d4c21886e6
question: WandB API error
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 1150
---

Problem: when running the preprocess_data.py file you get the following error:

wandb: ERROR api_key not configured (no-tty). call wandb.login(key=[your_api_key])

Solution: Go to your WandB profile (top RHS) → user settings → scroll down to “Danger Zone” and copy your API key. 

Then before running preprocess_data.py, add and run the following cell in your notebook:

%%bash

Wandb login <YOUR_API_KEY_HERE>.

Added and Answered by James Gammerman (jgammerman@gmail.com)

