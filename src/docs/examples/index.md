# Examples
[](){#examples-index}

This section showcases practical demonstrations of getML's capabilities across various domains and use cases, including integrations with other tools and frameworks.

## Demo Repository
Our [getml-demo](https://github.com/getml/getml-demo) repository on GitHub features a collection of Jupyter Notebooks that illustrate different aspects of getML's feature engineering and predictive modeling. You will get a comprehensive overview of how getML can be applied to various machine learning tasks, from basic feature engineering to advanced relational learning. Here are some interesting sections to get you started:

- #### FastProp Benchmark Notebooks (Community Edition)
    Showcase the performance of getML's [FastProp algorithm](https://docs.getml.com/latest/user_guide/feature_engineering/feature_engineering.html#fastprop), designed for efficient feature engineering and typically outperforming competing tools in runtime and resource requirements. These benchmarks help you understand how getML handles large datasets and complex feature engineering tasks.

    !!! example "Key Examples of FastProp Benchmarks:"

        **[Air Pollution Prediction](https://github.com/getml/getml-demo/blob/master/fastprop_benchmark/air_pollution_prop.ipynb)**: Demonstrates the superiority of FastProp over featuretools and tsfresh in runtime and predictive accuracy.

        **[Dodgers Traffic Volume Prediction](https://github.com/getml/getml-demo/blob/master/fastprop_benchmark/dodgers_prop.ipynb)**: Showcases FastProp's handling of high-frequency time series data, outperforming Prophet and tsfresh.

        **[Interstate 94 Traffic Volume Prediction](https://github.com/getml/getml-demo/blob/master/fastprop_benchmark/interstate94_prop.ipynb)**: Highlights FastProp's efficiency and predictive power compared to traditional methods.

- #### Feature Learner Notebooks (Enterprise Edition)
    Demonstrate the advanced feature engineering capabilities available in the [Enterprise edition](https://www.getml.com/pricing), including sophisticated algorithms like [Multirel](https://docs.getml.com/latest/user_guide/feature_engineering/feature_engineering.html#multirel), [Relboost](https://docs.getml.com/latest/user_guide/feature_engineering/feature_engineering.html#relboost), and [RelMT](https://docs.getml.com/latest/user_guide/feature_engineering/feature_engineering.html#relmt). They provide insights into achieving superior predictive performance on real-world data.

    !!! example "**Key Examples of Enterprise Features:**"

        **[AdventureWorks Customer Churn Prediction](https://github.com/getml/getml-demo/blob/master/adventure_works.ipynb)**: Utilizes Multirel to predict customer churn, demonstrating the benefits of relational learning algorithms.

        **[Atherosclerosis Disease Lethality Prediction](https://github.com/getml/getml-demo/blob/master/atherosclerosis.ipynb)**: Applies Relboost to complex medical datasets, showcasing its ability to manage high-dimensional data efficiently.

        **[Baseball Salary Prediction](https://github.com/getml/getml-demo/blob/master/baseball.ipynb)**: Uses RelMT to predict baseball player salaries, demonstrating advanced feature learners in sports analytics.

## Integrations
Demonstrations of how to connect getML with other tools and frameworks to enhance its functionality. Currently, we have an example showcasing integration with FastAPI, with more integrations coming soon.

### FastAPI
- **[Integration with FastAPI](/integration/fastapi/fastapi/)**: How to integrate getML with FastAPI to create a REST API for your machine learning models. This guide shows how to set up a generic prediction endpoint, making your getML pipelines accessible via web APIs.
