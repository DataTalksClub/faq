---
id: a250f11737
question: What is the fastest way to upload taxi data to dbt-postgres?
sort_order: 55
---

Use the PostgreSQL `COPY FROM` feature, which is compatible with CSV files.

### Steps:

1. **Create the Table**
   
   First, create your table (example):
   
   ```sql
   CREATE TABLE taxis (
   
   …
   
   );
   ```

2. **Use COPY Functionality**

   Use the `COPY` command (example):

   ```sql
   COPY taxis FROM PROGRAM
   'url'
   WITH (
   FORMAT csv,
   HEADER true,
   ENCODING utf8
   );
   ```

   - Syntax for `COPY`:

   ```sql
   COPY table_name [ ( column_name [, ...] ) ]
   FROM { 'filename' | PROGRAM 'command' | STDIN }
   [ [ WITH ] ( option [, ...] ) ]
   [ WHERE condition ]
   ```