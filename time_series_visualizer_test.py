import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.dates as dates

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.set_index('date')

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025))
& (df['value'] <= df['value'].quantile(0.975))]


    plt.figure(figsize=(8, 6))

    plt.plot(df['date'], df['value'])
    plt.locator_params(axis='x', nbins=4)
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.show()
