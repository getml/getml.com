[](){#annotating-data}
# Annotating data

After you have [imported][importing-data] your data into the getML engine, there is one more step to undertake before you can start learning features: You need to assign a **role** to each column. Why is that?

First, the general structure of the individual data frames is needed to construct the [relational data model][data-model]. This is done by assigning the roles [join key][annotating-data-join-keys] and [time stamp][annotating-data-time-stamp]. The former defines the columns that are used to join different data frames, the latter ensures that only rows in a reasonable time frame are taken into account (otherwise there might be data leaks).

Second, you need to tell the [feature learning algorithm][feature-engineering] how to interpret the individual columns for it to construct sophisticated features. That is why we need the roles [numerical][annotating-data-numerical], [categorical][annotating-data-categorical], and [target][annotating-data-target]. You can also assign [units][annotating-data-units] to each column in a Data Frame.

This chapter contains detailed information on the individual [roles][annotating-data-roles] and [units][annotating-data-units].
