import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# # Creating sum of number of cases group by Country Column
# df = df.groupby(['NOC']).agg(
# {'Gold': 'sum', 'Silver': 'sum', 'Bronze':
# 'sum'})

# Sorting values and select 20 first value
df = df.sort_values(by=['Total'],
ascending=[False]).head(20)

# Preparing data
trace1 = go.Bar(x=df['NOC'], y=df['Gold'], name='Gold',
marker={'color': '#FFD700'})
trace2 = go.Bar(x=df['NOC'], y=df['Silver'], name='Silver',
marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=df['NOC'], y=df['Bronze'], name='Bronze',
marker={'color': '#CD7F32'})
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='Total Olympic Medals', xaxis_title="Country",
                    yaxis_title="Number of Medals", barmode='stack')
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')