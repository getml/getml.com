[](){#greenplum}
# Greenplum interface

[Greenplum](https://greenplum.org/) is an open source database system maintained by Pivotal
Software, Inc. It can be connected to the getML engine using the
function [`connect_greenplum()`](getml/database/connect_greenplum). But first, make
sure your database is running, you have the corresponding hostname,
port as well as your user name and password ready, and you can reach
it from via your command line.

## Import from Greenplum

By selecting an existing table of your database in the
[`from_db()`](getml/data/DataFrame/from_db) class method, you can create a
new [`DataFrame`](getml/data/DataFrame) containing all its data.
Alternatively, you can use the [`read_db()`](getml/data/DataFrame/read_db)
and [`read_query()`](getml/data/DataFrame/read_query) methods to replace the
content of the current [`DataFrame`](getml/data/DataFrame) instance or
append further rows based on either a table or a specific query.

## Export to Greenplum

You can also write your results back into the Greenplum database. By
providing a name for the destination table in
[`Pipeline.transform()`](getml/pipeline/Pipeline/transform), the features generated
from your raw data will be written back. Passing it into
[`Pipeline.predict()`](getml/pipeline/Pipeline/predict) generates predictions
of the target variables to new, unseen data and stores the result into
the corresponding table.

