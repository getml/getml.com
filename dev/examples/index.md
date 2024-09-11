# Examples {#examples-index}

This section showcases practical demonstrations of getML's capabilities across various domains and use cases, including integrations with other tools and frameworks.

## [Community Edition Notebooks][community-notebooks] {#community-notebooks-overview}

A collection of Jupyter notebooks published on the [getml-community](https://github.com/getml/getml-community/tree/main/demo-notebooks) repository, showcasing the features of the getML Community edition across various data types, prediction tasks, and application domains. These notebooks can be run locally or on Google Colab without any restrictions (certain features in the [Enterprise edition][enterprise-benefits] require a license).

### [FastProp Benchmarks][fastprop-benchmarks] {#fastprop-benchmarks-overview}
Showcase the performance of getML's [FastProp algorithm][feature-engineering-algorithms-fastprop], designed for efficient feature engineering and typically outperforming competing tools in runtime and resource requirements. These benchmarks help you understand how getML handles large datasets and complex feature engineering tasks.

!!! example "Key Examples of FastProp Benchmarks:"
    **[Air Pollution Prediction](enterprise-notebooks/fastprop_benchmark/air_pollution_prop.ipynb)**: Demonstrates the superiority of FastProp over featuretools and tsfresh in runtime and predictive accuracy.

    **[Dodgers Traffic Volume Prediction](enterprise-notebooks/fastprop_benchmark/dodgers_prop.ipynb)**: Showcases FastProp's handling of high-frequency time series data, outperforming Prophet and tsfresh.

    **[Interstate 94 Traffic Volume Prediction](enterprise-notebooks/fastprop_benchmark/interstate94_prop.ipynb)**: Highlights FastProp's efficiency and predictive power compared to traditional methods.

## [Enterprise Edition Notebooks][enterprise-notebooks] {#enterprise-notebooks-overview}
Published on the [getml-demo](https://github.com/getml/getml-demo) repository, these notebooks demonstrate the advanced feature engineering capabilities available in the [Enterprise edition][enterprise-benefits], including sophisticated algorithms like [Multirel][feature-engineering-algorithms-multirel], [Relboost][feature-engineering-algorithms-relboost], and [RelMT][feature-engineering-algorithms-relmt]. They provide insights into achieving superior predictive performance on real-world data. Here are some interesting sections to get you started:

!!! example "**Key Examples of Enterprise Features:**"
    **[AdventureWorks Customer Churn Prediction](enterprise-notebooks/adventure_works.ipynb)**: Utilizes Multirel to predict customer churn, demonstrating the benefits of relational learning algorithms.

    **[Atherosclerosis Disease Lethality Prediction](enterprise-notebooks/atherosclerosis.ipynb)**: Applies Relboost to complex medical datasets, showcasing its ability to manage high-dimensional data efficiently.

    **[Baseball Salary Prediction](enterprise-notebooks/baseball.ipynb)**: Uses RelMT to predict baseball player salaries, demonstrating advanced feature learners in sports analytics.

## Integrations
Demonstrations of how to connect getML with other tools and frameworks to enhance its functionality. Currently, we have an example showcasing integration with FastAPI, with more integrations coming soon.

- ### [FastAPI][fastapi] {#fastapi-integrations}
How to integrate getML with [FastAPI](https://fastapi.tiangolo.com/) to create a REST API for your machine learning models. This guide shows how to set up a generic prediction endpoint, making your getML pipelines accessible via web APIs.

- ### [VertexAI](integrations/vertexai/vertexai.ipynb) {#vertexai-integrations}
A step-by-step guide on how to deploy getML models on [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai), enabling scalable and powerful machine learning workflows on Google Cloud Platform.