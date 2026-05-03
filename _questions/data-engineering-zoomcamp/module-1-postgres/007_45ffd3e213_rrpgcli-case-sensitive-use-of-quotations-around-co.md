---
id: 45ffd3e213
question: 'RRPGCLI: Case sensitive use of “Quotations” around columns with capital
  letters'
sort_order: 7
---

`PULocationID` will not be recognized, but `"PULocationID"` will be. This is because unquoted identifiers are case insensitive. [See docs](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS).