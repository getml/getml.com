# Release Notes
[](){release-notes}

## For getML Enterprise & Community editions { data-toc-label="getML" }

### 1.4.0	<small>Oct 17, 2023</small> {id="1.4.0"}
- Added [Fastboost][getml.feature_learning.Fastboost] feature learner
- Added new predictor: [ScaleGBMClassifier][getml.predictors.ScaleGBMClassifier] and [ScaleGBMRegressor][getml.predictors.ScaleGBMRegressor]
- Added the [EWMATrend aggregations][getml.feature_learning.aggregations]
- Faster JSON parsing using YYJSON

### 1.3.2	<small>Jan 26, 2023</small> {id="1.3.2"}
- Minor bugfixes

### 1.3.1	<small>Dec 20, 2022</small> {id="1.3.1"}
- Minor bugfixes

### 1.3.0	<small>Aug 28, 2022</small> {id="1.3.0"}
- Use websockets instead of polling
- Size [threshold][getml.pipeline.Features.to_sql] for better visualization of feature code
- Significantly sped up reading of memory-mapped data, relevant for all feature learners and predictors

### 1.2.0	<small>May 20, 2022</small> {id="1.2.0"}
- Support for [SQL transpilation][getml.pipeline.dialect]: TSQL, Postgre, MySQL, BigQuery, Spark
- Support for memory mapping

### 1.1.0	<small>Nov 21, 2021</small> {id="1.1.0"}
- Spark support
- Arrow support
- Improved code transpilation for seasonal variables
- Early stopping
- Trend aggregation
- Better progress logging
- Arange support in our virtual columns

### 1.0.0	<small>Sep 23, 2021</small> {id="1.0.0"}
- Complete overhaul of the API, including [Views][getml.data.View], [StarSchema][getml.data.StarSchema], [TimeSeries][getml.data.TimeSeries]

### 0.16.0 <small>May 25, 2021</small> {id="0.16.0"}
- Added the [Mapping preprocessor][getml.preprocessors.Mapping]

### 0.15.0 <small>Feb 23, 2021</small> {id="0.15.0"}
- Added the Fastprop feature learner
- Overhauled the way RelMT and Relboost generate features, making them more efficient

### 0.14.0 <small>Jan 18, 2021</small> {id="0.14.0"}
- Rename to [RelMT][getml.feature_learning.RelMT]


### 0.13.0 <small>Nov 13, 2020</small> {id="0.13.0"}

- Introduce new feature learner: RelMTModel, now [RelMT][getml.feature_learning.RelMT], RelMTTimeSeries [deprecated]

### 0.12.0 <small>Oct 1, 2020</small> {id="0.12.0"}
- Extend dataframe handling: [delete][getml.data.DataFrame.delete], [exists][getml.data.exists]
- Data set provisioning: [load_air_pollution][getml.datasets.load_air_pollution], [load_atherosclerosis][getml.datasets.load_atherosclerosis], [load_biodegradability][getml.datasets.load_biodegradability], [load_consumer_expenditures][getml.datasets.load_consumer_expenditures], [load_interstate94][getml.datasets.load_interstate94], [load_loans][getml.datasets.load_loans], [load_occupancy][getml.datasets.load_occupancy]
- High-level hyperopt handlers: [tune_feature_learners][getml.hyperopt.tune_feature_learners], [tune_predictors][getml.hyperopt.tune_predictors]
- Improve pipeline functionality: [delete][getml.pipeline.delete], [exists][getml.pipeline.exists], [Columns][getml.pipeline.Columns] 
- Introduce preprocessors: [EmailDomain][getml.preprocessors.EmailDomain], [Imputation][getml.preprocessors.Imputation], [Seasonal][getml.preprocessors.Seasonal], [Substring][getml.preprocessors.Substring] 
### 0.11.1 <small>Jul 13, 2020</small> {id="0.11.1"}
- Add pipeline functionality: [Pipeline][getml.pipeline.Pipeline], [list_pipelines][getml.pipeline.list_pipelines], [Features][getml.pipeline.Features], [Metrics][getml.pipeline.metrics], [SQLCode][getml.pipeline.SQLCode], [Scores][getml.pipeline.Scores]
- Better control of Hyperparameter optimization: [burn_in][getml.hyperopt.burn_in], [kernels][getml.hyperopt.kernels], [optimization][getml.hyperopt.burn_in.random]
- Handling of time stamps: [time][getml.data.time]
- Improve database I/O: [connect_odbc][getml.database.connect_odbc.connect_odbc], [copy_table][getml.database.copy_table.copy_table], [list_connections][getml.database.list_connections.list_connections], [read_s3][getml.data.DataFrame.read_s3], [sniff_s3][getml.database.sniff_s3.sniff_s3]
- Enable S3 access: [set_s3_access_key_id][getml.data.access.set_s3_access_key_id], [set_s3_secret_access_key][getml.data.access.set_s3_secret_access_key]
- New Feature Learner: MultirelTimeSeries [deprecated], RelboostTimeSeries [deprecated]

### 0.10.0 <small>Mar 17, 2020</small> {id="0.10.0"}
- Overhaul of documentation 
    - Introduction of "getML in one minute" (now [Quickstart][quick-start-guide]) and "How to use this guide"
    - Introduction of User Guide to include data annotation, feature engineering, hyperparameter optimization and more
- Integration with additional databases like [Greenplum][getml.database.connect_greenplum.connect_greenplum], [MariaDB][getml.database.connect_mariadb.connect_mariadb], [MySQL][getml.database.connect_mysql.connect_mysql], and extended [PostgreSQL][getml.database.connect_postgres.connect_postgres] support.
### 0.9.1	<small>Mar 17, 2020</small> {id="0.9.1"}
- Include hotfix for new domain getml.com
### 0.9	<small>Dec 9, 2019</small>  {id="0.9"}

### 0.8	<small>Oct 22, 2019</small> {id="0.8"}
- Renamed autosql to multirel
- Moved from closed beta to pip
- Introduce basic hyperopt algorithms: [LatinHypercubeSearch][getml.hyperopt.LatinHypercubeSearch], [RandomSearch][getml.hyperopt.RandomSearch]


