---
hide:
  - navigation
---
# Documentation

Welcome to the getML technical documentation. This document is written for data
scientists who want to use the getML software suite for their projects. For
general information about getML visit [getml.com](https://getml.com). For a collection of
demo notebooks, visit [getml-demo](https://github.com/getml/getml-demo). You can also [contact
us](https://www.getml.com/contact) for any questions or inquiries.

!!! note 

    Some components of getML have been open sourced as part of **getML community edition**.  You may have a look at 
    [community vs enterprise edition table](home/getting_started/getting_started.md#community-vs-enterprise-edition)
    to see the highlights of both the editions. 


## GetML in one minute 

getML is an innovative tool for the end-to-end automation of data
science projects. It covers everything from convenient data loading procedures 
to the deployment of trained models. 

Most notably, getML includes advanced algorithms for
**automated feature engineering** (feature learning) on relational data and time
series. Feature engineering on relational data is defined as the creation of a 
flat table by merging and aggregating data. It is sometimes also referred to
as **data wrangling**. Feature engineering is necessary if your data is distributed
over more than one data table.

Automated feature engineering

* Saves up to 90% of the time spent on a data science project
* Increases the prediction accuracy over manual feature engineering 

Andrew Ng, Professor at Stanford
University and Co-founder of Google Brain described manual feature engineering as follows:

> *Coming up with features is difficult, time-consuming, requires expert
> knowledge. "Applied machine learning" is basically feature engineering.*

The main purpose of getML is to automate this *"difficult, time-consuming"* process as much
as possible.

getML comes with a high-performance **engine** written in C++ and an intuitive
**Python API**. Completing a data science project with getML consists of seven
simple steps.

```python
import getml

getml.engine.launch()
getml.engine.set_project('one_minute_to_getml')
```

1. Load the data into the engine

```python
population = getml.data.DataFrame.from_csv('data_population.csv',
            name='population_table')
peripheral = getml.data.DataFrame.from_csv('data_peripheral.csv',
            name='peripheral_table')
```
2. Annotate the data

```python 
population.set_role('target', getml.data.role.target)
population.set_role('join_key', getml.data.role.join_key)
...
```
3. Define the data model

```python
dm = getml.data.DataModel(population.to_placeholder("POPULATION"))
dm.add(peripheral.to_placeholder("PERIPHERAL"))
dm.POPULATION.join(
   dm.PERIPHERAL,
   on="join_key",
)
```
4. Train the feature learning algorithm and the predictor

```python
pipe = getml.pipeline.Pipeline(
    data_model=dm,
    feature_learners=getml.feature_learning.FastProp()
    predictors=getml.predictors.LinearRegression()
)

pipe.fit(
    population=population,
    peripheral=[peripheral]
)
```
5. Evaluate

```python
pipe.score(
    population=population_unseen,
    peripheral=[peripheral_unseen]
)
```
6. Predict   

```python
pipe.predict(
    population=population_unseen,
    peripheral=[peripheral_unseen]
)
```
7. Deploy

```python
# Allow the pipeline to respond to HTTP requests
pipe.deploy(True)
```
Check out the rest of this documentation to find out how getML achieves top
performance on real-world data science projects with many tables and complex
data schemes.

____

## How to use this guide

If you want to get started with getML right away, we recommend to follow the
[installation instructions][installation] and then go through the
[getting started guide][getting-started]. 

If you are looking for more detailed information, other sections of this
documentation are more suitable. There are three major parts: 

[Tutorials](https://github.com/getml/getml-demo)

  The tutorials section contains examples of how to use getML in 
  real-world projects. All tutorials are based on public data sets 
  so that
  you can follow along. If you are looking for an intuitive access to
  getML, the tutorials section is the right place to go. Also, the
  code examples are explicitly intended to be used as a template for
  your own projects.  

[User guide][user-guide]

  The user guide explains all conceptional details behind getML in
  depth. It can serve as a reference guide for experienced users but it's also
  suitable for first day users who want to get a deeper understanding
  of how getML works. Each chapter in the
  user guide represents one step of a typical data science project.

[API documentation][python-api]

  The API documentation covers everything related to the Python
  interface to the getML engine. Each module comes with a dedicated
  section that contains concrete code examples.

You can also check out our other resources

[getML homepage](https://getml.com)
