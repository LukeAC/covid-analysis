import datetime as dt
import requests
import pandas as pd
import time

from preprocessing import preprocessing

today = "{}".format(dt.date.today())


def get_locations():
    url = f"https://api.covid19api.com/countries"
    r = requests.get(url=url)
    return r.json()


def get_data(
    countries: list = ["Canada"],
    threshold: int = None,
    first_n_days: int = None,
) -> pd.DataFrame:

    country_dfs = []

    for loc in countries:
        url = f"https://api.covid19api.com/dayone/country/{loc}"
        r = requests.get(url=url)

        if len(r.json()) < 2:
            available_countries = get_locations()
            suggestions = [
                x["Country"]
                for x in available_countries
                if x["Country"].startswith(loc[0].upper())
            ]
            raise (
                ValueError(
                    f"{loc} is not a valid country name. Country names starting with '{loc[0].upper()}' include {', '.join(suggestions)}"
                )
            )

        else:
            df = preprocessing(pd.DataFrame(r.json()), threshold=threshold)

            if first_n_days:
                df = df.iloc[:first_n_days]
            else:
                pass

            country_dfs.append(df)

        time.sleep(
            0.1
        )  # Just so that we don't get flagged if querying many countries at once

    df = pd.concat(i for i in country_dfs)

    return df
