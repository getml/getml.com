---
title: 'Boosting Graph Neural Networks with getML: Automated Feature Engineering for Superior Model Performance'
date: 2023-11-30
authors: [jan, joachim]
slug: boosting-gnns-with-getml
description: >
  How getML’s FastProp algorithm helps optimize your Graph Neural Network
categories:
  - Jupyter Notebooks
  - Kaggle
links:
  - "CORA: Graph Neural Networks vs getML <br><span class='fn'>cora_getml_vs_gnn.ipynb</span>": examples/enterprise-notebooks/kaggle_notebooks/cora_getml_vs_gnn.ipynb
  - "getML and GNNs: A Natural Symbiosis <br><span class='fn'>getml-and-gnns-a-natural-symbiosis.ipynb</span>": examples/enterprise-notebooks/kaggle_notebooks/getml-and-gnns-a-natural-symbiosis.ipynb
---

/// html | span.post-bold
Graph Neural Networks (GNNs) excel at modeling complex data but do require feature engineering. This article shows how integrating getML's FastProp automates this process, boosting accuracy to 92.5% on the CORA dataset—surpassing the 90.16% benchmark. This approach simplifies implementation, reduces manual effort, and ensures consistent performance across a wide range of neural architectures, making it a valuable tool for data scientists for building consistent and high-performing models with minimal effort.
///

<!-- more -->

##  Introduction

