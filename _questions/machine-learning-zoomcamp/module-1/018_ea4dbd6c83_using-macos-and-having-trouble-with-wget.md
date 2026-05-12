---
id: ea4dbd6c83
question: Using macOS and having trouble with WGET
sort_order: 18
---

Wget doesn't ship with macOS, but you can use `curl` as an alternative.

Example command:

```bash
curl -o ./housing.csv https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv
```

- **curl**: A utility for retrieving information from the internet.
- **-o**: Specifies the output filename for the file being downloaded.
- **filename**: Your choice for naming the file.
- **URL**: The web address from which `curl` will download the data and save it using the specified filename.

For more information, you can refer to the [Curl Documentation](https://curl.se/docs/manpage.html)