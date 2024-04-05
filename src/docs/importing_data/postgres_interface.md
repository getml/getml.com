# PostgreSQL interface

PostgreSQL is a powerful and well-established open source database system. It can be connected to the getML engine using the function [`connect_postgres()`](getml/database/connect_postgres). Make sure your database is running, you have the corresponding hostname, port, user name, and password ready, and you can reach it from your command line.

## Import from PostgreSQL

By selecting an existing table from your database in the [`DataFrame.from_db()`](getml/data/DataFrame/from_db) class method, you can create a new [`DataFrame`](getml/data/DataFrame) containing all its data.
Alternatively, you can use the [`read_db()`](getml/data/DataFrame/read_db) and [`read_query()`](getml/data/DataFrame/read_query) methods to replace the content of the current [`DataFrame`](getml/data/DataFrame) instance or append further rows based on either a table or a specific query.

## Export to PostgreSQL

You can also write your results back into the PostgreSQL database. If you provide a name for the destination table in [`transform()`](getml/pipeline/Pipeline/transform), the features generated from your raw data will be written back. Passing it into [`predict()`](getml/pipeline/Pipeline/predict) generates predictions of the target variables to new, unseen data and stores the result into the corresponding table.

[1]: https://www.postgresql.org/
