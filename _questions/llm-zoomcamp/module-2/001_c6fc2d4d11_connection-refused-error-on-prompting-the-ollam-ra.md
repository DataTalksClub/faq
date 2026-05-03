---
id: c6fc2d4d11
question: Connection refused error on prompting the ollam RAG?
sort_order: 1
---

If you encounter this error while doing the homework, you can resolve it by restarting the Ollama server using the following command:

```bash
!nohup ollama serve > nohup.out 2>&1 &
```

Make sure to rerun the cell containing `ollama serve` if you stop and restart the notebook cell.