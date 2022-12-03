
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    html.P("Hello world again",
        style={
            "backgroundColor":"red",
            "textAlign":"center"
        })

   
])

if __name__ == '__main__':
    app.run_server(debug=True)