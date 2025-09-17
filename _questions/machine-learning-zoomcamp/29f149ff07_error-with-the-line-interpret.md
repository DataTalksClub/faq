---
course: machine-learning-zoomcamp
id: 29f149ff07
question: Error with the line “interpreter.set_tensor(input_index, X”)
section: 9. Serverless Deep Learning
sort_order: 3170
---

I had this error when running the command line : interpreter.set_tensor(input_index, x) that can be seen in the video 9.3 around 12 minutes.

ValueError: Cannot set tensor: Got value of type UINT8 but expected type FLOAT32 for input 0, name: serving_default_conv2d_input:0

This is because the X is an int but a float is expected.

Solution:

I found this solution from this question here  :

# Need to convert to float32 before set_tensor

X = np.float32(X)

Then, it works. I work with tensorflow 2.15.0, maybe the fact that this version is more recent involves this change ?

Added by Mélanie Fouesnard

