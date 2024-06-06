[](){#sqlite3}
# SQLite3 interface

[SQLite3](https://sqlite.org/index.html) is a popular in-memory database. It is faster than classical relational databases like PostgreSQL but less stable under massive parallel access. It requires all contained datasets to be loaded into memory, which might use up too much RAM, especially for large datasets.

As with all other databases in the unified import interface of the getML Python API, 
you first need to connect to it using [`connect_sqlite3()`][getml.database.connect_sqlite3.connect_sqlite3].

## Import from SQLite3

By selecting an existing table from your database in the [`DataFrame.from_db()`][getml.data.DataFrame.from_db] class method, you can create a new [`DataFrame`][getml.data.DataFrame] containing all its data.
Alternatively, you can use the [`read_db()`][getml.data.DataFrame.read_db] and [`read_query()`][getml.data.DataFrame.read_query] methods to replace the content of the current [`DataFrame`][getml.data.DataFrame] instance or append further rows based on either a table or a specific query.

## Export to SQLite3

You can also write your results back into the SQLite3 database. By providing a name for the destination table in [`transform()`][getml.pipeline.Pipeline.transform], the features generated from your raw data will be written back. Passing it into [`predict()`][getml.pipeline.Pipeline.predict] generates predictions of the target variables to new, unseen data and stores the result into the corresponding table.

