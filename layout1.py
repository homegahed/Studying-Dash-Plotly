# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:59:52 2022

@author: hmegahed
"""

import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output



trade_df = pd.read_csv('assets/trade_clean.csv')

trade_categories = trade_df.sort_values('imports')

fig = px.histogram(trade_categories, x='total', y='abrev', color='trade')

fig.update_layout(margin=dict(l=1, r=1, t=40, b=1),
                  paper_bgcolor="white",
                  title = {
                      'text':'graph title',
                      'x':0.2,
                      'y': 0.98,
                      'xanchor':'center',
                      'yanchor':'top'
                      },
                  template="plotly_white",
                  legend = dict(
                      orientation="h",
                      yanchor='top',
                      y=0.1,
                      xanchor='left',
                      x=0.3
                      )
                  )
#========================

year_df = pd.read_csv('assets/trade_sums_years.csv')
vars_trade = ['imports', 'exports', 'reexports', 'trade']
year_pivot = year_df.melt(id_vars=('year'), value_vars=(vars_trade))
year_pivot = year_pivot.query('variable != "trade"')

fig2 = px.line(year_pivot, x='year', y='value', color='variable', markers=True)

fig2.update_layout(margin=dict(l=1, r=1, t=30, b=1),
                  title = {
                      'text':'graph title',
                      'x':0.5,
                      'y': 0.98,
                      'xanchor':'center',
                      'yanchor':'top'
                      },
                  template="plotly_white",
                  legend = dict(
                      yanchor='top',
                      y=0.7,
                      xanchor='left',
                      x=0.05
                      )
                  )



#========================

location_df = trade_df.groupby('trade')['total'].sum()
location_df = location_df.reset_index(drop=False)

fig3 = px.pie(location_df, names='trade', values='total', hole=0.5)
fig3.update_layout(margin=dict(l=30, r=30, t=30, b=30),
                  title = {
                      'text':'graph title',
                      'x':0.5,
                      'y': 0.98,
                      'xanchor':'center',
                      'yanchor':'top'
                      },
                  template="plotly_white",
                  legend = dict(
                      orientation='h',
                      yanchor='top',
                      y=0.02,
                      xanchor='left',
                      x=0.3
                      )
                  )

#========================
app = dash.Dash(__name__)

#style = {'display':'inline-block'},
app.layout = html.Div(className='container',
                      children = [
                          html.Div(className = 'header', 
                          children = [html.H2('Dubai Trade')]
                          ),

                          html.Div(dcc.Graph(figure=fig,
                                        config = {
                                            'displayModeBar':False
                                            })),
                          
                          
                          
                          html.Div(dcc.Graph(figure=fig3,
                                        config = {
                                            'displayModeBar':False
                                            })),
                          html.Div(dcc.Graph(figure=fig2,
                                        config = {
                                            'displayModeBar':False
                                            })),
                          
                          html.Div(className='header')
                          
                          ])
   

if __name__ == '__main__':
    app.run_server(debug=False)
    
    
    
    
    
 # children= [
     
     
     
     
 #     html.Div(
 #     children = ['hi', 
 #                 dcc.Graph()], 
 #     style = {'border': 'solid 2px red', 
 #                        'margin-right':'5px', 'display':'inline-block',
 #                        'width':'45%', 'height':'10%'})
 #     ,
     
 #     html.Div(
 #         children = ['hi', 
 #                     dcc.Graph()], 
 #         style = {'border': 'solid 2px red', 
 #                         'margin-right':'5px', 'display':'inline-block',
 #                         'width':'45%', 'height':'10%'}),
     
     
     
     
     
     
 #     # html.Span('hi', style = {'border': 'solid 2px green'})
     
 #     ]
 
 # )