[](){#annotating-data}
# Annotating data

After you have [imported][importing-data] your data into the getML engine, there is one more step to undertake before you can start learning features: You need to assign a **role** to each column. Why is that?

First, the general structure of the individual data frames is needed to construct the [relational data model][data-model]. This is done by assigning the roles [join key][annotating-data-join-keys] and [time stamp][annotating-data-time-stamp]. The former defines the columns that are used to join different data frames, the latter ensures that only rows in a reasonable time frame are taken into account (otherwise there might be data leaks).

Second, you need to tell the [feature learning algorithm][feature-engineering] how to interpret the individual columns for it to construct sophisticated features. That is why we need the roles [numerical][annotating-data-numerical], [categorical][annotating-data-categorical], and [target][annotating-data-target]. You can also assign [units][annotating-data-units] to each column in a Data Frame.

This chapter contains detailed information on the individual [roles][annotating-data-roles] and [units][annotating-data-units].

## In short

When **building the data model**, you should keep the following things in mind:
- Every [`DataFrame`][getml.data.data_frame] in a data model needs to have at least one column ([`columns`][getml.data.columns]) with the role [join key][annotating-data-join-keys].
- The role [time stamp][annotating-data-time-stamp] has to be used to prevent data leaks (refer to [data model time series][data-model-time-series] for details).

When **learning features**, please keep the following things in mind:

- Only [`columns`][getml.data.columns] with roles of [categorical][annotating-data-categorical], [numerical][annotating-data-numerical], and [time stamp][annotating-data-time-stamp] will be used by the feature learning algorithm for aggregations or conditions, unless you explicitly tell it to aggregate [target][annotating-data-target] columns as well (refer to `allow_lagged_target` in [`join()`][getml.data.Placeholder.join]).
- Columns are only compared with each other if they have the same [unit][annotating-data-units].
- If you want to make sure that a column is *only* used for comparison, you can set `comparison_only` (refer to [annotating units][annotating-data-units]). Time stamps are automatically set to `comparison_only`.

[](){#annotating-data-roles}
## Roles
Roles determine if and how [`columns`][getml.data.columns] are handled during the construction of the [data model][data-model] and how they are interpreted by the [feature learning algorithm][feature-engineering]. The following roles are available in getML:

| Role                | Class                                             | Included in FL algorithm |
|---------------------|---------------------------------------------------|--------------------------|
| [`categorical`][getml.data.roles.categorical]       | [`StringColumn`][getml.data.columns.StringColumn] | yes                      |
| [`numerical`][getml.data.roles.numerical]         | [`FloatColumn`][getml.data.columns.FloatColumn]   | yes                      |
| [`text`][getml.data.roles.text]              | [`StringColumn`][getml.data.columns.StringColumn] | yes                      |
| [`time_stamp`][getml.data.roles.time_stamp]        | [`FloatColumn`][getml.data.columns.FloatColumn]   | yes                      |
| [`join_key`][getml.data.roles.join_key]          | [`StringColumn`][getml.data.columns.StringColumn] | no                       |
| [`target`][getml.data.roles.target]            | [`FloatColumn`][getml.data.columns.FloatColumn]   | not by default           |
| [`unused_float`][getml.data.roles.unused_float]      | [`FloatColumn`][getml.data.columns.FloatColumn]   | no                       |
| [`unused_string`][getml.data.roles.unused_string]     | [`StringColumn`][getml.data.columns.StringColumn] | no                       |

When constructing a [`DataFrame`][getml.data.DataFrame] via the class methods [`from_csv`][getml.data.DataFrame.from_csv], [`from_pandas`][getml.data.DataFrame.from_pandas], [`from_db`][getml.data.DataFrame.from_db], and [`from_json`][getml.data.DataFrame.from_json], all [`columns`][getml.data.columns] will have either the role [unused float][annotating-data-unused-float] or [unused string][annotating-data-unused-string]. Unused columns will be ignored by the feature learning and machine learning (ML) algorithms.

```python
import pandas as pd
data_df = dict(
    animal=["hawk", "parrot", "goose"],
    votes=[12341, 5127, 65311],
    weight=[12.14, 12.6, 11.92],
    animal_id=[123, 512, 671],
    date=["2019-05-02", "2019-02-28", "2018-12-24"]
)
pandas_df = pd.DataFrame(data=data_df)
getml_df = getml.data.DataFrame.from_pandas(pandas_df, name='animal elections')

getml_df
# Output:
# | votes        | weight       | animal_id    | animal        | date          |
# | unused float | unused float | unused float | unused string | unused string |
# ------------------------------------------------------------------------------
# | 12341        | 12.14        | 123          | hawk          | 2019-05-02    |
# | 5127         | 12.6         | 512          | parrot        | 2019-02-28    |
# | 65311        | 11.92        | 671          | goose         | 2018-12-24    |
```

To make use of the imported data, you have to tell getML how you intend to use each column by assigning a role ([`roles`][getml.data.roles]). This is done by using the [`set_role`][getml.data.DataFrame.set_role] method of the [`DataFrame`][getml.data.DataFrame]. Each column must have exactly one role. If you wish to use a column in two different roles, you have to add it twice and assign each copy a different role.

```python
getml_df.set_role(['animal_id'], getml.data.roles.join_key)
getml_df.set_role(['animal'], getml.data.roles.categorical)
getml_df.set_role(['votes', 'weight'], getml.data.roles.numerical)
getml_df.set_role(['date'], getml.data.roles.time_stamp)    
getml_df
# Output:
# | date                        | animal_id | animal      | votes     | weight    |
# | time stamp                  | join key  | categorical | numerical | numerical |
# ---------------------------------------------------------------------------------
# | 2019-05-02T00:00:00.000000Z | 123       | hawk        | 12341     | 12.14     |
# | 2019-02-28T00:00:00.000000Z | 512       | parrot      | 5127      | 12.6      |
# | 2018-12-24T00:00:00.000000Z | 671       | goose       | 65311     | 11.92     |
```
When assigning new roles to existing columns, you might notice that some of
these calls are completed in an instance while others might take a considerable
amount of time. What's happening here? A column's role also determines its type. 
When you set a new role, an implicit type conversion might take place.

## A note on reproducibility and efficiency

When building a stable pipeline you want to deploy in a productive environment, the flexible default behavior of the import interface might be more of an obstacle. For instance, CSV files are not type-safe. A column that was interpreted as a float column for one set of files might be interpreted as a string column for a different set of files. This obviously has implications for the stability of your pipeline. Therefore, it might be a good idea to hard-code column roles.

In the getML Python API, you can bypass the default deduction of the role of each column by providing a dictionary mapping each column name to a role in the import interface.

```python
roles = {"categorical": ["colname1", "colname2"], "target": ["colname3"]}
df_expd = getml.data.DataFrame.from_csv(
    fnames=["file1.csv", "file2.csv"],
    name="MY DATA FRAME",
    sep=';',
    quotechar='"',
    roles=roles,
    ignore=True
)
```
If the `ignore` argument is set to `True`, any columns missing in the dictionary won't be imported at all.

If you feel that writing the roles by hand is too tedious, you can use `dry`: If you call the import interface while setting the `dry` argument to `True`, no data is read. Instead, the default roles of all columns will be returned as a dictionary. You can store, alter, and hard-code this dictionary into your stable pipeline.

```python
roles = getml.data.DataFrame.from_csv(
    fnames=["file1.csv", "file2.csv"],
    name="MY DATA FRAME",
    sep=';',
    quotechar='"',
    dry=True                                     
)
```
Even if your data source is type safe, setting roles is still a good idea because it is also more efficient. Using [`set_role()`][getml.data.DataFrame.set_role] creates a deep copy of the original column and might perform an implicit type conversion. If you already know where you want your data to end up, it might be a good idea to set roles in advance.
[](){#annotating-data-join-keys}
## Join key

Join keys are required to establish a relation between two [`DataFrame`][getml.data.DataFrame] objects. Please refer to the [data models][data-model] for details.

The content of this column is allowed to contain NULL values. NULL values won't be matched to anything, not even to NULL values in other join keys.

[`columns`][getml.data.columns] of this role will *not* be aggregated by the feature learning algorithm or used for conditions.
[](){#annotating-data-time-stamp}
## Time stamp

This role is used to prevent data leaks. When you join one table onto another, you usually want to make sure that no data from the future is used. Time stamps can be used to limit your joins.

In addition, the feature learning algorithm can aggregate time stamps or use them for conditions. However, they will not be compared to fixed values unless you explicitly change their units. This means that conditions like this are not possible by default:

```sql
WHERE time_stamp > some_fixed_date
```
Instead, time stamps will always be compared to other time stamps:

```sql
WHERE time_stamp1 - time_stamp2 > some_value
```
This is because it is unlikely that comparing time stamps to a fixed date performs
well out-of-sample.

When assigning the role time stamp to a column that is currently a 
[`StringColumn`][getml.data.StringColumn], 
you need to specify the format of this string. You can do so by using 
the `time_formats` argument of
[`set_role()`][getml.data.DataFrame.set_role]. You can pass a list of time formats
that is used to try to interpret the input strings. Possible format options are


* %w - abbreviated weekday (Mon, Tue, ...)
* %W - full weekday (Monday, Tuesday, ...)
* %b - abbreviated month (Jan, Feb, ...)
* %B - full month (January, February, ...)
* %d - zero-padded day of month (01 .. 31)
* %e - day of month (1 .. 31)
* %f - space-padded day of month ( 1 .. 31)
* %m - zero-padded month (01 .. 12)
* %n - month (1 .. 12)
* %o - space-padded month ( 1 .. 12)
* %y - year without century (70)
* %Y - year with century (1970)
* %H - hour (00 .. 23)
* %h - hour (00 .. 12)
* %a - am/pm
* %A - AM/PM
* %M - minute (00 .. 59)
* %S - second (00 .. 59)
* %s - seconds and microseconds (equivalent to %S.%F)
* %i - millisecond (000 .. 999)
* %c - centisecond (0 .. 9)
* %F - fractional seconds/microseconds (000000 - 999999)
* %z - time zone differential in ISO 8601 format (Z or +NN.NN)
* %Z - time zone differential in RFC format (GMT or +NNNN)
* %% - percent sign 

If none of the formats works, the getML engine will try to interpret
the time stamps as numerical values. If this fails, the time stamp will be set
to NULL.
```python
data_df = dict(
date1=[getml.data.time.days(365), getml.data.time.days(366), getml.data.time.days(367)],
date2=['1971-01-01', '1971-01-02', '1971-01-03'],
date3=['1|1|71', '1|2|71', '1|3|71'],
)
df = getml.data.DataFrame.from_dict(data_df, name='dates')
df.set_role(['date1', 'date2', 'date3'], getml.data.roles.time_stamp, time_formats=['%Y-%m-%d', '%n|%e|%y'])
df
# | date1                       | date2                       | date3                       |
# | time stamp                  | time stamp                  | time stamp                  |
# -------------------------------------------------------------------------------------------
# | 1971-01-01T00:00:00.000000Z | 1971-01-01T00:00:00.000000Z | 1971-01-01T00:00:00.000000Z |
# | 1971-01-02T00:00:00.000000Z | 1971-01-02T00:00:00.000000Z | 1971-01-02T00:00:00.000000Z |
# | 1971-01-03T00:00:00.000000Z | 1971-01-03T00:00:00.000000Z | 1971-01-03T00:00:00.000000Z |
```
!!! note 

    getML time stamps are actually floats expressing the number of seconds since 
    UNIX time (1970-01-01T00:00:00).


[](){#annotating-data-target}
## Target

The associated [`columns`][getml.data.columns] contain the variables we want to predict. They are not used by the feature learning algorithm unless we explicitly tell it to do so (refer to `allow_lagged_target` in [`join()`][getml.data.Placeholder.join]). However, they are such an important part of the analysis that the population table is required to contain at least one of them (refer to [data model tables][data-model-tables]).

The content of the target columns needs to be numerical. For classification problems, target variables can only assume the values 0 or 1. Target variables can never be `NULL`.
[](){#annotating-data-numerical}
## Numerical

This role tells the getML engine to include the associated [`FloatColumn`][getml.data.columns.FloatColumn] during the feature learning.

It should be used for all data with an inherent ordering, regardless of whether it is sampled from a continuous quantity, like passed time or the total amount of rainfall, or a discrete one, like the number of sugary mulberries one has eaten since lunch.
[](){#annotating-data-categorical}
## Categorical

This role tells the getML engine to include the associated [`StringColumn`][getml.data.columns.StringColumn] during feature learning.

It should be used for all data with no inherent ordering, even if the categories are encoded as integers instead of strings.
[](){#annotating-data-text}
## Text

getML provides the role [`text`][getml.data.roles.text] to annotate free form text fields within relational data structures. getML deals with columns of role [`text`][getml.data.roles.text] through one of two approaches: Text fields can either be integrated into features by learning conditions based on the mere presence (or absence) of certain words in those text fields (the default) or they can be split into a relational bag-of-words representation by means of the [`TextFieldSplitter`][getml.preprocessors.TextFieldSplitter] preprocessor. For more information on getML's handling of text fields, refer to [the Preprocessing section][preprocessing-free-form-text]
[](){#annotating-data-unused-float}
## Unused_float

Marks a [`FloatColumn`][getml.data.columns.FloatColumn] as unused.

The associated columns will be neither used for the data model nor by the feature learning algorithms and predictors.
[](){#annotating-data-unused-string}
## Unused_string

Marks a [`StringColumn`][getml.data.columns.StringColumn] as unused.

The associated columns will be neither used for the data model nor by the feature learning algorithms and predictors.
[](){#annotating-data-units}
## Units

By default, all columns of role [categorical][annotating-data-categorical] or [numerical][annotating-data-numerical] will only be compared to fixed values.

```sql
...
WHERE numerical_column > some_value 
OR categorical_column == 'some string'
...
```
If you want the feature learning algorithms to
compare these columns with each other (like in the snippet below), 
you have to explicitly set a unit. 


```sql
...
WHERE numerical_column1 - numerical_column2 > some_value
OR categorical_column1 != categorical_column2
...

```
Using [`set_unit()`][getml.data.DataFrame.set_unit] you can set the *unit* of
a column to an arbitrary, non-empty string. If it matches the string
of another column, both of them will be compared by the getML
engine. Please note that a column can not have more than one unit.

There are occasions where *only* a pairwise comparison of columns but
not a comparison with fixed values is useful. To cope with this problem,
you can set the `comparison_only` flag in
[`set_unit()`][getml.data.DataFrame.set_unit].

!!! note

    Note that time stamps are used for comparison only by default. The feature 
    learning algorithm will not compare them to a fixed date, because
    it is very unlikely that such a feature would perform well out-of-sample.

