import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

app = dash.Dash()

# Line Chart
df1 = pd.read_csv('../Datasets/Weather2014-15.csv')
df1['date'] = pd.to_datetime(df1['date'])

# Preparing data
data_linechart = [go.Scatter(x=df1['date'], y=df1['actual_max_temp'], mode='lines', name='actual_max_temp')]

# Preparing layout
layout = go.Layout(title='Max Temperature of Each Month for 2014 - 2015', xaxis_title="Month for 2014 - 2015",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
#fig = go.Figure(data=data_linechart, layout=layout)
#pyo.plot(fig, filename='linechart.html')

# Multi-Line Chart
df2 = pd.read_csv('..\Datasets\Weather2014-15.csv')
df2['date'] = pd.to_datetime(df2['date'])

trace1 = go.Scatter(x=df2['date'], y=df2['actual_max_temp'], mode='lines', name='Actual Max')
trace2 = go.Scatter(x=df2['date'], y=df2['actual_min_temp'], mode='lines', name='Min')
trace3 = go.Scatter(x=df2['date'], y=df2['actual_mean_temp'], mode='lines', name='Mean')
data_multilinechart = [trace1, trace2, trace3]

layout = go.Layout(title="Temps", xaxis_title="Date", yaxis_title="Temps")

#fig = go.Figure(data=data_multilinechart, layout=layout)
#pyo.plot(fig, filename='tempmultiline.html')

# Bubble Chart
df3 = pd.read_csv('../Datasets/Weather2014-15.csv')
df3 = df3.apply(lambda x : x.str.strip() if x.dtype == "object" else  x)

new_df = df3.groupby(['month']).agg(
    { 'actual_max_temp': 'mean', 'actual_min_temp': 'mean'}).reset_index()
data_bubblechart = [
    go.Scatter(x=new_df['actual_max_temp'],
               y=new_df['actual_min_temp'],
               mode='markers',
               marker=dict(size=30, color=10, showscale=True),
               text=new_df["month"]
               )
]
layout = go.Layout(title='Max and Min temp per Month', xaxis_title="Max temp",
                   yaxis_title="Min temp", hovermode='closest')
#fig = go.Figure(data=data_bubblechart, layout=layout)
#pyo.plot(fig, filename='WeatherBubblechart.html')

# Heatmap
# Preparing data
df4 = pd.read_csv('../Datasets/Weather2014-15.csv')

data_heatmap = [go.Heatmap(x=df4['day'],
                   y=df4['month'],
                   z=df4['actual_max_temp'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='Max Temperature on Day of Week and Month of Year', xaxis_title="Day of Week",
                   yaxis_title="Month")

# Plot the figure and saving in a html file
#fig = go.Figure(data=data_heatmap, layout=layout)
#pyo.plot(fig, filename='heatmapweather.html')

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('2014 - 2015 weather data', style={'textAlign': 'center'}),
    #
    html.Br(),
    html.Br(),
    html.Br(),

    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Weather Line Chart', style={'color': '#df1e56'}),
    html.Div('The line chart shows the max temperatures of each month for 2014 - 2015.'),
    dcc.Graph(id='graph1',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Max Temperatures', xaxis_title="Month for 2014 - 2015", yaxis_title="Temperature")
              }),

    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multiple Line Chart', style={'color': '#df1e56'}),
    html.Div(
        'This chart shows us the actual, min and mean temperatures of weather from 2014 - 2015.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_multilinechart,
                  'layout': go.Layout(title="Temps", xaxis_title="Date", yaxis_title="Temps")
              }),

    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart of temperatures.', style={'color': '#df1e56'}),
    html.Div(
        'This bubble chart shows a different representation of temperature data.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_bubblechart,
                  'layout': go.Layout(title='Max and Min temp per Month', xaxis_title="Max temp",
                   yaxis_title="Min temp", hovermode='closest')
              }
              ),

    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div('This heat map represent the Corona Virus recovered cases of all reported cases per day of week and week of month.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='Max Temperature on Day of Week and Month of Year', xaxis_title="Day of Week",
                   yaxis_title="Month")
              }
              )
])


if __name__ == '__main__':
    app.run_server()