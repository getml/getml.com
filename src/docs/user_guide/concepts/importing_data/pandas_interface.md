[](){#pandas}
# Pandas interface

[Pandas](https://pandas.pydata.org/) is one of the key packages used in most data science projects done in Python. The associated import interface is one of the slowest, but you can harness the good data exploration and manipulation capabilities of this Python package.

## Import from Pandas

Using the [`DataFrame.from_pandas()`][getml.data.DataFrame.from_pandas] class method, you can create a new [`DataFrame`][getml.data.DataFrame] based on the provided `pandas.DataFrame`. The [`read_pandas()`][getml.data.DataFrame.read_pandas] method will replace the content of the current [`DataFrame`][getml.data.DataFrame] instance or append further rows.

## Export to Pandas

In addition to reading data from a `pandas.DataFrame`, you can also write an existing [`DataFrame`][getml.data.DataFrame] back into a `pandas.DataFrame` using [`DataFrame.to_pandas()`][getml.data.DataFrame.to_pandas]. 

!!! note
    Due to the way data is stored within the getML engine, the dtypes of the original `pandas.DataFrame` cannot be restored properly and there might be inconsistencies in the order of microseconds being introduced into timestamps.
