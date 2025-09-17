---
id: bc8bd71f9c
question: How did I resolve the out of memory (OOM) issue when training my model on a GPU?
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 3000
---

To address the out of memory (OOM) issue, I followed these steps:

1. Check GPU Memory Usage:

I ran the following command to see how much memory was being used and which processes were occupying it:

!nvidia-smi

This command provided details about memory usage and active processes on the GPU.

2. Identify Active Processes:

From the output of nvidia-smi, I noticed that a Python process (...a3/envs/tensorflow2_p310/bin/python) was consuming a significant amount of GPU memory.

3. Terminate the Python Process:

I used the process ID (PID) to kill the Python process that was consuming the excessive memory. For example, to kill a process with PID 11208, I executed:

!kill 11208

4. Kernel Restart:

After terminating the process, I noticed that the kernel automatically restarted, freeing up the GPU memory.

5. Recheck GPU Memory:

I ran nvidia-smi again to confirm that the memory usage had decreased, and there were no longer any blocking processes.

By following these steps, I was able to free up GPU memory and continue training my model successfully.

(added by Karina)

