---
id: c4ad81910b
question: Install Docker (udocker) in Google Colab
sort_order: 30
---

To work with Docker in Google Colab, follow these steps:

1. Open your Google Colab notebook.
2. Run the following commands:

   ```bash
   %%shell
   pip install udocker
   udocker --allow-root install
   ```

3. Test the installation:

   ```bash
   !udocker --allow-root run hello-world
   ```

For more details, refer to this [gist](https://gist.github.com/mwufi/6718b30761cd109f9aff04c5144eb885).