While Large Language models and Diffusion models have been attracting a lot of attention, Graph Neural Networks (GNN) also advanced in leaps and bounds. No longer confined to academic exercises, GNNs are applied in [recommender systems](https://www.uber.com/en-DE/blog/uber-eats-graph-learning/), [hardware development](https://blog.research.google/2020/04/chip-design-with-deep-reinforcement.html), [drug discovery](https://www.cell.com/cell/fulltext/S0092-8674(20)30102-1?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS0092867420301021%3Fshowall%3Dtrue) and much more.

One of the primary drivers of the success of GNNs is their incredible flexibility; unlike most deep learning architectures, Graph Networks are not limited to euclidean data representations. When graphs are utilized, the complexity of relationships between entities exceeds what can be represented by tables, images, or words. It is this unbounded structure that proliferates novel approaches and insightful solutions to a variety of problems.

While an abundance of options and parameters may excite experts, it presents a considerable challenge to novices and casual practitioners: Domain knowledge, fine tuning and lengthy experimentation become requirements to successfully implement GNNs. Specifically, to capture the intricacies of real world problems, it is necessary to carefully select and design the right input features. **Feature engineering**, as this process is called, is a time consuming and cumbersome endeavor that resembles more an art than a technique and heavily relies on domain knowledge and intuition.

Another potentially lucrative but labor intensive and computationally expensive step is the experimentation with a variety of Neural Network architectures.

Hence, to exploit the power of GNNs optimally,

*   a lot of time consuming **manual work** and
*   a substantial **computation budget**

is required.

![Photo by Max Duzij on Unsplash](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*-Wudp23uZbWIAL5t)

But not any longer! This article introduces an approach that not only eliminates the need for intricate feature engineering but also reduces the importance of experimentation significantly. Surprisingly, and most importantly, predictive performance of the GNN has risen sharply with the implementation of this innovative tool.

That tool is **getML**.

Now, without further ado, let’s dig right into it.

## Framework and Dataset

[GetML][why-getml] is a high-performance machine learning framework to build regression and prediction models on any kind of relational data. While I briefly touch on getML’s prediction algorithms, I will mostly exploit its feature learner capabilities.

The dataset used for benchmarking is the well known CORA data set, that includes 2708 scientific publications classified into one of seven classes. The papers reference each other, giving rise to a graph network. Hence, in GNN terminology, the papers are nodes, the references are edges. Words in the papers’ abstract are features of the papers, i.e. node attributes.

Since its creation in 2000, the CORA dataset has facilitated the growth of an entire ecosystem of algorithms in NLP, RL and GNN. [Papers with code](https://paperswithcode.com/sota/node-classification-on-cora) documents and compares performance of cutting edge research on the dataset. As of 2023, the list is topped by an implementation attaining **90.16%** in accuracy. This value is used as a **benchmark**.

![Visual Representation of CORA’s graph structure (from: https://graphsandnetworks.com/the-cora-dataset/)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*PzVoY6ihv_vfVZfE2eCjrQ.png)

## Analysis

Since I am interested in simplicity and ease of implementation, I will start out with an off-the-shelf GNN implementation, compare its performance to the getML standalone solution, and then combine both approaches.

### Standalone solutions

For full implementation details, please check out my [Kaggle notebook](https://www.kaggle.com/code/jankmeyer/cora-relational-learning-vs-graph-neural-networks/notebook). As a baseline model, I constructed a simple GNN embedded in the message passing framework. Using a graph convolutional operator (GCNConv) readily available in pytorch-geometric, I trained the GNN on 70% of the data and tested it on the remaining 30%. With this setting, **87.6%** accuracy was attained. Next, I implemented a [getML standalone solution](https://www.kaggle.com/code/jankmeyer/cora-relational-learning-vs-graph-neural-networks?scriptVersionId=129903249&cellId=35). In this approach I capitalized on getML’s end-to-end prediction capabilities: getML’s “FastProp” feature learner _and_ getML’s XGBoostClassifier to predict the labels. Randomizing over different train/test splits, this approach attains an accuracy of **88.3%**.

### Combine GNN and getML

Now, of course the next question arises: What if I combine the best of both worlds: The predictive power of Graph Neural Networks and FastProp’s ability to condense disparate data into valuable feature information?

So far, the word matrix one-hot-encodes 1433 words per paper’s abstract. That sparse representation does not only seem clumsy and inefficient, it is. getML’s FastProp algorithm aggregates it into a dense matrix, consisting of only 200 but highly discriminating features per node. Subsequently that 200 features were fed to the same off-the-shelf GNN as node attributes, just like before. Averaging over many train test splits, an astounding **92.5%** accuracy was reached. Further results and programmatic implementation can be found in [this notebook](https://www.kaggle.com/code/jankmeyer/getml-and-gnns-a-natural-symbiosis) that investigates this symbiosis in full detail.

That means, without domain knowledge of linkage of academic papers with respect to their contents, without technical expertise of GNNs, and without any efforts and time investment in tinkering with parameters, any data science practitioner beats state of the art implementations by simply adding getML’s feature learner to the mix.

### Consistency of Results

Now, one may object, perhaps I was simply lucky and picked by chance the right GNN configuration. I put this claim to the test and ran large scale trials probing different neural layer implementations. For every layer/optimisation combination I trained on different 30 randomized train test splits. Figure 1 shows how the resulting accuracies were distributed across conditions.

![Figure 1: Predictive accuracies across Layer architecture and Preprocessing condition](https://miro.medium.com/v2/resize:fit:1154/format:webp/0*INdgeFiTdvZprGCa)

It is clear that for each and every layer implementation, the optimized features perform considerably better (each pairwise difference p < 0.001). The numerical values and the differences are shown in table 1. The improvement ranges from 4.1% points to 6.99% points, averaging 5.6% points.

![Table 1: Predictive accuracies across Layer architecture and Preprocessing condition](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*meLey_ynoI6tKbRxSY46hw.png)

What catches the eye is the remarkable consistency of results within the getML optimized condition. The standard deviation of the pooled results in the getML optimized condition with no preprocessing has 35% less spread than the condition without preprocessing. Considering the mere means within each layer condition (see table 1), spread in the getML condition shrinks by even 62%. That means, when using getML’s Feature Learner, it matters much less what layer implementation you end up choosing or how your data set is split, your result will be reliably good.

## Conclusion

As a standalone solution, the getML pipeline slightly outperforms an off-the-shelf GNN implementation (88.3% vs 87.6%). Its true strength, however, lies in its flexibility to build on top of already high performing techniques. getML’s FastProp algorithm embeds a coarse one-hot-encoding in a dense matrix with highly distinguishing features. A simple GNN leverages this highly informative data in predictive accuracies well beyond the state of the art (92.5% vs 90.16%).

The information gain of FastProp’s automatic feature engineering is so significant, that predictive performance remains invariant across train test split randomization and variation of Neural Layer architectures. Computationally expensive experimentation, therefore is much less required.

And here I arrive at the gist of the matter: prepending getML’s feature learner to a Graph Neural Network leads to a

*   massive **improvement** in accuracy, while
*   **eliminating** extensive manual feature engineering and
*   sharply **reducing** the need for computationally costly experimentation.

Whether you are seasoned machine learning engineer or a budding data scientist, getML’s feature learner will boost your models almost effortlessly.

Throughout the article, I used [getML’s community edition](https://github.com/getml/getml-community). Being open source and free of charge it offers the already powerful, brute force based [FastProp][feature-engineering-algorithms-fastprop] algorithm. The [enterprise edition](https://www.getml.com/) takes automated feature engineering then to the next level. Decision Tree based Feature Learning Algorithms ([Multirel][feature-engineering-algorithms-multirel], [Relboost][feature-engineering-algorithms-relboost], [RelMT][feature-engineering-algorithms-relmt]) produce more complex features for even higher predictive model performance.

To learn more about getML, check out its other [use cases][examples-index] or give the [community edition][installation-index] a try on your project. If building high-performance models is something you or your data science team cares about, contact [me and my colleagues][contact-page] from getML at hello@getml.com to explore how we can help you.