``` python hl_lines="11 17 24" linenums="1"
import getml

# Staging of data
data_container = ... # (6)!

# Defintion of data model
star_schema = ... # (7)!

# Define the feature learners
fast_prop = getml.feature_learning.FastProp() # (1)!
relboost = getml.feature_learning.Relboost() # (2)!

# Define the predictor
xgb_predictor = getml.predictors.ScaleGBMRegressor() # (3)!

# Define the pipeline
pipeline = getml.pipeline.Pipeline( # (4)!
    data_model = star_schema.data_model,
    feature_learners = [fast_prop, relboost],
    predictors = xgb_predictor
)

# Train the feature learnings and the predictor
pipeline.fit(data_container.train) # (5)!

pipeline.predict(data_container.test)
```

1.  [`FastProp`][feature-engineering-algorithms-fastprop]{ data-preview_ } comes with our [Community](https://github.com/getml/getml-community) edition. It is fast and generates a substantial number of important features based on simple aggregations.

2.  [`Relboost`][feature-engineering-algorithms-relboost]{ data-preview_ } is part our [Enterprise][enterprise-benefits] edition. A generalization of the gradient boosting algorithm, Relboost can learn really complex interdependencies.

3. [`ScaleGBMRegressor`][getml.predictors.ScaleGBMRegressor]{ data-preview_ } is our memory-mapped predictor that can handle big datasets that do not fit into memory.

4. [`Pipeline`][getml.pipeline.Pipeline]{ data-preview_ } bundles together the data model, feature learners and predictors. Just with this line of code, getML takes care of generation and selection of features, and training of the predictor when the pipeline's `fit` is called next.

5. Inspired by libraries like `scikit-learn`, the [`fit()`][getml.pipeline.Pipeline.fit]{ data-preview_ }, [`score()`][getml.pipeline.Pipeline.score]{ data-preview_ }, and [`predict()`][getml.pipeline.Pipeline.predict]{ data-preview_ } methods of a pipeline make the machine learning process a breeze.

6. [`Container`][getml.data.Container]{ data-preview_ } holds data that is assigned to any given data model.

7. [`StarSchema`][getml.data.StarSchema]{ data-preview_ } is one of our go-to data model abstractions that covers the vast majority of relational data use cases.

/// html | div.hidden
To find the best set of aggregation functions and conditions, getML’s supervised learning algorithms perform an iterative, tree-based search inside relational data. This allows for the automatic generation of complex features for a given target variable on a scale and accuracy that no manual or brute-force approach can match.
///
