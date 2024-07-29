---
template: home.html
hide:
  - toc
  - navigation
  - feedback
---

<center>

[**What's new?** | getML 1.5 release &rarr;](#)
{: .pill }

</center>


# Your <span class="accent">ML suite</span> for relational <br>and time-series data. {: .h1-lg }

GetML Relational Learning unlocks a 10x speed-up potential and superior model performance. <br class="show-lg">
A game changer in predictive applications for enterprise applications.
{: .lead .big-lg .mb-2-lg }


<center class="mb-3-lg">

[Request a demo](enterprise/book-demo){ .md-button .md-button--primary }
[API Reference](reference){ .md-button }
{: .spacer }

</center>


<center class="mb-4-lg">

<span class="impact">Powering the world’s best machine learning pipelines.</span><br>
<span class="mute">From next-gen startups to established enterprises.</span>
{: .medium-lg }


/// html | div.logo_grid.mb-5-lg
:c-ao:

:c-si:

:c-pw:

:c-em:

:c-ge:

:c-pe:

:c-ze:

:c-v:
///


</center>

<center>
<div class="box box-bg why-getml mb-4-lg" markdown>

## :fontawesome-pro-duotone-layer-plus:{.accent} Why you should consider getML {: .h2-md .w-25-lg }

Finally smooth pipeline
{: .hidden }

<div class="w-75-lg medium-lg" markdown>

GetML introduces new ML algorithms that empower data scientists to achieve superior model performance without the burden of manual feature engineering and building complex feature pipelines. By generalizing gradient boosting to multi-relational decision trees, getML brings supervised learning to raw relational data, enabling end-to-end prediction pipelines. The getML suite provides an easy to use Python API, adhering to modern standards.

GetML is developed by Code17 GmbH, and is used across industries, from finance and manufacturing to healthcare and beyond.

</div>

</div>
</center>


## The right getML flavor for your application {: .h2-lg .center-lg .mb-1-lg }

There are two different getML flavoour out there. We give you all you need.
{: .medium-lg .mute .center-lg .mb-3-lg }


/// html | div

## The better solution for enterprise grade predictive analytics applications

### Makes Data Science fun again

High perfomance models require 10x less code. Howl new feeling of purpose.


### Sheer performance

### Range of evaluated features

Good models require hundreds of features and they can change all the time.
Good feature stores contain 100 of features. but what if they change? getML is your push button solution to learn form billions of features and search new any time.
GetML learns from billions of features

1bn
range of evaluated features

///


<div class="container mb-4-lg" markdown>
<div class="box box-bg box-50" markdown>

### :fontawesome-pro-duotone-user-group:{.accent} Community Edition
For anyone who worked with Prophet, tsfresh or FeatureTools and is looking for a more memory and run-time efficient solution. GetML Community is the leading open source implementation of the propositionalization framework.


[Get started](install){ .md-button }

</div>
<div class="box box-bg box-50" markdown>

### :fontawesome-pro-duotone-industry:{.accent} Enterprise Edition
This is your choice if shorter development cycles and unprecedented model accuracy provide a competitive edge to your business. GetML Enterprise gives you access to the most advanced Relational Learning algorithms.

[Learn more](enterprise/benefits.md){ .md-button }

</div>
</div>

/// html | div.full-width-bg-lg

<div class="hidden clear-lg"></div>

#### FOR THOSE WHO CODE {.accent}
## Whats under the hood? {.h2-lg .center-lg .mb-1-lg}

: For performance reason everything is written in C++

: Comes with a nice python API


``` py linenums="1"
# Launch the engine
import getml
getml.engine.launch() # (1)!
getml.engine.set_project('quick_rundown')

# Load the data into the engine
df_population = getml.data.DataFrame.from_csv('data_population.csv', name='population_table')
df_peripheral = getml.data.DataFrame.from_csv('data_peripheral.csv',name='peripheral_table')

# Annotate the data
df_population.set_role(cols='target', role=getml.data.role.target)
df_population.set_role(cols='join_key', role=getml.data.role.join_key)

# Define the data model
dm = getml.data.DataModel(population=df_population.to_placeholder())
dm.add(df_peripheral.to_placeholder())
dm.population.join(dm.peripheral, on="join_key")

# Define the feature learners
fast_prop = getml.feature_learning.FastProp()
relboost = getml.feature_learning.Relboost()

# Train the feature learning algorithm and the predictor
pipe = getml.pipeline.Pipeline(
    data_model=dm,
    feature_learners=[fast_prop, relboost],
    predictors=getml.predictors.LinearRegression()
)
pipe.fit(population=df_population, peripheral=[df_peripheral])

# Evaluate
pipe.score(population=df_population_unseen, peripheral=[df_peripheral_unseen])

# Predict
pipe.predict(population=df_population_unseen, peripheral=[df_peripheral_unseen])

# Allow the pipeline to respond to HTTP requests
pipe.deploy(True)
```

1.  Look ma, less line noise!
2.  Annotation on first line (appended)


dont care about specifics and just want top performing models?


### **Getting started is easy**

1. read through our user guide
2. `pip install getml`
3. `checkout our example repository` to get started with our getML community edition


<div class="hidden clear-lg"></div>

///


<div class="container mb-4-lg pt-4-lg" markdown>
<div class="box box-lg box-50 p-sm-0 mb-sm-0" markdown>

## Interested in getML Relational Learning? {: .h2-big .mb-sm-0}

</div>
<div class="box box-50 p-sm-0" markdown>
Request a meeting to explore the potential of GetML Relational Learning for your business application. Or check out one of our code examples before.

[Talk to sales](contact){ .md-button .md-button--primary }
[Get started](user_guide){ .md-button  }
</div>

</div>
