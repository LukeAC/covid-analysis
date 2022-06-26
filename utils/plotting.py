from src.queries import get_data
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_initial_growth(
    countries: list,
    first_n_days: int = 100,
    case_type: str = "Active",
    threshold: int = 100,
    ax: plt.axis = None,
    title: str = None,
):
    """
    Returns a plot describing the initial growth/propagation of COVID.
    Note: case_type can be one of: Confirmed, Active, Deaths
    """

    _, ax = plt.subplots()

    # add the initial growth trend for each country to the same plot
    for country in countries:
        initial_growth = get_data(
            country, threshold=threshold, first_n_days=first_n_days, preprocess=True
        )
        fig = initial_growth.plot(y=case_type, ax=ax, label=country)

    # clean up plot
    ax.set(ylabel=f"Number of Cases ({case_type})")
    # dtfmt = mdates.DateFormatter("%m-%y")
    # ax.xaxis.set_major_formatter(dtfmt)
    plt.xticks(rotation=45)
    fig.set_title(title)

    return fig, ax
