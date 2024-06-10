::: getml.feature_learning
    options:
      members: false

# Feature Learners

Feature Learners are getML's powerhouse leveraging the high performance of C++ to 
ensure efficient execution and effective memory use.

There are five different algorithms, each capitalizing on unique strengths and 
suitable for different use cases. Most of them are available in the 
[getML enterprise edition][getting-started-community-vs-enterprise].

!!! info "Enterprise Edition"
    Tap the full potential of your data with getML's advanced Feature Learners: <br>
    [**Contact us**](https://www.getml.com/contact) and let us tailor your enterprise 
    package today!

## [FastProp][getml.feature_learning.FastProp]
- FastProp utilizes aggregation-based 
operations, enabling rapid generation of numerous features through simple aggregations. This 
makes FastProp ideal for the exploration phase of a data science project, delivering 
quick, decent results. 
- FastProp is available in both, the [getML community edition and getML enterprise 
  edition][getting-started-community-vs-enterprise].


## [Mulitrel][getml.feature_learning.Multirel]
- Multirel focuses on minimizing algorithmic redundancies through incremental 
updates and combining 
these improvements with ensemble learning methods. 
- Recalculations are only performed where changes occur, 
significantly increasing efficiency while 
integrating methods such as bagging and gradient boosting.
- This feature learner is available in the [getML enterprise edition][getting-started-community-vs-enterprise].

## [Relboost][getml.feature_learning.Relboost]
- Relboost extends the gradient boosting approach,
to relational learning by focusing on aggregating learnable weights rather than
columns, addressing computational complexity and exponentially growing feature 
space. 
- While Relboost often surpasses Multirel 
in predictive accuracy and training efficiency, its generated features are less 
intuitive.
- This feature learner is available in the [getML enterprise edition][getting-started-community-vs-enterprise].

## [RelMT][getml.feature_learning.RelMT]
- RelMT adapts linear model trees to relational data, combining linear models at each 
tree leaf to effectively capture both linear and non-linear relationships, making it 
particularly advantageous for modeling time-series data. 
- This feature learner is available in the [getML enterprise edition][getting-started-community-vs-enterprise].
