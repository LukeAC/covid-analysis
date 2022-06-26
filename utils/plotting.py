from queries import get_data
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_initial_growth(
    countries: list,
    first_n_days: int = 100,
    case_type: str = "Confirmed",
    threshold: int = 100,
    ax: plt.axis = None,
    title: str = None,
):
    """
    Returns a plot describing the initial growth/propagation of COVID.
    Note: case_type can be one of: Confirmed, Active, Deaths
    """
    if not ax:
        _, ax = plt.subplots()

    ax.set(ylabel=f"Number of Cases ({case_type})")

    for country in countries:
        initial_growth = get_data(
            [country], threshold=threshold, first_n_days=first_n_days
        )
        plot = initial_growth.plot("Date", case_type, ax=ax, label=country)

    myFmt = mdates.DateFormatter("%m-%y")
    ax.xaxis.set_major_formatter(myFmt)
    plt.xticks(rotation=45)

    plot.set_title(title)

    return plot, ax
