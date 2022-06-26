from statsmodels.tsa.api import Holt
import numpy as np
import pandas as pd


def holt(y_train, smoothing_level=0.5, smoothing_slope=0.1, forecast_period=50):
    fit1 = Holt(y_train).fit(smoothing_level, smoothing_slope, optimized=False)
    fit2 = Holt(y_train, exponential=True).fit(
        smoothing_level, smoothing_slope, optimized=False
    )

    fcast1 = fit1.forecast(forecast_period).rename("Holt linear trend")
    fcast2 = fit2.forecast(forecast_period).rename("Exponential trend")

    return fcast1, fcast2


def evaluate_model(y_obs, y_pred):
    rmse = np.sqrt(((y_pred - y_obs) ** 2).mean())
    mape = np.mean(np.abs((y_obs - y_pred) / y_obs)) * 100

    return pd.DataFrame({"metric": ["rmse", "mape"], "score": [rmse, mape]})
