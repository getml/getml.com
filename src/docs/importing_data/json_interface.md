# JSON interface

The another convenient but slow way to import data into the getML
engine via its Python API.

## Import from JSON

Using the [`from_json()`](getml/data/DataFrame/from_json) class method, you
can create a new [`DataFrame`](getml/data/DataFrame) based on a JSON
string. The [`read_json()`](getml/data/DataFrame/read_json) method will
replace the content of the current [`DataFrame`](getml/data/DataFrame)
instance or append further rows.

## Export to JSON

In addition to reading data from a JSON string, you can also convert an
existing [`DataFrame`](getml/data/DataFrame) into one using
[`to_json()`](getml/data/DataFrame/to_json).
