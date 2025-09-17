---
course: machine-learning-zoomcamp
id: e6d04a94b1
question: CUDA toolkit and cuDNN Install for Tensorflow
section: Miscellaneous
sort_order: 4080
---

Install Nvidia drivers: .

Windows:

Install Anaconda prompt

Two options:

Install package ‘tensorflow-gpu’ in Anaconda

Install the Tensorflow way

WSL/Linux:

WSL: Use the Windows Nvida drivers, do not touch that.

Two options:

Install the Tensorflow way

Make sure to follow step 4 to install CUDA by environment

Also run:

echo ‘export XLA_FLAGS=--xla_gpu_cuda_data_dir=$CONDA_PREFIX/lib/> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

Install CUDA toolkit 11.x.x

Install

Now you should be able to do training/inference with GPU in Tensorflow

(Learning in public links Links to social media posts where you share your progress with others (LinkedIn, Twitter, etc). Use #mlzoomcamp tag. The scores for this part will be capped at 7 points. Please make sure the posts are valid URLs starting with "https://" Does it mean that I should provide my linkedin link? or it means that I should write a post that I have completed my first assignement? (

ANS (by ezehcp7482@gmail.com): Yes, provide the linkedIN link to where you posted.

ezehcp7482@gmail.com:

PROBLEM: Since I had to put up a link to a public repository, I had to use Kaggle and uploading the dataset therein was a bit difficult; but I had to ‘google’ my way out.

ANS: See this link for a guide (https://www.kaggle.com/code/dansbecker/finding-your-files-in-kaggle-kernels/notebook)

