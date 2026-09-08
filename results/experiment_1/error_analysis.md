# Experiment 1 Error Analysis

## Objective

Experiment 1 evaluates whether machine learning models can improve ETo prediction compared with a simple mean baseline. Error analysis was used to examine the distribution and magnitude of prediction errors and to identify differences between Linear Regression and Random Forest.

## Overall Error

The baseline produced substantially larger errors than either machine learning model. Its mean absolute error was 1.9553 mm, compared with 0.2578 mm for Linear Regression and 0.1380 mm for Random Forest. This indicates that both machine learning models provide substantially more accurate predictions than simply predicting the mean ETo value.

The baseline also had a much larger error range, with absolute errors reaching 6.2700 mm. In comparison, the maximum absolute error was 2.2583 mm for Linear Regression and 2.6489 mm for Random Forest.

Both machine learning models had mean signed errors close to zero, indicating little overall systematic bias. Linear Regression had a mean error of 0.0008 mm, while Random Forest had a mean error of -0.0053 mm.

Overall, Random Forest produced the smallest errors among the three approaches and substantially outperformed both the baseline and Linear Regression.

## Error by ETo Range

Prediction error varied across the observed ETo ranges.

For the baseline, mean absolute error was highest in the >8 mm range at 4.4553 mm and in the 0-2 mm range at 3.0149 mm. The 2-5 mm range had the lowest baseline error at 0.9421 mm.

Linear Regression had lower errors than the baseline across every ETo range. Its mean absolute error ranged from 0.2010 mm in the 2-5 mm range to 0.6155 mm in the >8 mm range.

Random Forest produced the lowest mean absolute error in every ETo range. Its mean absolute error ranged from 0.0789 mm in the 0-2 mm range to 0.2556 mm in the >8 mm range.

Both machine learning models therefore show a general increase in error as actual ETo increases, although Random Forest maintains lower errors across the full range.

## Actual vs. Predicted ETo

The actual-versus-predicted plots for both Linear Regression and Random Forest show a strong positive relationship, with observations clustered around the 1:1 reference line.

Random Forest shows a tighter clustering pattern around the reference line than Linear Regression. Linear Regression shows slightly more dispersion, particularly near the lower ETo range around 0-1 mm and the higher range above 8 mm, although the difference at these extremes is not pronounced.

The stronger clustering around the reference line for Random Forest is consistent with its lower MAE and RMSE compared with Linear Regression.

## Error Distribution

The prediction-error distributions show that Random Forest produces a tighter concentration of errors around zero than Linear Regression.

Linear Regression has measurable error frequencies across a wider range, approximately from -1 mm to 1 mm, before the distribution becomes extremely sparse. Its highest frequency occurs slightly above zero, with zero error occurring at nearly the same frequency, followed by a rapid decrease in frequency.

Random Forest has a narrower range of meaningful error frequencies, concentrated approximately between -0.6 mm and 0.5 mm before tapering to very sparse frequencies. Its highest frequency occurs at zero error, followed by a relatively rapid decrease in frequency as the error moves away from zero.

The tighter error distribution for Random Forest indicates that its predictions are generally closer to the actual ETo values, with fewer moderate prediction errors.

## Error vs. Actual ETo

The error-versus-actual ETo plots show that both machine learning models have errors generally clustered around the zero-error reference line, but the patterns differ between the two models.

For Linear Regression, the observations are more tightly clustered around the zero-error line through the middle of the ETo range, while the lower range below approximately 1 mm and the higher range above 8 mm show greater dispersion and more outliers.

Random Forest shows relatively consistent clustering around the zero-error line across the full range from approximately 0 to 8 mm. The lower half of this range appears slightly more tightly clustered, primarily because there are fewer outliers, although the difference in dispersion between the lower and upper portions is small.

Overall, Random Forest shows tighter clustering around the zero-error line than Linear Regression, with fewer noticeable outliers across most of the observed ETo range. This is consistent with its lower MAE and RMSE.

## Interpretation

The error analysis provides additional evidence that Random Forest performs better than Linear Regression for this ETo prediction task.

Both models substantially outperform the mean baseline, demonstrating that the weather measurements contain useful information for predicting ETo. Random Forest produces a tighter actual-versus-predicted relationship, a narrower error distribution, and lower error across every ETo range examined.

The errors for both machine learning models are generally concentrated around zero, indicating little overall systematic bias. However, error increases as actual ETo increases, particularly in the highest ETo range. This suggests that higher ETo conditions may be more difficult for the models to predict accurately and represent an area for further investigation.

## Conclusion

Experiment 1 shows that machine learning models provide substantially more accurate ETo predictions than a simple mean baseline. Random Forest performs better than Linear Regression across the overall test set and across each ETo range examined.

The visual error analysis supports the numerical results, with Random Forest showing tighter clustering around the 1:1 reference line and zero-error line and a narrower distribution of prediction errors. Although both models perform well overall, the increased error at higher ETo values suggests that additional analysis of high-ETo conditions may help identify opportunities for future model improvement.