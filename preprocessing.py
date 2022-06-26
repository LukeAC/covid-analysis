import pandas as pd


def preprocessing(
    df: pd.DataFrame, threshold: int = None, attribute: str = "Confirmed"
) -> pd.DataFrame:
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(by="Date", ascending=True)
    if threshold:
        df = df.loc[df[attribute] >= threshold]
        df["days_since_threshold_crossed"] = df.reset_index().index

    return df
