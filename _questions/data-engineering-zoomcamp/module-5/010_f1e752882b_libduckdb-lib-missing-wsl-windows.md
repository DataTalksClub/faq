---
id: f1e752882b
question: 'libduckdb.so: cannot open shared object file error when running Bruin with
  DuckDB on Windows 10 / WSL Ubuntu 24.04'
sort_order: 10
---

The error occurs because the system cannot locate the DuckDB shared library. Resolve by downloading and moving the library to the system's library path:

```bash
# 1. Download the Linux AMD64 shared library
wget https://github.com/duckdb/duckdb/releases/download/v1.1.3/libduckdb-linux-amd64.zip

# 2. Unzip the package
unzip libduckdb-linux-amd64.zip

# 3. Move the library to a standard system location
sudo mv libduckdb.so /usr/local/lib/

# 4. Refresh the library cache
sudo ldconfig
```
