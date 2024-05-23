[](){#mariadb}
# MariaDB interface

[MariaDB](https://mariadb.org/) is a popular open source fork of MySQL. It can be
connected to the getML engine using the function
[`connect_mariadb()`][getml.database.connect_mariadb]. But first, make sure your
database is running, you have the corresponding hostname, port as well
as your username and password ready, and you can reach it from your command line.

If you are unsure which port or socket your MariaDB is running
on, you can start the `mysql` command line interface 


```bash
$ mysql
```
and use the following queries to get the required insights.

```sql
MariaDB [(none)]> SELECT @@port;

MariaDB [(none)]> SELECT @@socket;
```

# Import from MariaDB

By selecting an existing table of your database in the [`DataFrame.from_db()`][getml.data.DataFrame.from_db] class method, you can create a new [`DataFrame`][getml.data.DataFrame] containing all its data.
Alternatively, you can use the [`read_db()`][getml.data.DataFrame.read_db] and [`read_query()`][getml.data.DataFrame.read_query] methods to replace the content of the current [`DataFrame`][getml.data.DataFrame] instance or append further rows based on either a table or a specific query.

# Export to MariaDB

You can also write your results back into the MariaDB database. By providing a name for the destination table in [`transform()`][getml.pipeline.Pipeline.transform], the features generated from your raw data will be written back. Passing it into [`predict()`][getml.pipeline.Pipeline.predict] generates predictions of the target variables to new, unseen data and stores the result into the corresponding table.

