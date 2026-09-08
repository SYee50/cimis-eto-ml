## ML Experiment Design

## 1. Experiment Overview

The goal of this project is to investigate whether weather-station measurements can be used to predict daily reference evapotranspiration (ETo).

The machine learning experiments are designed based on findings from the exploratory data analysis (EDA). The EDA showed strong relationships between ETo and several weather variables, including solar radiation, air temperature, and relative humidity. It also showed a clear nonlinear seasonal pattern in ETo and differences in environmental conditions across the five CIMIS weather stations.

The experiments will investigate whether the models can outperform simple and linear approaches, whether seasonal information improves prediction, and whether the model can generalize to weather stations that were not represented during training.

The experiments will evaluate:

* Whether the machine learning models outperform the mean baseline.
* Whether the Random Forest improves upon Linear Regression.
* Whether adding Day of Year improves predictive performance.
* Whether model performance changes when predicting an unseen station.

Following the experiments, an error analysis will investigate where the model makes larger prediction errors and whether those errors show systematic patterns.

## 2. Research Questions

The experiments will address the following questions:

1. Can weather-station measurements accurately predict daily ETo?
2. Does a nonlinear model improve ETo prediction compared with a linear model?
3. Does including Jul (Day of Year) improve ETo prediction by capturing seasonal patterns?
4. Can the model generalize to a CIMIS weather stations that were not represented during training?

## 3. Target Variable

The target variable is:

* `ETo (mm)` - daily reference evapotranspiration measured in millimeters.

The model will predict the daily ETo value for each observation.

## 4. Features

### Weather Features

The initial weather feature set will include:

* `Precip (mm)`
* `Avg Sol Rad (W/m²)`
* `Avg Vap Pres (kPa)`
* `Max Air Temp (°C)`
* `Min Air Temp (°C)`
* `Avg Air Temp (°C)`
* `Max Rel Hum (%)`
* `Min Rel Hum (%)`
* `Avg Rel Hum (%)`
* `Dew Point (°C)`
* `Avg Wind Speed (m/s)`

### Seasonal Feature

A second feature set will add;

* `Jul` - Day of Year

The EDA showed that Day of Year has little linear correlation with ETo, but the relationship between Day of Year and ETo is clearly nonlinear and follows a seasonal pattern. Experiment 2 will determine whether including Day of Year improves predictive performance.

### Excluded Variables

The following variables will not be used as model features:

* `Station Number`
* `Station Name`
* `CIMIS Region`
* `Date`

Station identifiers and location labels identify observations rather than representing physical weather measurements. The experiments will focus on predicting ETo from environmental conditions rather than allowing the model to rely directly on station identity.

## 5. Data Splitting Strategy

Two evaluation strategies will be used.

### Standard Train/Test Split

The initial model comparison will use an 80/20 train/test split.

The training set will be used to fit the models, while the test set will be reserved for evaluating predictions on observation that were not used during training.

The test set will not be used during model training.

A fixed random seed of 42 will be used to make the split reproducible.

### Held-Out Station Evaluation

A separate experiment will assess geographic generalization.

For each station, observations from that station will be excluded from training and used as the test set. The model will be trained on the remaining four stations and evaluated on the held-out station.

This process will be repeated for all five CIMIS stations so that each station serves as the held-out test station once.

The five stations are:

* FivePoints
* Davis
* Bishop
* Calipatria/Mulberry

This evaluation provides a more challenging test of geographic generalization than the standard random train/test split because the model does not encounter observations from the held-out station during training.

## 6. Models

The experiments will compare three approaches.

### Mean Baseline

The baseline will predict the mean ETo value calculated from the training data for every test observation.

This establishes a reference point for determining whether the machine learning models provide meaningful predictive improvement.

## Linear Regression

Linear Regression will be used as the initial machine learning model.

This model is motivated by the strong linear relationships identified during EDA between ETo and variables such as:

* Average solar radiation
* Maximum air temperature
* Average air temperature
* Minimum air temperature
* Average relative humidity

### Random Forest

Random Forest will be used as a nonlinear machine learning model.

