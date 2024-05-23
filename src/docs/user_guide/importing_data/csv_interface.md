[](){#csv}
# CSV interface

The fastest way to import data into the getML engine is to read it
directly from CSV files.

## Import from CSV

Using the [`from_csv()`][getml.data.DataFrame.from_csv] class method, you can
create a new [`DataFrame`][getml.data.DataFrame] based on a table stored in
the provided file(s). The [`read_csv()`][getml.data.DataFrame.read_csv]
method will replace the content of the current
[`DataFrame`][getml.data.DataFrame] instance or append further rows.

## Export to CSV

In addition to reading data from a CSV file, you can also write an
existing [`DataFrame`][getml.data.DataFrame] back into one using
[`to_csv()`][getml.data.DataFrame.to_csv].

