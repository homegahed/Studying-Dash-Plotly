# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 01:32:04 2022

@author: hmegahed
"""
import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


trade_df = pd.read_csv('assets/trade_clean.csv')

# fig = px.histogram(trade_df, x='abrev', y='total', color='trade')

# fig.update_layout(margin=dict(l=1, r=1, t=30, b=1),
#                   paper_bgcolor="white",
#                   title = 'graph title',
#                   template="simple_white"
#                   )

#===================



# year_df = pd.read_csv('assets/trade_sums_years.csv'
# vars_trade = ['imports', 'exports', 'reexports', 'trade']
# year_pivot = year_df.melt(id_vars=('year'), value_vars=(vars_trade))
# year_pivot = year_pivot.query('variable != "trade"')

#(year_df.head())



# fig2 = px.line(year_pivot, x='year', y='value', color='variable', markers=True)

# fig.update_layout(margin=dict(l=1, r=1, t=30, b=1),
#                   title = {
#                       'text':'graph title',
#                       'x':0.5,
#                       'y': 0.98,
#                       'xanchor':'center',
#                       'yanchor':'top'
#                       },
#                   template="plotly_white",
#                   legend = dict(
#                       yanchor='top',
#                       y=0.7,
#                       xanchor='left',
#                       x=0.05
#                       )
#                   )

#===================


# print(trade_df['trade'].head())

location_df = trade_df.groupby('trade')['total'].sum()
location_df = location_df.reset_index(drop=False)

fig3 = px.pie(location_df, names='trade', values='total', hole=0.5)

print(location_df.head())

app = dash.Dash(__name__)

app.layout = html.Div(
    dcc.Graph(figure=fig3,
                  config = {
                      'displayModeBar':False
                      })
    )
    

if __name__ == '__main__':
    app.run_server(debug=False)
    
    