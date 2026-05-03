---
id: d07a9a8ff9
question: 'Why does DuckDB show “IO Error: Could not set lock on file” after pressing
  Ctrl+Z in Ubuntu, and how can it be fixed?'
sort_order: 9
---

Pressing `Ctrl+Z` while running:
```
duckdb data.duckdb
```
does not exit DuckDB.
It only suspends the process and returns to the shell. The DuckDB process continues running in the background and still holds a lock on the database file.
When running:
```
duckdb data.duckdb
```
gain, the message appears:
```
IO Error: Could not set lock on file
```
because the original suspended process still owns the file lock.
How to fix it:
* Option 1, resume and exit properly
1. Bring the suspended process back to the foreground:
```
fg
```
2. Exit DuckDB properly:
```
.exit
```
or press:
```
Ctrl+D
```
* Option 2, kill the DuckDB process
1. Check the running DuckDB process:
```
ps -Af | grep duckdb
```
Example output:
```
demo    33251    3667  0 08:21 pts/0    00:00:00 duckdb taxi_rides_ny.duckdb
```
The process ID (PID) is `33251`.
2. Kill the process:
```
kill -9 33251
```
This releases the file lock.