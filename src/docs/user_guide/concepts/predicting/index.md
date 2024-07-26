[](){#predicting}
# Predicting

Now that you know how to [engineer a flat table of features][feature-engineering], you are ready to make predictions of the [target variable(s)][annotating-data-target].

## Using getML

getML comes with six built-in machine learning predictors:

- [`LinearRegression`][getml.predictors.LinearRegression]
- [`LogisticRegression`][getml.predictors.LogisticRegression]
- [`XGBoostClassifier`][getml.predictors.XGBoostClassifier]
- [`XGBoostRegressor`][getml.predictors.XGBoostRegressor]
- [`ScaleGBMClassifier`][getml.predictors.ScaleGBMClassifier]
- [`ScaleGBMRegressor`][getml.predictors.ScaleGBMRegressor]

!!! info "Enterprise Feature"
    [`ScaleGBMClassifier`][getml.predictors.ScaleGBMClassifier] and [`ScaleGBMRegressor`][getml.predictors.ScaleGBMRegressor] are enterprise features and not available in the community edition. Learn more about the [benefits][enterprise-benefits] and see the [comparion of features][enterprise-feature-list] between the community and enterprise edition.

Using one of them in your analysis is very simple. Just pass one as the `predictor` argument to either [`Pipeline`][getml.pipeline.Pipeline]
on initialization. As a list, more than one predictor can be passed to the pipeline.

```python
feature_learner1 = getml.feature_learners.Relboost()

feature_learner2 = getml.feature_learners.Multirel()

predictor = getml.predictors.XGBoostRegressor()

pipe = getml.pipeline.Pipeline(
    data_model=data_model,
    peripheral=peripheral_placeholder,
    feature_learners=[feature_learner1, feature_learner2],
    predictors=predictor,
)
```

When you call [`fit()`][getml.pipeline.Pipeline.fit] on a pipeline, the entire pipeline will be trained.

!!! Note
    
    The time estimation for training a pipeline is a rough estimate. Occasionally, the training time can be significantly longer than the estimate. But the pipeline never silently crashes. Given enough time, computations always finish.

Note that [`Pipeline`][getml.pipeline.Pipeline] comes with dependency tracking. That means it can figure out on its own what has changed and what needs to be trained again.

```python
feature_learner1 = getml.feature_learners.Relboost()

feature_learner2 = getml.feature_learners.Multirel()

predictor = getml.predictors.XGBoostRegressor()

pipe = getml.pipeline.Pipeline(
    data_model=data_model,
    population=population_placeholder,
    peripheral=peripheral_placeholder,
    feature_learners=[feature_learner1, feature_learner2],
    predictors=predictor 
)

pipe.fit(...)

pipe.predictors[0].n_estimators = 50

# Only the predictor has changed,
# so only the predictor will be refitted.
pipe.fit(...)
```

To score the performance of your prediction on a test dataset, the getML models come with a [`score()`][getml.pipeline.Pipeline.score] method. The available metrics are documented in [`metrics`][getml.pipeline.metrics].

To use a trained model, including both the trained features and the predictor, to make predictions on new, unseen data, call the [`predict()`][getml.pipeline.Pipeline.predict] method of your model.

## Using external software

In our experience, the most relevant contribution to making accurate predictions are the generated features. Before trying to tweak your analysis by using sophisticated prediction algorithms and tuning their hyperparameters, we recommend tuning the hyperparameters of your [`Multirel`][getml.feature_learning.Multirel] or [`Relboost`][getml.feature_learning.Relboost] instead. You can do so either by hand or using getML's automated [hyperparameter optimization][hyperparamter-optimization].

If you wish to use external predictors, you can transform new data, which is compliant with your relational data model, to a flat feature table using the [`transform()`][getml.pipeline.Pipeline.transform] method of your pipeline.
