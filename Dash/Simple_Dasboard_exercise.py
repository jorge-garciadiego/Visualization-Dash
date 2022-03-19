import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('data/OldFaithful.csv')

"""
  D = date of the recordings in month (August)
  X = duration of the current eruption in minutes 
  Y = waiting time until the next eruption in minutes
"""

data_faithful = [go.Scatter(x=df['X'], y=df['Y'], mode='markers',
                            marker=dict(
    size=12,
    color='rgb(51,204,153)',
    symbol='pentagon',
    line={'width': 2}
))]

layout_faithful = go.Layout(title='Old Faithful Eruption Intervals Durations',
                            xaxis={'title': 'Duration of eruption (minutes'},
                            yaxis=dict(
                                title='Interval to the next eruption (minutes)'),
                            hovermode='closest')

app.layout = html.Div([dcc.Graph(
    id='scatterplot',
    figure={'data': data_faithful, 'layout': layout_faithful}
)])

if __name__ == '__main__':
    app.run_server()
