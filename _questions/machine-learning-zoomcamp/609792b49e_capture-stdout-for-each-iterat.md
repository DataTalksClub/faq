---
course: machine-learning-zoomcamp
id: 609792b49e
question: Capture stdout for each iterations of a loop separately
section: 6. Decision Trees and Ensemble Learning
sort_order: 2500
---

I wanted to directly capture the output from the xgboost training for multiple eta values to a dictionary without the need to run the same cell multiple times and manually editing the eta value in between or copy the code for a second eta value.

Using the magic cell command “%%capture output” I was only able to capture the complete output for all iterations for the loop, but. I was able to solve this using the following approach. This is just a code sample to grasp the idea.

# This would be the content of the Jupyter Notebook cell

from IPython.utils.capture import capture_output

import sys

different_outputs = {}

for i in range(3):

with capture_output(sys.stdout) as output:

print(i)

print("testing capture")

different_outputs[i] = output.stdout

# different_outputs

# {0: '0\ntesting capture\n',

#  1: '1\ntesting capture\n',

#  2: '2\ntesting capture\n'}

Added by Sylvia Schmitt

