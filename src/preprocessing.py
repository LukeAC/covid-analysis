import pandas as pd


def preprocessing(
    df: pd.DataFrame,
    threshold: int = None,
) -> pd.DataFrame:
    """
    Returns processed df. Converts input df to use a DateTimeIndex, and
    applies a threshold on number of 'Confirmed' cases if one is supplied.
    """

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(by=["Date"], ascending=True)

    if threshold:
        df = df.loc[
            df["Confirmed"] >= threshold
        ]  # I think this threshold should only apply to 'Confirmed' cases. This is just meant to eliminate noise from early (mis-)reporting of cases.
        df["days_since_threshold_crossed"] = df.reset_index().index  # Just in case this is needed

    df.index = df["Date"]
    df = df.drop(columns=["Date"])

    return df
