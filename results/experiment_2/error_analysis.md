## Actual vs. Predicted ETo

The actual-versus-predicted plots for Weather Only and Weather + Day of Year models show very similar patterns. Both models exhibit a strong positive relationship between actual and predicted ETo, with observations clustered closely around the 1:1 reference line.

The high density of overlapping observations causes the main cluster to appear as a thick line, making many individual observations difficult to distinguish. Only a relatively small number of observations appear substantially separated from the main cluster.

The similarity between the two plots is consistent with the small difference in their aggregate performance metrics. Adding Day of Year does not produce a substantial visual change in the relationship between actual and predicted ETo.

## Error Distribution

The prediction-error distributions for both models are strongly concentrated around zero.

For the Weather Only model, the highest frequency occurs at approximately zero error, followed by the neighboring positive and negative error ranges. The frequency decreases rapidly as the error moves away from zero, with relatively few observations beyond approximately +0.5 mm or -0.6 mm.

The Weather + Day of Year model shows a similar distribution. Its highest frequency occurs slightly above zero, followed by a rapid decrease in frequency toward approximately ±0.5 mm. Observations become very sparse beyond approximately +0.5 mm and -0.7 mm.

The concentration of errors around zero is consistent with the near-zero mean signed errors of both models. Overall, the plots indicate that most predictions have relatively small errors, with only a small number of larger errors.

## Error vs. Actual ETo

The error-versus-actual ETo plots for both models show that predictions are generally clustered around the zero-error reference line.

The Weather Only model appears to have slightly tighter clustering around the zero-error line, while the Weather + Day of Year model shows slightly greater dispersion. However, the difference is small, and both models remain relatively tightly clustered overall.

The lower ETo ranges appear to have somewhat tighter clustering around zero error. This is consistent with the ETo-range analysis, which shows that mean absolute error generally increases as actual ETo increases.

For the Weather Only model, MAE increases from 0.0789 mm in the 0-2 mm range to 0.2556 mm in the >8 mm range. The Weather + Day of Year model shows a similar pattern, increasing from 0.0769 mm to 0.2588 mm.

Overall, the error-versus-actual plots suggest that both models perform well across most of the observed ETo range, while higher ETo values are associated with somewhat greater prediction error.