This model is motivated by the nonlinear relationships observed during EDA, particularly the seasonal relationship between Day of Year and ETo.

Random Forest will also provide a comparison against Linear Regression to determine whether modeling nonlinear relationships improves prediction.

## 7. Evaluation Metrics

Each model will be evaluated using:

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted and actual ETo values.

Lower MAE indicates smaller average prediction errors.

### Root Mean Squared Error (RMSE)

RMSE measures prediction error while placing greater emphasis on larger errors.

Lower RMSE indicates better performance, particularly when large prediction errors are undesirable.

### R²

R² measures how much of the variation in ETo is explained by the model relative to the baseline.

Higher R² generally indicates better predictive performance.

All three metrics will be reported together because they provide different information about model performance.

### 8. Experiments

### Experiment 1: Baseline and Model Comparison

**Research question:**

Can weather-station measurements accurately predict daily ETo?

The following approaches will be compared:

1. Mean baseline
2. Linear Regression
3. Random Forest

The models will use the weather feature set and will be evaluated using the standard 80/20 train/test split.

The results will be compared using MAE, RMSE, and R².

This experiment establishes whether the machine learning models provide predictive value and whether Random Forest improves upon the linear model.

### Experiment 2: Effect of Seasonal Information

**Research question:**

Does including Day of Year improve ETo prediction?

Two feature sets will be compared:

**Weather only**

Weather features.

**Weather + Day of Year**

Weather features + `Jul`.

The models will be evaluated using the same train/test methodology and evaluation metrics.

The difference in performance will indicate whether Day of Year provides useful predictive information beyond the weather measurements.

## Experiment 3: Geographic Generalization

**Research question:**

Can the model predict ETo for CIMIS stations that were not represented during training?

The Random Forest model will be trained using data from four CIMIS stations and evaluated using data from the fifth station.

This process will be repeated for all five stations:

1. FivePoints held out
2. Davis held out
3. Bishop held out
4. Calipatria/Mulberry held out
5. San Luis Obispo held out

For each evaluation, the held-out station will be completely excluded from model training.

Performance will be evaluated using MAE, RMSE, and R².

This experiment provides evidence about whether the model can generalize to environmental conditions from stations that were not represented during training.

## 9. Error Analysis

Following the three experiments, an error analysis will investigate the conditions under which the model makes larger prediction errors.

The analysis will examine:

* Prediction errors by station.
* Prediction errors across different ETo ranges.
* Actual versus predicted ETo values.
* Residuals and their relationship with actual ETo.
* Potential systematic overprediction or underprediction.
* Error patterns under different environmental conditions.

The purpose of the error analysis is to identify patterns that may not be apparent from aggregate MAE, RMSE, and R² values alone.

The error analysis will also help identify potential limitations of the model and areas for future improvement.

## 10. Limitations

The experiments have several limitations.

First, the dataset contains observations from only five CIMIS weather stations. Therefore, successful performance on the selected stations does not establish that the model will generalize to all California environments.

Second, the target variable is the CIMIS-provided calculated reference evapotranspiration value. The model is therefore evaluating its ability to reproduce this target from weather measurements rather than independently measuring actual evapotranspiration.

Third, the standard 80/20 train/test split may contain observations from the same stations and similar environmental conditions in both sets. The held-out station experiment provides a stronger test of geographic generalization.

Fourth, the held-out station evaluation includes only five stations and therefore provides evidence of geographic generalization within the selected dataset rather than proving generalization to arbitrary locations.

Finally, model performance metrics alone do not establish that the model is suitable for operational use. The results must be interpreted alongside error analysis and the conditions represented in the evaluation data.

## 11. Future Extensions

Future iterations of the project may investigate:

* Leave-one-station-out evaluation with additional CIMIS stations.
* Cyclical encoding of Day of Year using sine and cosine transformations.
* Additional machine learning models.
* Hyperparameter tuning.
* Additional CIMIS weather stations.
* Longer historical datasets.
* More detailed error analysis across ETo ranges, stations, and season.
* Model explainability techniques.
* Evaluation under specific environmental conditions or seasons.


