import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/CoronavirusTotal.csv')
# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating unrecovered column
df['Unrecovered'] = df['Confirmed'] - df['Deaths'] - df['Recovered']

# Removing China and Others from data frame
df = df[(df['Country'] != 'China') & (df['Country'] != 'Others')]

# Creating sum of number of cases group by Country Column
new_df = df.groupby(['Country']).agg(
    {'Confirmed': 'sum', 'Recovered': 'sum', 'Unrecovered': 'sum'}).reset_index()

# Preparing data
# Student Notes
#
# The data variable holds information about the bubbles in the bubblechart. This code says that the bubbles x axis
# holds values for recovered cases and its y axis holds values for unrecovered cases. The text variable says that
# each bubble represents a country, and that the text displayed when hovering over each bubble will be a country's name.
# Setting the mode to markers indicates that this data is for bubbles in a
# bubblechart. The marker variable deals with the sizing of bubbles and the coloring of the graph's bubbles.
# Showscale = true means that the color gradient scale will be displayed on the finalized graph.
#
data = [
    go.Scatter(x=new_df['Recovered'],
               y=new_df['Unrecovered'],
               text=new_df['Country'],
               mode='markers',
               marker=dict(size=new_df['Confirmed'] /
                           100,color=new_df['Confirmed'] / 100, showscale=True))
                           ]

# Preparing layout
# Student Notes
#
# The layout variable holds data for the base graph that the bubbles will be displayed on. This
# includes the graph’s title and its x and y axis title labels. The hovermode variable is set to closest, which means
# that whatever bubble is the closest to the user's mouse pointer is that one that will be displayed.
#
layout = go.Layout(title='Corona Virus Confirmed Cases', xaxis_title="Recovered Cases", yaxis_title="Unrecovered Cases", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')