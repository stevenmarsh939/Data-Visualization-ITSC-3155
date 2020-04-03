import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV File
df = pd.read_csv('..\Datasets\Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

# Prep Data
# Student Notes
#
# Similar to the stacked bar graph, the multilinechart has different line types that represent different data.
# To differentiate between the different types of lines, trace variables are made during preparation. In this
# instance, there are three trace variables which represent the three line types: death, recovered, and unrecovered.
# All of the line types use date as their x axis variable, and have either death, recovered, or unrecovered as their y
# axis variable. The data for the different line types are collected into one variable "data".

trace1 = go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='Actual Max')
trace2 = go.Scatter(x=df['date'], y=df['actual_min_temp'], mode='lines', name='Min')
trace3 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], mode='lines', name='Mean')
data = [trace1, trace2, trace3]

# Prep layout
# Student Notes
#
# The layout variable holds data for the base graph that the lines will be displayed on. This
# includes the graph’s title, their x and y axis title labels and a designation that the bar graph is
# considered a multiline graph.

layout = go.Layout(title="Temps", xaxis_title="Date", yaxis_title="Temps")

#Plot it and save html
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='tempmultiline.html')