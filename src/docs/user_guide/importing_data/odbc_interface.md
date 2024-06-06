[](){#odbc}
# ODBC interface

[ODBC](https://docs.microsoft.com/en-us/sql/odbc/reference/what-is-odbc) (Open Database Connectivity) is an API specification for connecting software programming language to a database, developed by Microsoft.

In a nutshell, it works like this:

- Any database of relevance has an ODBC driver that translates calls from the ODBC API into a format the database can understand, returning the query results in a format understood by the ODBC API.
- To connect getML or other software to a database using ODBC, you first need to install the ODBC driver provided by your database vendor.
- In theory, ODBC drivers should translate queries from the SQL 99 standard into the SQL dialect, but this is often ignored in practice. Also, not all ODBC drivers support all ODBC calls.

At getML, native APIs are preferred for connecting to relational databases. ODBC is used when native APIs are not feasible due to licensing or other restrictions, especially for connecting to proprietary databases like Oracle, Microsoft SQL Server, or IBM DB2.

ODBC is pre-installed on modern Windows operating systems, while Linux and macOS can use open-source implementations like unixODBC and iODBC, with getML using unixODBC.

## An example: Microsoft SQL Server

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

## Important: Always pass *escape_chars*

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

## Import data using ODBC

By selecting an existing table from your database in the [`DataFrame.from_db()`][getml.data.DataFrame.from_db] class method, you can create a new [`DataFrame`][getml.data.DataFrame] containing all its data.
Alternatively, you can use the [`read_db()`][getml.data.DataFrame.read_db] and [`read_query()`][getml.data.DataFrame.read_query] methods to replace the content of the current [`DataFrame`][getml.data.DataFrame] instance or append further rows based on either a table or a specific query.

## Export data using ODBC

You can also write your results back into the database using ODBC. When you provide a name for the destination table in [`transform()`][getml.pipeline.Pipeline.transform], the features generated from your raw data will be written back. Passing it into [`predict()`][getml.pipeline.Pipeline.predict] generates predictions of the target variables to new, unseen data and stores the result into the corresponding table.



