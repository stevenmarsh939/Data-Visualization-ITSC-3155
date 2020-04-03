import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/CoronaTimeSeries.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Preparing data
# Student Notes
#
# The data variable holds information about the line in the line chart. This code says that the line's x axis
# value holds a date, the y axis value holds data that corresponds to the number of confirmed cases, and that the line's
# name is "Death". It also specifies that the data is for a line when it sets "mode = line".
#

data = [go.Scatter(x=df['Date'], y=df['Confirmed'], mode='lines', name='Death')]

# Preparing layout
# Student Notes
#
# The layout variable holds data for the base graph that the line will be displayed on. This
# includes the graph’s title and its x and y axis title labels.
#
layout = go.Layout(title='Corona Virus Confirmed Cases From 2020-01-22 to 2020-03-17', xaxis_title="Date", yaxis_title="Number of cases")

# Plot the figure and saving in a html
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')