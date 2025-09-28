import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.dates as mdates
import calendar

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.set_index('date')


# Clean data
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df = df.loc[(df['value'] >= df['value'].quantile(0.025))
& (df['value'] <= df['value'].quantile(0.975))]


df_line_chart = df.copy()

x = df_line_chart['date']
y = df_line_chart['value']

fig = plt.figure(figsize=(8, 6))
plt.plot(df_line_chart['date'], df_line_chart['value'])

plt.xlabel("Date")
plt.ylabel("Page Views")
plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

'''
def draw_line_plot():
    # Draw line plot
    df_line = df.copy()

    fig = plt.figure(figsize=(8, 6))
    plt.plot(df_line['date'], df_line['value'])

    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
'''





'''
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar['months'] = df_bar['date'].dt.month_name()
    df_bar.dropna()

    months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

    df_bar['months'] = pd.Categorical(df_bar['months'], categories=months, ordered=True)
    df_bar = df_bar.groupby(['year','months'])['value'].mean().reset_index(name='average')
    df_bar = df_bar.pivot(index="year", columns="months", values="average")

    fig, ax = plt.subplots(figsize=(10, 8), layout='constrained')

    bar_width = 0.05
    x = np.arange(len(df_bar))
    for i, sub_cat in enumerate(df_bar.columns):
        ax.bar(x + i * bar_width, df_bar[sub_cat], width=bar_width, label=sub_cat)

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months", loc='upper left')
    ax.set_xticks(x + bar_width / 2)
    ax.set_xticklabels(df_bar.index)
    ax.tick_params(axis='x', labelrotation=90)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
'''


