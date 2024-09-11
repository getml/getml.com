# Enterprise Edition Notebooks {#enterprise-notebooks}

A diverse collection of Jupyter Notebooks that showcase relational datasets across various domains, addressing typical data science challenges like binary classification on time series and regression with complex relational data, using publicly available datasets for benchmarking. 

## Algorithms and Predictors 
Serving as both documentation and practical blueprints, these notebooks demonstrate the performance of getML's feature engineering algorithms ([`FastProp`][getml.feature_learning.FastProp], [`Multirel`][getml.feature_learning.Multirel], [`Relboost`][getml.feature_learning.Relboost], [`RelMT`][getml.feature_learning.RelMT]) and predictors ([`LinearRegression`][getml.predictors.LinearRegression], [`LogisticRegression`][getml.predictors.LogisticRegression], [`XGBoostClassifier`][getml.predictors.XGBoostClassifier], [`XGBoostRegressor`][getml.predictors.XGBoostRegressor] ) against competing tools like [featuretools](https://www.featuretools.com), [tsfresh](https://tsfresh.readthedocs.io/en/latest/), and [Prophet](https://facebook.github.io/prophet/). 

!!! enterprise-adm "Enterprise edition"
    While FastProp excels in speed and resource efficiency, more advanced algorithms only available in the Enterprise Edition, deliver higher accuracy with even lower resource demands.
    Discover the [benefits of the Enterprise edition][enterprise-benefits] and [compare their features][enterprise-feature-list].

## Overview

|                                                               | Task           | Data                     | Size               | Domain         |
| ------------------------------------------------------------- | -------------- | ------------------------ | ------------------ | -------------- |
| [AdventureWorks - Predicting customer churn](adventure_works.ipynb) | Classification | Relational               | 71 tables, 233 MB  | Commerce       |
| [Air Pollution - Why feature learning is better than simple propositionalization](air_pollution.ipynb) | Regression     | Multivariate time series | 1 table, 41k rows  | Environment    |
| [Atherosclerosis - Disease lethality prediction](atherosclerosis.ipynb) | Classification | Relational               | 3 tables, 22 MB    | Health         |
| [Baseball - Predicting players' salary](baseball.ipynb) | Regression     | Relational               | 25 tables, 74 MB   | Sports         |
| [Consumer expenditure - Why relational learning matters](consumer_expenditures.ipynb) | Classification | Relational               | 3 tables, 150 MB   | E-commerce     |
| [CORA - Categorizing academic publications](cora.ipynb) | Classification | Relational               | 3 tables, 4.6 MB   | Academia       |
| [Dodgers - Traffic volume prediction](dodgers.ipynb) | Regression     | Multivariate time series | 1 table, 47k rows  | Transportation |
| [Formula 1 - Predicting the winner of a race](formula1.ipynb) | Classification | Relational               | 13 tables, 56 MB   | Sports         |
| [IMDb - Predicting actors' gender](imdb.ipynb) | Classification | Relational with text     | 7 tables, 477.1 MB | Entertainment  |
| [Interstate 94 - Multivariate time series prediction](interstate94.ipynb) | Regression     | Multivariate time series | 1 table, 24k rows  | Transportation |
| [Loans - Predicting loan default risk](loans.ipynb) | Classification | Relational               | 8 tables, 60 MB    | Financial      |
| [MovieLens - Predicting a user's gender based on the movies they have watched](movie_lens.ipynb) | Classification | Relational               | 7 tables, 20 MB    | Entertainment  |
| [Occupancy - A multivariate time series example](occupancy.ipynb) | Classification | Multivariate time series | 1 table, 32k rows  | Energy         |
| [Online Retail - Predicting order cancellations](online_retail.ipynb) | Classification | Relational               | 1 table, 398k rows | E-commerce     |
| [Robot - Feature engineering on sensor data](robot.ipynb) | Regression     | Multivariate time series | 1 table, 15k rows  | Robotics       |
| [Seznam - Predicting transaction volume](seznam.ipynb) | Regression     | Relational               | 4 tables, 147 MB   | E-commerce     |
| [SFScores - Predicting health inspection scores of restaurants](sfscores.ipynb) | Regression     | Relational               | 3 tables, 9 MB     | Restaurants    |
| [StatsExchange - Predicting users' reputations](stats.ipynb) | Regression     | Relational               | 8 tables, 658 MB   | Internet       |

## Source

These notebooks are published on the [getml-demo](https://github.com/getml/getml-demo) repository.