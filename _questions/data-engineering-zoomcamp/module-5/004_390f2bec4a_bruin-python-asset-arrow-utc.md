---
id: 390f2bec4a
question: 'Bruin Python asset fails with ArrowInvalid: Cannot locate timezone ''UTC'':
  Timezone database not found'
sort_order: 4
---

Cause: On Windows, PyArrow has no built-in timezone database. When dlt/ingestr receives a DataFrame with naive (tz-unaware) timestamp columns, it calls pyarrow.compute.assume_timezone("UTC") internally to annotate them — which requires a tzdata file on disk. If that file isn't where PyArrow expects it, the pipeline crashes even if tzdata is listed in your requirements.txt (that package only installs into the asset container, not the host ingestr environment).

Solution: Return timestamps that are already tz-aware UTC from your materialize() function. When columns arrive with timezone info already set, dlt skips the assume_timezone call entirely.
```python
for col in df.columns:
    if pd.api.types.is_datetime64_any_dtype(df[col]):
        if hasattr(df[col].dt, "tz") and df[col].dt.tz is None:
            df[col] = df[col].dt.tz_localize("UTC")
        else:
            df[col] = df[col].dt.tz_convert("UTC")
        # microsecond precision avoids ns-overflow and is what pyarrow prefers
        df[col] = df[col].astype("datetime64[us, UTC]")

df["extracted_at"] = pd.Timestamp.now("UTC").floor("us")
```

Also bump pyarrow to 14+ in `requirements.txt` — `datetime64[us, UTC]` as a pandas dtype was stabilised there:
```
pyarrow==15.0.2
tzdata==2024.1
```
