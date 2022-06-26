from src.queries import get_data
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_initial_growth(
    countries: list,
    first_n_days: int = 100,
    case_types: list = ["Confirmed", "Active", "Deaths"],
    threshold: int = 100,
    ax: plt.axis = None,
    title: str = None,
):
    """
    Returns a plot describing the initial growth/propagation of COVID.
    Note: case_types can contain: Confirmed, Active, Deaths
    """

    _, axes = plt.subplots(len(case_types))

    # add the initial growth trend for each country to the same plot
    for country in countries:
        initial_growth = get_data(
            country, threshold=threshold, first_n_days=first_n_days, preprocess=True
        )
        for i, case_type in enumerate(case_types):
            fig = initial_growth.plot(y=case_type, ax=axes[i], label=country)
            axes[i].set(ylabel=f"Number of Cases ({case_type})")
            fig.set_title(label=f"{first_n_days}-day growth of COVID {case_type} cases past {threshold}-case initial threshold.")


    # clean up plot
    
    # dtfmt = mdates.DateFormatter("%m-%y")
    # ax.xaxis.set_major_formatter(dtfmt)
    plt.xticks(rotation=45)

    return fig, ax
