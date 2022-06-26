"""
NOTE: this code was taken/adapted from https://www.bounteous.com/insights/2020/09/15/forecasting-time-series-model-using-python-part-two/
"""

from statsmodels.tsa.api import Holt
import matplotlib.pyplot as plt


def holt(df, y_train, y_test, smoothing_level, smoothing_slope, predict_date):
    df.plot(marker="o", color="black", legend=True, figsize=(14, 7))

    fit1 = Holt(y_train).fit(smoothing_level, smoothing_slope, optimized=False)
    fcast1 = fit1.forecast(predict_date).rename("Holt's linear trend")
    mse1 = ((fcast1 - y_test) ** 2).mean()
    print(
        "The Root Mean Squared Error of Holt"
        "s Linear trend {}".format(round(np.sqrt(mse1), 2))
    )

    fit2 = Holt(y_train, exponential=True).fit(
        smoothing_level, smoothing_slope, optimized=False
    )
    fcast2 = fit2.forecast(predict_date).rename("Exponential trend")
    mse2 = ((fcast2 - y_test) ** 2).mean()
    print(
        "The Root Mean Squared Error of Holt"
        "s Exponential trend {}".format(round(np.sqrt(mse2), 2))
    )

    fit1.fittedvalues.plot(marker="o", color="blue")
    fcast1.plot(color="blue", marker="o", legend=True)
    fit2.fittedvalues.plot(marker="o", color="red")
    fcast2.plot(color="red", marker="o", legend=True)

    plt.show()
