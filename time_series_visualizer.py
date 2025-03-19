import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data: Remove top and bottom 2.5% outliers
low_threshold = df["value"].quantile(0.025)
high_threshold = df["value"].quantile(0.975)
df = df[(df["value"] >= low_threshold) & (df["value"] <= high_threshold)]


def draw_line_plot():
    """Draws a line plot of daily page views."""
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df["value"], color="red", linewidth=1)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    """Draws a bar plot of average monthly page views grouped by year."""
    df_bar = df.copy()
    df_bar["Year"] = df_bar.index.year
    df_bar["Month"] = df_bar.index.month

    df_bar = df_bar.groupby(["Year", "Month"])["value"].mean().unstack()

    fig = df_bar.plot(kind="bar", figsize=(12, 6)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=[
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ])

    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    """Draws two box plots to show trends and seasonality in page views."""
    df_box = df.copy()
    df_box["Year"] = df_box.index.year
    df_box["Month"] = df_box.index.strftime("%b")

    # Pastikan kolom "value" bertipe float
    df_box["value"] = df_box["value"].astype(float)

    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Year-wise box plot
    sns.boxplot(x="Year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(x="Month", y="value", data=df_box, order=month_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig

