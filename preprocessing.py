import pandas as pd


def preprocessing(data: pd.DataFrame, threshold: int = None) -> pd.DataFrame:
    data["Date"] = pd.to_datetime(data["Date"])
    data = data.sort_values(by="Date", ascending=True)
    if threshold:
        data = data.loc[data["Confirmed"] >= threshold]
        data["days_since_threshold_crossed"] = data.reset_index().index

    return data
