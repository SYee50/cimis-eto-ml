# Experiment 3 Error Analysis

## 1. Overview

This analysis evaluated the prediction errors by the Random Forest model in Experiment 3. The goal is to determine how closely the model predictions match the observed reference evapotranspiration (ETo) values and identify whether prediction accuracy varies from stations or ETo ranges.

The test set contains 9,051 observations. Prediction error is defined as:

`Error = Predicted ETo - Observed ETo`

A positive error indicates that the model overpredicted ETo, while a negative error indicates that the model underpredicted ETo. Absolute error is used to evaluate the magnitude of prediction errors regardless of direction.

## 2. Overall Error

The mean prediction error was **0.0043 mm**, with a median error of **0.0279 mm**. The mean error being very close to zero indicates that the model has little overall systematic bias toward overprediction or underprediction.

The mean absolute error was **0.2164 mm**, while the median absolute error was **0.1491 mm**. The 25th and 75th percentiles of absolute error were **0.0648 mm** and **0.2839 mm**, respectively. This indicates that the majority of predictions have relatively small errors.

The largest absolute error was **3.8041 mm**. Although this is substantially larger than the typical error, it represents an extreme observation rather than the general behavior of the model.

## 3. Error Distribution

The error distribution is strongly concentrated around zero. The histogram shows the highest frequency of observations near zero error, with the frequency decreasing rapidly as the magnitude of the error increases.

Most errors appear to fall within approximately **±0.5 mm**, while relatively few observations have errors approaching ±1 mm or greater. The distribution also does not show a strong shift toward either positive or negative errors, which is consistent with the overall mean error of only 0.0043 mm.

Overall, the error distribution suggests that the Random Forest model generally produces predictions close to the observed ETo values without substantial systematic bias.

## 4. Error vs. Actual ETo

The error-versus-actual-ETo plot shows that most observations remain concentrated around the zero-error line across the majority of the ETo range.

From approximately 0 to 8 mm of observed ETo, the points form a dense band around zero. The large number of overlapping observations makes the band appear thick, but this primarily reflects the high concentration of observations rather than consistently large errors.

At higher ETo values, particularly above approximately 8 mm, the errors show greater dispersion. This is consistent with the ETo range analysis, where the mean and median absolute errors increase as the observed ETo value increases.

This suggests that the model performs best at lower and moderate ETo values but may have more difficulty maintaining the same level of accuracy under higher-ETo conditions.

## 5. Error by Station

Mean absolute error varied across the five stations:

| Station             | Mean Absolute Error (mm) | Median Absolute Error (mm) | Maximum Error (mm) |
| ------------------- | -----------------------: | -------------------------: | -----------------: |
| Bishop              |                   0.2677 |                     0.2126 |             1.7521 |
| Calipatria/Mulberry |                   0.2776 |                     0.1810 |             3.8041 |
| Davis               |                   0.1623 |                     0.1152 |             3.5455 |
| FivePoints          |                   0.2042 |                     0.1323 |             2.9481 |
| San Luis Obispo     |                   0.1712 |                     0.1273 |             3.6181 |

Davis had the lowest mean absolute error at **0.1623 mm**, followed by San Luis Obispo at **0.1712 mm**. Calipatria/Mulberry had the highest mean absolute error at **0.2776 mm**, followed closely by Bishop at **0.2677 mm**.

The maximum errors were substantially larger than the typical errors at several stations. In particular, Calipatria/Mulberry had the largest observed error at **3.8041 mm**. This indicates that while typical prediction errors remain relatively small, some individual observations produce much larger errors.

The difference between stations suggest that model performance may depend partly on the environmental conditions represented by each station.

## 6. Error by ETo Range

Prediction error increased as observed ETo increased:

| ETo Range | Mean Absolute Error (mm) | Median Absolute Error (mm) | Maximum Error (mm) | Observations |
| --------- | -----------------------: | -------------------------: | -----------------: | -----------: |
| 0–2 mm    |                   0.1316 |                     0.0797 |             1.7523 |        1,750 |
| 2–5 mm    |                   0.1960 |                     0.1507 |             2.0693 |        3,888 |
| 5–8 mm    |                   0.2501 |                     0.1875 |             3.8041 |        2,946 |
| >8 mm     |                   0.4917 |                     0.4017 |             2.5641 |          467 |

The model had the lowest error for observations with ETo between 0 and 2 mm, with a mean absolute error of **0.1316 mm** and a median absolute error of **0.0797 mm**.

Error increased through the 2-5 mm and 5-8 mm ranges. For observations above 8 mm, the mean absolute error increased to **0.4917 mm** and the median absolute error increased to **0.4017 mm**.

The >8 mm range contains only 467 observations, substantially fewer than the other ranges. However, the increase in error is consistent with the greater dispersion observed in the error-versus-actual-ETo plot.

These results indicate that higher-ETo conditions represent a more challenging prediction range for the model.

## 7. Actual vs. Predicted ETo

The actual-versus-predicted plot shows a strong positive relationship between observed and predicted ETo values. Most observations are concentrated close to the 1:1 reference line, indicating that predicted values generally track the observed ETo values well.

The dense concentration of points below approximately 8 mm makes individual observations difficult to distinguish visually. However, the concentration around the 1:1 line indicates that the model is generally producing predictions close to the observed values in this range.

Greater derivation from the expected relationship is visible among some higher-ETo observations, which is consistent with the increased error observed in the ETo-range analysis.

## 8. Summary

Overall, the Experiment 3 Random Forest model demonstrates relatively strong prediction performance on the test set. Across 9,051 observations, the model produced a mean absolute error of **0.2164 mm** and a median absolute error of **0.1491 mm**. The mean prediction error of **0.0043 mm** was very close to zero, indicating little overall systematic bias.

The error distribution is strongly concentrated around zero, and the error-versus-actual-ETo analysis shows that errors remain relatively small across most of the observed ETo range. Model performance does, however, decline as ETo increases, with the largest mean and median absolute errors occurring for observations above 8 mm.

Performance also varies between stations, with Davis and San Luis Obispo showing lower typical errors than Bishop and Calipatria/Mulberry.

The primary area for further investigation is therefore **high-ETo prediction performance**. Future experiments could examine which environmental conditions, features, or station characteristics contribute to the larger errors observed at higher ETo values. These findings can be used to guide subsequent model improvements and experiments.