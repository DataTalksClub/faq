---
id: acf8fa5356
question: uv says Failed to hardlink files in Codespaces. Is it an error?
sort_order: 24
---

No. This warning can happen in GitHub Codespaces when `uv` cannot hardlink files between the cache and the target environment.

The package still installs. `uv` falls back to copying files.

To suppress the warning for the current shell:

```bash
export UV_LINK_MODE=copy
```

To make it persistent:

```bash
echo 'export UV_LINK_MODE=copy' >> ~/.bashrc
source ~/.bashrc
```

See the `uv` documentation for more details: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/).
