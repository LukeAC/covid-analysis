import datetime as dt
import requests
import pandas as pd
import time

from .preprocessing import preprocessing

today = "{}".format(dt.date.today())


def get_locations():
    """
    Returns json of available locations (countries) for which data
    can be queried from the free Covid-19 API 
    """
    
    url = f"https://api.covid19api.com/countries"
    r = requests.get(url=url)
    return r.json()


def get_data(
    country: str = "Canada",
    threshold: int = None,
    first_n_days: int = None,
    preprocess: bool = True,
) -> pd.DataFrame:
    """
    Returns pd.DataFrame of API response for the specified country.
    If first_n_days, and threshold are provided: applies a filter to only
    return the first N days after a threshold of 'Confirmed' cases is surpassed.
    """

    url = f"https://api.covid19api.com/dayone/country/{country}"
    r = requests.get(url=url)

    if len(r.json()) < 2:
        available_countries = get_locations()
        suggestions = [
            x["Country"]
            for x in available_countries
            if x["Country"].startswith(country[0].upper())
        ]
        raise (
            ValueError(
                f"{country} is not a valid country name. Country names starting with '{country[0].upper()}' include {', '.join(suggestions)}"
            )
        )

    else:
        df = pd.DataFrame(r.json())
        if preprocess:
            df = preprocessing(df, threshold=threshold)
        if first_n_days:
            df = df.iloc[:first_n_days]

    return df


def batch_get_data(
    countries: list,
    threshold: int = None,
    first_n_days: int = None,
    preprocess: bool = True,
) -> pd.DataFrame:
    return pd.concat(
        get_data(country, threshold, first_n_days, preprocess)
        for country in countries
        if time.sleep(0.1) is None
        # Adding sleep here to not risk bothering the API
    )
