---
title: Feature Learning
---

::: getml.feature_learning
    options:
      members: false
      show_docstring_description: false

[Feature Learners][feature-engineering-algorithms] are getML's powerhouse leveraging 
the high performance of C++ to ensure efficient execution and effective memory use.

There are five different algorithms, each capitalizing on unique strengths and 
suitable for different use cases. Most of them are available in the 
[getML Enterprise edition][enterprise-feature-list].


## [`FastProp`][getml.feature_learning.FastProp]
- FastProp utilizes aggregation-based 
operations, enabling rapid generation of numerous features through simple aggregations. This 
makes FastProp ideal for the exploration phase of a data science project, delivering 
quick, decent results. 
- FastProp is available in both, the [getML Community edition and getML enterprise 
  edition][enterprise-feature-list].


## [`Multirel`][getml.feature_learning.Multirel]
- Multirel focuses on minimizing algorithmic redundancies through incremental 
updates and combining 
these improvements with ensemble learning methods. 
- Recalculations are only performed where changes occur, 
significantly increasing efficiency while 
integrating methods such as bagging and gradient boosting.
- This feature learner is available in the [getML Enterprise edition][enterprise-feature-list].

## [`Relboost`][getml.feature_learning.Relboost]
- Relboost extends the gradient boosting approach,
to relational learning by focusing on aggregating learnable weights rather than
columns, addressing computational complexity and exponentially growing feature 
space. 
- While Relboost often surpasses Multirel 
in predictive accuracy and training efficiency, its generated features are less 
intuitive.
- This feature learner is available in the [getML Enterprise edition][enterprise-feature-list].

## [`Fastboost`][getml.feature_learning.Fastboost]

- Fastboost uses a simpler, faster, and more scalable algorithm than Relboost, making 
it ideal for large datasets and many cross-joins. Fastboost can outperform FastProp 
in speed for datasets with many columns.

-  Fastboost requires free disk space due to extensive memory mapping and has 
difficulty applying to multiple targets as it must learn separate rules for each.

- This feature learner is available in the [getML Enterprise edition][enterprise-feature-list].


## [`RelMT`][getml.feature_learning.RelMT]
- RelMT adapts linear model trees to relational data, combining linear models at each 
tree leaf to effectively capture both linear and non-linear relationships, making it 
particularly advantageous for modeling time-series data. 
- This feature learner is available in the [getML Enterprise edition][enterprise-feature-list].
