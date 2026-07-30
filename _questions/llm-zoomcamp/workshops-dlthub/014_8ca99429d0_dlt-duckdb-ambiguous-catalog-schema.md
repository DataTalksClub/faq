---
id: 8ca99429d0
question: How do I fix DuckDB's "Ambiguous reference to catalog or schema" error
  in a dlt pipeline?
sort_order: 14
---

When you use `destination="duckdb"`, dlt normally creates a database file named
after `pipeline_name` and a database schema named after `dataset_name`. If both
names are identical, DuckDB can't tell whether the unqualified name refers to
the catalog or the schema.

Give the pipeline and dataset different names:

```python
pipeline = dlt.pipeline(
    pipeline_name="agent_traces_pipeline",
    destination="duckdb",
    dataset_name="agent_traces",
)
```

You can also provide an explicit DuckDB file whose basename differs from the
dataset:

```python
pipeline = dlt.pipeline(
    pipeline_name="agent_traces",
    destination=dlt.destinations.duckdb("workshop.duckdb"),
    dataset_name="agent_traces",
)
```

If you already loaded data into another DuckDB file, point the destination at
that existing file rather than accidentally creating a new empty database.
