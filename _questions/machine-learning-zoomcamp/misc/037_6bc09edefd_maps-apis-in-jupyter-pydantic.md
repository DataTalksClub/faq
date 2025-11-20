---
id: 6bc09edefd
question: How I use maps APIs in Pydantic, Jupyter?
sort_order: 37
---

To install bibl.
```python
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import base64
# Pre-carrega ícones em base64 (cache)
icon_cache = {}
for brand_key, filename in icon_mapping.items():
    icon_path = ICONS_DIR / filename
    if icon_path.exists():
        with open(icon_path, 'rb') as f:
            img_data = base64.b64encode(f.read()).decode()
        ext = icon_path.suffix.lower()
        mime = 'image/jpeg' if ext in ['.jpg', '.jpeg'] else 'image/png'
        icon_url = f'data:{mime};base64,{img_data}'
        icon_cache[brand_key] = folium.CustomIcon(
            icon_url,
            icon_size=(32, 32),
            icon_anchor=(16, 32),
            popup_anchor=(0, -32)
        )

def color_for_brand(b):
    s = str(b or "")
    for k, v in palette.items():
        if k.lower() in s.lower():
            return v
    return "#555555"

def icon_for_brand(b):
    s = str(b or "")
    for k in icon_cache.keys():
        if k.lower() in s.lower():
            return icon_cache[k]
    return None
# Mapa base
m = folium.Map(
    location=[df[lat].mean(), df[lon].mean()],
    zoom_start=11,
    tiles="CartoDB positron"
)
``` 