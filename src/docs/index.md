---
  title: ""
---

getML is an innovative tool for the end-to-end automation of data
science projects. It covers everything from convenient data loading procedures 
to the deployment of trained models. 


### Why getML

getML features:

- **automated feature engineering** — five highly efficient algorithms for automated feature engineering on relational data and time series
- **database engine** — a high-performance database engine written in C++ customized for feature engineering
- **faster speed** — 60x to 1000x more speed than other tools for automated feature engineering
- **python API** — an intuitive python API to interact with the engine 
- **increase in prediction accuracy** — increase of up to 30% in prediction accuracy compared to manual feature engineering  
- **less time** — decrease of up to 90% time spent on a data science project
- **real-time dashboard** — a real-time monitor for tracking data, pipelines, and performance 
- **native data connectors** — multiple native data connectors for maximum efficiency and minimal data duplication
-  **transpilation**  — transpilation of engineered features into numerous SQL dialects
-  **deployment** — seamless deployment of ML pipelines into production environments for real-time and batch predictions.



!!! enterprise-adm "Enterprise and community editions" 

    getML comes with a full-featured Enterprise Edition as well as limited-featured 
    Community Edition. Compare the highlights of both editions in our 
    [community vs enterprise edition table](home/getting_started/getting_started.md#community-vs-enterprise-edition). 
    Unlock advanced features by purchasing the Enterprise Edition. 
    For licenses, technical support, and more information, please [contact us](https://www.getml.com/contact)!


### Why automated feature engineering

Feature engineering on relational data is the process of creating a 
flat table by merging and aggregating data. Also referred to
as **data wrangling**, feature engineering is essential if your data is distributed
over multiple tables. 

Andrew Ng, Professor at Stanford
University and Co-founder of Google Brain described manual feature engineering as follows:

!!! quote

    Coming up with features is difficult, time-consuming, requires expert
    knowledge. "Applied machine learning" is basically feature engineering.

The main purpose of getML is to automate this *"difficult, time-consuming"* process as much as possible.



### Example

Completing a data science project with getML consists of seven
simple steps.


```python
import getml

getml.engine.launch()
getml.engine.set_project('one_minute_to_getml')


# 1. Load the data into the engine
df_population = getml.data.DataFrame.from_csv('data_population.csv',
            name='population_table')
df_peripheral = getml.data.DataFrame.from_csv('data_peripheral.csv',
            name='peripheral_table')


# 2. Annotate the data
df_population.set_role(cols='target', role=getml.data.role.target)
df_population.set_role(cols='join_key', role=getml.data.role.join_key)


# 3. Define the data model
dm = getml.data.DataModel(population=df_population.to_placeholder())
dm.add(df_peripheral.to_placeholder())
dm.population.join(
   dm.peripheral,
   on="join_key",
)


# 4. Train the feature learning algorithm and the predictor
pipe = getml.pipeline.Pipeline(
    data_model=dm,
    feature_learners=getml.feature_learning.FastProp(),
    predictors=getml.predictors.LinearRegression()
)
pipe.fit(
    population=df_population,
    peripheral=[df_peripheral]
)


# 5. Evaluate
pipe.score(
    population=df_population_unseen,
    peripheral=[df_peripheral_unseen]
)


# 6. Predict   
pipe.predict(
    population=df_population_unseen,
    peripheral=[df_peripheral_unseen]
)


# 7. Deploy
# Allow the pipeline to respond to HTTP requests
pipe.deploy(True)
```

Check out the rest of this documentation to find out how getML achieves top
performance on real-world data science projects with many tables and complex
data schemes.



### How to use the developer portal

If you want to get started with getML right away, we recommend to follow the
[installation instructions][installation] and then go through the
[getting started guide][getting-started]. 

If you are looking for more detailed information, other sections of this
documentation are more suitable:

- [Examples](./examples/index.md)
  
    The examples section contains examples of how to use getML in 
    real-world projects. All examples are based on public data sets 
    so that
    you can follow along. If you are looking for an intuitive access to
    getML, the examples section is the right place to go. Also, the
    code examples are explicitly intended to be used as a template for
    your own projects.  

- [User guide][user-guide]

    The user guide explains all conceptional details behind getML in
    depth. It can serve as a reference guide for experienced users but it's also
    suitable for first day users who want to get a deeper understanding
    of how getML works. Each chapter in the
    user guide represents one step of a typical data science project.

- [API documentation][python-api]

    The API documentation covers everything related to the Python
    interface to the getML engine. Each module comes with a dedicated
    section that contains concrete code examples.


The developer portal is targeted to data scientists who want to use the getML software suite for their projects. For business-related information about getML, visit [getml.com](https://getml.com). You can also check out our [blog articles and case studies](https://www.getml.com/blog). And, of course, you can always [contact
us](https://www.getml.com/contact) for any questions or inquiries.

