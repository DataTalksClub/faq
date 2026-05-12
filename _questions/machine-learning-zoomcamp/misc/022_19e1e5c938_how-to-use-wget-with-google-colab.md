---
id: 19e1e5c938
question: How to use wget with Google Colab?
sort_order: 22
---

To use `wget` in Google Colab, follow these steps:

1. **Install wget**: Ensure that `wget` is installed by running the following command:
   
   ```bash
   !which wget
   ```

2. **Download Data**: Use `wget` to download files by specifying the URL and destination path:
   
   ```bash
   !wget -P /content/drive/My\ Drive/Downloads/ URL
   ```