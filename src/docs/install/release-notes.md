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
- Support for SQL transpilation: TSQL, Postgre, MySQL, BigQuery, Spark
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
- Added the RelMT feature learner

/// html | div.hidden

### 0.13.0 <small>Nov 13, 2020</small> {id="0.13.0"}
### 0.12.0 <small>Oct 1, 2020</small> {id="0.12.0"}
### 0.11.1 <small>Jul 13, 2020</small> {id="0.11.1"}
### 0.10.0 <small>Mar 17, 2020</small> {id="0.10.0"}
### 0.9.1	<small>Mar 17, 2020</small> {id="0.9.1"}
### 0.9	<small>Dec 9, 2019</small>  {id="0.9"}
### 0.8	<small>Oct 22, 2019</small> {id="0.8"}

///
