---
id: b024daf322
question: Which type of SQL is used in Spark? Postgres? MySQL? SQL Server?
sort_order: 19
---

Spark uses its own type of SQL, known as Spark SQL.

The SQL syntax across various providers is generally similar, as shown below:

```sql
SELECT [attributes]
FROM [table]
WHERE [filter]
GROUP BY [grouping attributes]
HAVING [filtering the groups]
ORDER BY [attribute to order]
(INNER/FULL/LEFT/RIGHT) JOIN [table2]
ON [attributes table joining table2] (...)
```

What differs most between SQL providers are the built-in functions.

For built-in Spark SQL functions, check this link: [Spark SQL Functions](https://spark.apache.org/docs/latest/api/sql/index.html)

Extra information on Spark SQL:

[What is Spark SQL?](https://databricks.com/glossary/what-is-spark-sql#:~:text=Spark%20SQL%20is%20a%20Spark,on%20existing%20deployments%20and%20data)