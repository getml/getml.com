# FastProp Benchmarks

A compilation of benchmark notebooks that demonstrate and compare the performance of getML's [`FastProp`][getml.feature_learning.FastProp] algorithm against various implementations of other propositionalization algorithms across different datasets.

!!! Note
    [`FastProp`][getml.feature_learning.FastProp] (short for fast propositionalization) is an open source [Feature Learner][feature-engineering-algorithms] and available in the getML [Community Edition][enterprise-feature-list].

## Results

<p align="center" style="text-align: center;">
    <img src="https://github.com/getml/getml-demo/blob/master/fastprop_benchmark/comparisons/nrpf_performance.png?raw=true" />
</p>

|                                      | Faster vs. featuretools | Faster vs. tsfresh | Remarks                                                                                                                                                                               |
| ------------------------------------ | ----------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Air pollution](air_pollution_prop.ipynb) | ~65x                    | ~33x               | The predictive accuracy can be significantly improved by using RelMT instead of propositionalization approaches, please refer to [this notebook](../air_pollution.ipynb).                     |
| [Dodgers](dodgers_prop.ipynb)            | ~42x                    | ~75x               | The predictive accuracy can be significantly improved by using the mapping preprocessor and/or more advanced feature learning algorithms, please refer to [this notebook](../dodgers.ipynb). |
| [Interstate94](interstate94_prop.ipynb)  | ~55x                    |                    |                                                                                                                                                                                       |                                                                                                                                                                                       |
| [Occupancy](occupancy_prop.ipynb)        | ~87x                    | ~41x               |                                                                                                                                                                                       |
| [Robot](robot_prop.ipynb)                | ~162x                   | ~77x               |                                                                                                                                                                                       |

## Source

These notebooks are published on the [getml-demo](https://github.com/getml/getml-demo/tree/master/fastprop_benchmark) repository.