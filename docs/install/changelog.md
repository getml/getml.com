# Changelog {#changelog}

## For getML Enterprise & Community editions { data-toc-label="getML" }

### 1.5.0   <small>Sep 24, 2024</small> {id="1.5.0"}
#### Features
- Overhaul and better integration of API documentation and web page:
    - Switch from [sphinx](https://www.sphinx-doc.org/en/master/) to [mkdocs](https://www.mkdocs.org/)
    - Restructuring of [User Guide][user-guide-index], multiple amendments to documentation 
- Introduce strict typing regiment for [feature learning aggregations][getml.feature_learning.aggregations] and [loss functions][getml.feature_learning.loss_functions]
- Clean up and maintenance of [example notebooks][examples-index], make them executable in [Colab](https://colab.google/)
- More informative progress bar and status updates using [rich](https://github.com/Textualize/rich?tab=readme-ov-file)
- Completely reworked IO
    - Improved reliability, speed and maintainability by capitalizing on [PyArrow](https://arrow.apache.org/docs/python/index.html)
- Introduce [reflect-cpp](https://github.com/getml/reflect-cpp) for parsing and de/serialization
- Availability of [getML Docker runtime as a service on Docker Hub](https://hub.docker.com/r/getml/getml), allowing for easy setup 
#### Developer-focused
- Complete rework of the build pipeline (docker and linux native)
    - Introduce [CCache](https://ccache.dev/), [conan](https://conan.io/), [vcpkg](https://vcpkg.io/en/)
    - User multi-stage docker builds leveraging buildx and buildkit
    - Centralized `VERSION`
- [Ruff](https://docs.astral.sh/ruff/) for linting and formatting
- [Hatch](https://hatch.pypa.io/latest/) for python package management
#### Bug fixes
- Generalization of [`Placeholder.join`][getml.data.Placeholder.join]'s `on` argument 
- Improved timestamp handling
- Slicing improvements
    - Slicing of `DataFrames` returned wrong results: Remove short circuit for slices with upper bound
    - Introduce set semantics for slicing of `DataFrame` (return empty collections instead of erroring)
- Fix displaying of parameter lists with values that exceed the presentable width
- Fix displaying of [`DataFrames`][getml.data.DataFrame] with one row or less
- Fix progress bar output on Google Colab

### 1.4.0	<small>Oct 17, 2023</small> {id="1.4.0"}
- Accelerated feature learning through [Fastboost][getml.feature_learning.Fastboost]
- Improved modelling on huge datasets through [ScaleGBMClassifier][getml.predictors.ScaleGBMClassifier] and [ScaleGBMRegressor][getml.predictors.ScaleGBMRegressor]
- Advanced trend aggregations using [EWMATrend aggregations][getml.feature_learning.aggregations.EWMA_1S]
- Faster JSON parsing using YYJSON

### 1.3.2	<small>Jan 26, 2023</small> {id="1.3.2"}
- Minor bugfixes

### 1.3.1	<small>Dec 20, 2022</small> {id="1.3.1"}
- Implement `tqdm` for progress bars
- Minor bugfixes

### 1.3.0	<small>Aug 28, 2022</small> {id="1.3.0"}
- Use websockets instead of polling
- Size [threshold][getml.pipeline.Features.to_sql] for better visualization of feature code
- Faster reading of memory-mapped data, relevant for all feature learners and predictors
- Introduce [CategoryTrimmer][getml.preprocessors.CategoryTrimmer] as preprocessor

### 1.2.0	<small>May 20, 2022</small> {id="1.2.0"}
- Support for [SQL transpilation][getml.pipeline.dialect]: TSQL, Postgres, MySQL, BigQuery, Spark
- Support for memory mapping

### 1.1.0	<small>Nov 21, 2021</small> {id="1.1.0"}
- Enhance data processing by introducing Spark (e.g. [spark_sql][getml.pipeline.dialect.spark_sql]) and Arrow (e.g. [from_arrow()][getml.data.DataFrame.from_arrow])
- Integrate Vcpkg for dependency management
- Improve code transpilation for seasonal variables
- Better control of predictor training and hyperparamter optimization through introduction of early stopping (e.g. in [ScaleGBMClassifier][getml.predictors.ScaleGBMClassifier])
- Introduce [TREND][getml.feature_learning.aggregations.TREND] aggregation
- Better progress logging

### 1.0.0	<small>Sep 23, 2021</small> {id="1.0.0"}
- Introduction of [Containers][getml.data.Container] for data storage
- Complete overhaul of the API including [Views][getml.data.View], [StarSchema][getml.data.StarSchema], [TimeSeries][getml.data.TimeSeries]
- Add [subroles][getml.data.subroles] for fine grained data control
- Improved model evaluation through [Plots][getml.pipeline.Plots] and [Scores][getml.pipeline.Scores] container
- Introduce [slicing][getml.data.View.where] of Views
- Add [datetime()][getml.data.time.datetime] utility

### 0.16.0 <small>May 25, 2021</small> {id="0.16.0"}
- Add the [Mapping][getml.preprocessors.Mapping] and [TextFieldSplitter][getml.preprocessors.TextFieldSplitter] preprocessors

### 0.15.0 <small>Feb 23, 2021</small> {id="0.15.0"}
- Add the [Fastprop][getml.feature_learning.FastProp] feature learner
- Overhaul the way RelMT and Relboost generate features, making them more efficient

### 0.14.0 <small>Jan 18, 2021</small> {id="0.14.0"}
- Significant improvement of  project management:
    -  [project.restart()][getml.project.attrs.restart], [project.suspend()][getml.project.attrs.suspend], and [project.switch()][getml.project.attrs.switch]
    - multiple project support
- Add custom `__getattr__` and `__dir__` methods to DataFrame, enabling column retrieval through autocomplete

### 0.13.0 <small>Nov 13, 2020</small> {id="0.13.0"}
- Introduce new feature learner: 
    - RelMTModel [now [RelMT][getml.feature_learning.RelMT]], 
    - RelMTTimeSeries [now integrated in [TimeSeries][getml.data.TimeSeries]]

### 0.12.0 <small>Oct 1, 2020</small> {id="0.12.0"}
- Extend dataframe handling: [delete()][getml.data.DataFrame.delete], [exists()][getml.data.exists]
- Data set provisioning: [load_air_pollution()][getml.datasets.load_air_pollution], [load_atherosclerosis()][getml.datasets.load_atherosclerosis], [load_biodegradability()][getml.datasets.load_biodegradability], [load_consumer_expenditures()][getml.datasets.load_consumer_expenditures], [load_interstate94()][getml.datasets.load_interstate94], [load_loans()][getml.datasets.load_loans], [load_occupancy()][getml.datasets.load_occupancy]
- High-level hyperopt handlers: [tune_feature_learners()][getml.hyperopt.tune_feature_learners], [tune_predictors()][getml.hyperopt.tune_predictors]
- Improve pipeline functionality: [delete()][getml.pipeline.delete], [exists()][getml.pipeline.exists], [Columns][getml.pipeline.Columns] 
- Introduce preprocessors: [EmailDomain][getml.preprocessors.EmailDomain], [Imputation][getml.preprocessors.Imputation], [Seasonal][getml.preprocessors.Seasonal], [Substring][getml.preprocessors.Substring] 

### 0.11.1 <small>Jul 13, 2020</small> {id="0.11.1"}
- Add pipeline functionality: [Pipeline][getml.pipeline.Pipeline], [list_pipelines()][getml.pipeline.list_pipelines], [Features][getml.pipeline.Features], [Metrics][getml.pipeline.metrics], [SQLCode][getml.pipeline.SQLCode], [Scores][getml.pipeline.Scores]
- Better control of hyperparameter optimization: [burn_in][getml.hyperopt.burn_in], [kernels][getml.hyperopt.kernels], [optimization][getml.hyperopt.optimization]
- Handling of time stamps: [time][getml.data.time]
- Improve database I/O: [connect_odbc()][getml.database.connect_odbc.connect_odbc], [copy_table()][getml.database.copy_table.copy_table], [list_connections()][getml.database.list_connections.list_connections], [read_s3()][getml.data.DataFrame.read_s3], [sniff_s3()][getml.database.sniff_s3.sniff_s3]
- Enable S3 access: [set_s3_access_key_id()][getml.data.access.set_s3_access_key_id], [set_s3_secret_access_key()][getml.data.access.set_s3_secret_access_key]
- New Feature Learner: MultirelTimeSeries, RelboostTimeSeries [now both integrated in [TimeSeries][getml.data.TimeSeries]]

### 0.10.0 <small>Mar 17, 2020</small> {id="0.10.0"}
- Add [XGBoostClassifier][getml.predictors.XGBoostClassifier] and [XGBoostRegressor][getml.predictors.XGBoostRegressor] for improved predictive power
- Overhaul of documentation 
    - Introduction of "getML in one minute" (now [Quickstart][quick-start-guide]) and "How to use this guide" (now [User Guide][user-guide-index])
    - Introduction of User Guide (now [Concepts][concepts-guide]) to include data annotation, feature engineering, hyperparameter optimization and more
- Integration with additional databases like [Greenplum][getml.database.connect_greenplum.connect_greenplum], [MariaDB][getml.database.connect_mariadb.connect_mariadb], [MySQL][getml.database.connect_mysql.connect_mysql], and extended [PostgreSQL][getml.database.connect_postgres.connect_postgres] support

### 0.9.1	<small>Mar 17, 2020</small> {id="0.9.1"}
- Include hotfix for new domain getml.com

### 0.9	<small>Dec 9, 2019</small>  {id="0.9"}
- Rework hyperopt design and handling, added [load_hyperopt()][getml.hyperopt.load_hyperopt.load_hyperopt]
- Improved dataframe handling: add [to_placeholder()][getml.data.DataFrame.to_placeholder] and [nrows()][getml.data.DataFrame.nrows]

### 0.8	<small>Oct 22, 2019</small> {id="0.8"}
- Rename Autosql to [Multirel][getml.feature_learning.Multirel]
- Boolean and categorical columns: Add support for boolean columns and operators, along with enhanced categorical column handling.
- Introduce API improvements: fitting, saving/loading of models, data transformation
- Add support for various aggregation functions such as [MEDIAN][getml.feature_learning.aggregations.MEDIAN], [VAR][getml.feature_learning.aggregations.VAR], [STDDEV][getml.feature_learning.aggregations.STDDEV], and [COUNT_DISTINCT][getml.feature_learning.aggregations.COUNT_DISTINCT]
- Move from closed beta to [pip](https://pypi.org/project/getml/)
- Introduce basic hyperopt algorithms: [LatinHypercubeSearch][getml.hyperopt.LatinHypercubeSearch], [RandomSearch][getml.hyperopt.RandomSearch]
