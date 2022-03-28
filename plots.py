# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 03:56:08 2022

@author: hmegahed
"""

import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

fig = px.line(
    x=["a","b","c"], y=[1,3,2], # replace with your own data source
    title="sample figure", height=500, width=300
)


fig2 = px.bar(
    x=["a","b","c"], y=[5,3,4], # replace with your own data source
    title="sample figure2", height=500, width=350
)



fig3 = px.area(
    x=["a","b","c"], y=[1,3,4], # replace with your own data source
    title="sample figure3", height=300, width=300
)

app = dash.Dash(__name__)

app.layout = html.Div(
    style = {'display':"inline-block", 'width':'auto',
             'height': '100vh', 'width':'100vw'},
    
    children = [
    html.Div(
        children = [dcc.Graph(figure=fig)], 
        style={'border':'solid black 2px'}),
    
    html.Div(
        children = [dcc.Graph(figure=fig2)], 
        style={'border':'solid black 2px'}),
        
    
    

    dcc.Graph(figure=fig3)
    ]
    )

if __name__ == '__main__':
    app.run_server(debug=True)
