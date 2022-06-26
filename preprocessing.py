import pandas as pd


def preprocessing(
    df: pd.DataFrame,
    threshold: int = None,
    case_types: list = ["Confirmed", "Active", "Deaths"],
    pivot: bool = False,
) -> pd.DataFrame:

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(by=["Date"], ascending=True)

    if threshold:
        df = df.loc[
            df["Confirmed"] >= threshold
        ]  # I think this threshold should only apply to 'Confirmed' cases. This is just meant to eliminate noise from early (mis-)reporting of cases.
        df["days_since_threshold_crossed"] = df.reset_index().index

    if pivot:
        df = df.pivot(index="Date", columns="Country", values=case_types)
    else:
        df.index = df["Date"]
        df = df.drop(columns=["Date"])

    return df
