import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/CoronaTimeSeries.csv')

# Preparing data
# Student Notes
#
# The data variable holds information about the heatgraph squares in the heatgraph.
# This code says that the heatgraph squares x axis hold values for days and its y axis holds
# values for the week of the month. The z variable holds the number that determines what color
# each square will be, and in this case, the z variable changes based on the amount of recovered
# corona virus cases.
#
# The colorscale is the list of colors that the heatmap can use to represent its z variable.
# The colorscale "Jet" must be a premade coloring method that we chose for the graph.
#
data = [go.Heatmap(x=df['Day'],
                   y=df['WeekofMonth'],
                   z=df['Recovered'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
# Student Notes
#
# The layout variable holds data for the base graph that the heatmap will be displayed on. This
# includes the graph’s title, its x and y axis title labels.
#
layout = go.Layout(title='Corona Virus Recovered Cases', xaxis_title="Day of Week", yaxis_title="Week of Month")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')