---
title: Importing Data
---

[](){#importing-data}
# Importing data

Before being able to analyze and process your data using the getML Suite,
you have to import it into the engine. At the end of this step, you will have
your data in data frame objects in the getML engine and will be ready to
[annotate them][annotating-data].

!!! note

    If you have imported your data into the engine before and want to restore it,
    refer to [Python API: DataFrame][python-api-lifecycles]

[](){#importing-data-unified-interface}
## Unified import interface

The getML Python API provides a unified import interface requiring
similar arguments and resulting in the same output format, regardless
of the data source.

You can use one of the dedicated class methods (e.g. [`from_csv()`][getml.data.DataFrame.from_csv]) 
to construct a data frame object in the getML engine, fill it with the provided data, and retrieve 
a [`DataFrame`][getml.data.DataFrame] handle in the Python API.

!!! example
    Example demonstrating the use of [`from_csv()`][getml.data.DataFrame.from_csv]
    ```python
    data = getml.data.DataFrame.from_csv(
        "path/to/my/data.csv", 
        "my_data"
    )
    ```

If you already have a data frame object in place, you can use the methods of the corresponding 
[`DataFrame`][getml.data.DataFrame] handle (e.g. [`read_csv()`][getml.data.DataFrame.read_csv]) 
to either replace its content with new data or append to it.

All those functions also have their counterparts for exporting (e.g. [`to_csv()`][getml.data.DataFrame.to_csv]).

## Data Frames

The resulting [`DataFrame`][getml.data.DataFrame] instance in the Python
API represents a handle to the corresponding data frame object in the
getML engine. The mapping between the two is done based on
the name of the object, which has to be unique. Similarly, the names of 
the [`columns`][getml.data.columns] are required to be
unique within the data frame they are associated with.


## Handling of NULL values

Unfortunately, data sources often 
contain missing or corrupt data - also called NULL
values. getML is able to work with missing values except for the
[target variable][annotating-data-target], which must not
contain any NULL values (because having NULL targets does not
make any sense). Please refer to the section on 
[join keys][annotating-data-join-keys] for
details about their handling during the construction of the data
model.

During import, a NULL value is automatically inserted at all
occurrences of the strings "nan", "None", "NA", or an empty string as
well as at all occurrences of `None` and `NaN`.

## Import Formats

[](){#csv}
### **CSV**

The fastest way to import data into the getML engine is to read it
directly from CSV files.

Import from CSV

Using the [`from_csv()`][getml.data.DataFrame.from_csv] class method, you can
create a new [`DataFrame`][getml.data.DataFrame] based on a table stored in
the provided file(s). The [`read_csv()`][getml.data.DataFrame.read_csv]
method will replace the content of the current
[`DataFrame`][getml.data.DataFrame] instance or append further rows.

Export to CSV

In addition to reading data from a CSV file, you can also write an
existing [`DataFrame`][getml.data.DataFrame] back into one using
[`to_csv()`][getml.data.DataFrame.to_csv].

[](){#pandas}
### **Pandas**

[Pandas](https://pandas.pydata.org/) is one of the key packages used in most data science projects done in Python. The associated import interface is one of the slowest, but you can harness the good data exploration and manipulation capabilities of this Python package.

Import from Pandas

Using the [`DataFrame.from_pandas()`][getml.data.DataFrame.from_pandas] class method, you can create a new [`DataFrame`][getml.data.DataFrame] based on the provided `pandas.DataFrame`. The [`read_pandas()`][getml.data.DataFrame.read_pandas] method will replace the content of the current [`DataFrame`][getml.data.DataFrame] instance or append further rows.

Export to Pandas

In addition to reading data from a `pandas.DataFrame`, you can also write an existing [`DataFrame`][getml.data.DataFrame] back into a `pandas.DataFrame` using [`DataFrame.to_pandas()`][getml.data.DataFrame.to_pandas]. 

!!! note
    Due to the way data is stored within the getML engine, the dtypes of the original `pandas.DataFrame` cannot be restored properly and there might be inconsistencies in the order of microseconds being introduced into timestamps.

[](){#json}
### **JSON**

A convenient but slow way to import data into the getML engine via its Python API.

Import from JSON

Using the [`from_json()`][getml.data.DataFrame.from_json] class method, you
can create a new [`DataFrame`][getml.data.DataFrame] based on a JSON
string. The [`read_json()`][getml.data.DataFrame.read_json] method will
replace the content of the current [`DataFrame`][getml.data.DataFrame]
instance or append further rows.

Export to JSON

In addition to reading data from a JSON string, you can also convert an
existing [`DataFrame`][getml.data.DataFrame] into one using
[`to_json()`][getml.data.DataFrame.to_json].

[](){#sqlite3}
### **SQLite3**

[SQLite3](https://sqlite.org/index.html) is a popular in-memory database. It is faster than classical relational databases like PostgreSQL but less stable under massive parallel access. It requires all contained datasets to be loaded into memory, which might use up too much RAM, especially for large datasets.

As with all other databases in the unified import interface of the getML Python API, 
you first need to connect to it using [`connect_sqlite3()`][getml.database.connect_sqlite3.connect_sqlite3].

Import from SQLite3

By selecting an existing table from your database in the [`DataFrame.from_db()`][getml.data.DataFrame.from_db] class method, you can create a new [`DataFrame`][getml.data.DataFrame] containing all its data.
Alternatively, you can use the [`read_db()`][getml.data.DataFrame.read_db] and [`read_query()`][getml.data.DataFrame.read_query] methods to replace the content of the current [`DataFrame`][getml.data.DataFrame] instance or append further rows based on either a table or a specific query.

Export to SQLite3

You can also write your results back into the SQLite3 database. By providing a name for the destination table in [`transform()`][getml.pipeline.Pipeline.transform], the features generated from your raw data will be written back. Passing it into [`predict()`][getml.pipeline.Pipeline.predict] generates predictions of the target variables to new, unseen data and stores the result into the corresponding table.

[](){#mysql}
### **MySQL**

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

Import from MySQL

By selecting an existing table of your database in the [`DataFrame.from_db()`][getml.data.DataFrame.from_db] class method, you can create a new [`DataFrame`][getml.data.DataFrame] containing all its data.
Alternatively, you can use the [`read_db()`][getml.data.DataFrame.read_db] and [`read_query()`][getml.data.DataFrame.read_query] methods to replace the content of the current [`DataFrame`][getml.data.DataFrame] instance or append further rows based on either a table or a specific query.

Export to MySQL

You can also write your results back into the MySQL database. By providing a name for the destination table in [`transform()`][getml.pipeline.Pipeline.transform], the features generated from your raw data will be written back. Passing it into [`predict()`][getml.pipeline.Pipeline.predict] generates predictions of the target variables to new, unseen data and stores the result into the corresponding table.

[](){#mariadb}
### **MariaDB**

[MariaDB](https://mariadb.org/) is a popular open source fork of MySQL. It can be
connected to the getML engine using the function
[`connect_mariadb()`][getml.database.connect_mariadb.connect_mariadb]. But first, make sure your
database is running, you have the corresponding hostname, port as well
as your username and password ready, and you can reach it from your command line.

If you are unsure which port or socket your MariaDB is running
on, you can start the `mysql` command line interface 


```bash
$ mysql
```

Once inside the MariaDB interface, use the following queries to get the required insights:

```sql
MariaDB [(none)]> SELECT @@port;

MariaDB [(none)]> SELECT @@socket;
```

Import from MariaDB

By selecting an existing table of your database in the [`DataFrame.from_db()`][getml.data.DataFrame.from_db] class method, you can create a new [`DataFrame`][getml.data.DataFrame] containing all its data.
Alternatively, you can use the [`read_db()`][getml.data.DataFrame.read_db] and [`read_query()`][getml.data.DataFrame.read_query] methods to replace the content of the current [`DataFrame`][getml.data.DataFrame] instance or append further rows based on either a table or a specific query.

Export to MariaDB

You can also write your results back into the MariaDB database. By providing a name for the destination table in [`transform()`][getml.pipeline.Pipeline.transform], the features generated from your raw data will be written back. Passing it into [`predict()`][getml.pipeline.Pipeline.predict] generates predictions of the target variables to new, unseen data and stores the result into the corresponding table.

[](){#postgresql}
### **PostgreSQL**

[PostgreSQL](https://www.postgresql.org/) is a powerful and well-established open 
source database system. It can be connected to the getML engine using the function [`connect_postgres()`][getml.database.connect_postgres.connect_postgres]. Make sure your database is running, you have the corresponding hostname, port, user name, and password ready, and you can reach it from your command line.

Import from PostgreSQL

By selecting an existing table from your database in the [`DataFrame.from_db()`][getml.data.DataFrame.from_db] class method, you can create a new [`DataFrame`][getml.data.DataFrame] containing all its data.
Alternatively, you can use the [`read_db()`][getml.data.DataFrame.read_db] and [`read_query()`][getml.data.DataFrame.read_query] methods to replace the content of the current [`DataFrame`][getml.data.DataFrame] instance or append further rows based on either a table or a specific query.

Export to PostgreSQL

You can also write your results back into the PostgreSQL database. If you provide a name for the destination table in [`transform()`][getml.pipeline.Pipeline.transform], the features generated from your raw data will be written back. Passing it into [`predict()`][getml.pipeline.Pipeline.predict] generates predictions of the target variables to new, unseen data and stores the result into the corresponding table.

[](){#greenplum}
### **Greenplum**

!!! info "Enterprise Feature"
    This is an enterprise feature and not available in the community edition. Learn more about the [benefits][enterprise-benefits] and see the [comparion of features][enterprise-feature-list] between the community and enterprise edition.

[Greenplum](https://greenplum.org/) is an open source database system maintained by Pivotal
Software, Inc. It can be connected to the getML engine using the
function [`connect_greenplum()`][getml.database.connect_greenplum.connect_greenplum]. But first, make
sure your database is running, you have the corresponding hostname,
port as well as your user name and password ready, and you can reach
it from your command line.

Import from Greenplum

By selecting an existing table of your database in the
[`from_db()`][getml.data.DataFrame.from_db] class method, you can create a
new [`DataFrame`][getml.data.DataFrame] containing all its data.
Alternatively, you can use the [`read_db()`][getml.data.DataFrame.read_db]
and [`read_query()`][getml.data.DataFrame.read_query] methods to replace the
content of the current [`DataFrame`][getml.data.DataFrame] instance or
append further rows based on either a table or a specific query.

Export to Greenplum

You can also write your results back into the Greenplum database. By
providing a name for the destination table in
[`Pipeline.transform()`][getml.pipeline.Pipeline.transform], the features generated
from your raw data will be written back. Passing it into
[`Pipeline.predict()`][getml.pipeline.Pipeline.predict] generates predictions
of the target variables to new, unseen data and stores the result into
the corresponding table.

[](){#odbc}
### **ODBC**

!!! info "Enterprise Feature"
    This is an enterprise feature and not available in the community edition. Learn more about the [benefits][enterprise-benefits] and see the [comparion of features][enterprise-feature-list] between the community and enterprise edition.

[ODBC](https://docs.microsoft.com/en-us/sql/odbc/reference/what-is-odbc) (Open Database Connectivity) is an API specification for connecting software programming language to a database, developed by Microsoft.

In a nutshell, it works like this:

- Any database of relevance has an ODBC driver that translates calls from the ODBC API into a format the database can understand, returning the query results in a format understood by the ODBC API.
- To connect getML or other software to a database using ODBC, you first need to install the ODBC driver provided by your database vendor.
- In theory, ODBC drivers should translate queries from the SQL 99 standard into the SQL dialect, but this is often ignored in practice. Also, not all ODBC drivers support all ODBC calls.

With getML, native APIs are preferred for connecting to relational databases. ODBC is used when native APIs are not feasible due to licensing or other restrictions, especially for connecting to proprietary databases like Oracle, Microsoft SQL Server, or IBM DB2.

ODBC is pre-installed on modern Windows operating systems, while Linux and macOS can use open-source implementations like unixODBC and iODBC, with getML using unixODBC.

**An example: Microsoft SQL Server**

To connect to Microsoft SQL Server using ODBC:

1. If you do not have a Microsoft SQL Server instance, you can [download](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) a trial or development version.
2. Download the [ODBC driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server).
3. Configure the ODBC driver. Many drivers provide customized scripts for this, so manual configuration might not be necessary.

For Linux and macOS, create a `.odbc.ini` file in your home directory with the following contents:

```plaintext
[ANY-NAME-YOU-WANT]
Driver = /opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.5.so.2.1
Server = 123.45.67.890
Port = 1433
User = YOUR-USERNAME
Password = YOUR-PASSWORD
Database = YOUR-DATABASE
Language = us_english
NeedODBCTypesOnly = 1
```
On **Docker**, you can make appropriate changes to the Dockerfile and then rerun `./setup.sh` or `bash setup.sh`.

You will need to set the following parameters:

- The first line is the *server name* or *data source name*. You can use this name to tell getML that this is the server you want to connect to.
- The *Driver* is the location of the ODBC driver you have just downloaded. The location or file name might be different on your system.
- The *Server* is the IP address of the server. If the server is on the same machine as getML, just write "localhost".
- The *Port* is the port on which to connect the server. The default port for SQL Server is 1433.
- *User* and *Password* are the user name and password that allow access to the server.
- The *Database* is the database inside the server you want to connect to.

You can now connect getML to the database:

```python
getml.database.connect_odbc(
    server_name="ANY-NAME-YOU-WANT",
    user="YOUR-USERNAME",
    password="YOUR-PASSWORD",
    escape_chars="[]")
```

**Important: Always pass *escape_chars***

Earlier we mentioned that ODBC drivers are *supposed* to translate standard SQL queries into the specific SQL dialects, but this requirement is often ignored.

A typical issue is *escape characters*, needed when the names of your schemas, tables, or columns are SQL keywords, like the loans dataset containing a table named *ORDER*.

To avoid this problem, you can envelop the schema, table, and column names in *escape characters*. 
```sql
SELECT "some_column" FROM "SOME_SCHEMA"."SOME_TABLE";
```
getML always uses escape characters for its automatically generated queries.

The SQL standard requires that the quotation mark (") be used as the escape character. However, many SQL dialects do not follow this requirement, e.g., SQL Server uses "[]":

```sql
SELECT [some_column] FROM [SOME_SCHEMA].[SOME_TABLE];
```
MySQL and MariaDB work like this:
```sql
SELECT `some_column` FROM `SOME_SCHEMA`.`SOME_TABLE`;
```
To avoid frustration, determine your server's escape characters and explicitly pass 
them to [`connect_odbc()`][getml.database.connect_odbc.connect_odbc].

Import data using ODBC

By selecting an existing table from your database in the [`DataFrame.from_db()`][getml.data.DataFrame.from_db] class method, you can create a new [`DataFrame`][getml.data.DataFrame] containing all its data.
Alternatively, you can use the [`read_db()`][getml.data.DataFrame.read_db] and [`read_query()`][getml.data.DataFrame.read_query] methods to replace the content of the current [`DataFrame`][getml.data.DataFrame] instance or append further rows based on either a table or a specific query.

Export data using ODBC

You can also write your results back into the database using ODBC. When you provide a name for the destination table in [`transform()`][getml.pipeline.Pipeline.transform], the features generated from your raw data will be written back. Passing it into [`predict()`][getml.pipeline.Pipeline.predict] generates predictions of the target variables to new, unseen data and stores the result into the corresponding table.
