---
id: e3c5c81223
question: Running ‘nvidia-smi’ in a loop without using ‘watch’
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 2950
---

The command ‘nvidia-smi’ has a built-in function which will run it in subsequently updating it every N seconds without the need of using the command ‘watch’.

nvidia-smi -l <N seconds>

The following command will run ‘nvidia-smi’ every 2 seconds until interrupted using CTRL+C.

nvidia-smi -l 2

Added by Sylvia Schmitt

