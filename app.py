import plotly.express as px
import numpy as np
import pandas as pd
import dash
import plotly.io as pio
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv("C:/Users/User/Downloads/data_uncorrupted.csv")

app = dash.Dash(__name__)
app.title = "Algothon Data Visualisation Dashboard"

x = df[['time']].values
y = df[['value']].values

reformatted_x = []
reformatted_y = []

for i in range(len(x)):
    reformatted_x.append(x[i][0])
    reformatted_y.append(y[i][0])    

app.layout = html.Div([
    html.H1("Algothon challenge", style={'text-align': 'center'}),
    
    html.Div(id='output_container', children=[]),
    html.Br(),
    
    dcc.Graph(id="line_plot", figure={'data':[{'x':reformatted_x, 'y':reformatted_y, 'type':'line'}], 'layout': {'title': 'Cleaned Data'}})
    
])

if __name__ == '__main__':
    app.run_server(debug=True)