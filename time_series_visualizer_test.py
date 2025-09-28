import matplotlib.pyplot as plt
import pandas as pd
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
    df_bar['year'] = pd.DatetimeIndex(df_bar['Date']).year
    df_bar['month'] = pd.DatetimeIndex(df_bar['Date']).month
    # Draw bar plot

    fig = plt.figure(figsize=(8, 6))
    plt.plot(df_bar['date'], df_bar['value'])

    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
'''


df_bar = df.copy()
df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month
#df_bar['month'] = calendar.month_name[df_bar['month']]

result = df_bar.dt.month_name(locale = 'English')
print(result.head())

df_bar = df_bar.drop(columns=['date'])

#print(df_bar.head())

#print(df_bar.groupby(['year','month']).mean())

#df_bar = pd.melt(df_bar, id_vars=['year','month'], value_vars=['value'])
#df_bar = df_bar.groupby(['year', 'month', 'value'])['year'].mean().reset_index(name='average')


'''
df_bar = df.copy()
fig = plt.figure(figsize=(8, 6))
plt.plot(df_bar['year'], df_bar['value'])
plt.xlabel("Date")
plt.ylabel("Page Views")

plt.xlabel("Years")
plt.ylabel("Average Page Views")
'''
