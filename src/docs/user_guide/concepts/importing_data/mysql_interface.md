[](){#mysql}
# MySQL interface

[MySQL](https://www.mysql.com) is one of the most popular databases in use today. It 
can be connected to the getML engine using the function [`connect_mysql()`][getml.database.connect_mysql.connect_mysql]. But first, make sure your database is running, you have the corresponding hostname, port as well as your user name and password ready, and you can reach it from via your command line.

If you are unsure which port or socket your MySQL is running on, you can start the `mysql` command line interface
```bash
$ mysql

```

Once inside the MySQL interface, use the following queries to get the required insights:
```sql
> SELECT @@port;

> SELECT @@socket;
```

## Import from MySQL

By selecting an existing table of your database in the [`DataFrame.from_db()`][getml.data.DataFrame.from_db] class method, you can create a new [`DataFrame`][getml.data.DataFrame] containing all its data.
Alternatively, you can use the [`read_db()`][getml.data.DataFrame.read_db] and [`read_query()`][getml.data.DataFrame.read_query] methods to replace the content of the current [`DataFrame`][getml.data.DataFrame] instance or append further rows based on either a table or a specific query.

## Export to MySQL

You can also write your results back into the MySQL database. By providing a name for the destination table in [`transform()`][getml.pipeline.Pipeline.transform], the features generated from your raw data will be written back. Passing it into [`predict()`][getml.pipeline.Pipeline.predict] generates predictions of the target variables to new, unseen data and stores the result into the corresponding table.
