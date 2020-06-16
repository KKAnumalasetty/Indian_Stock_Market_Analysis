
# A very simple Flask Hello World app for you to get started with...

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:12:39 2020

@author: Z002L70
"""


from flask import Flask

server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Hello from Flask!'


############################ My DASH App below ###########################


import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__,server=server,routes_pathname_prefix='/dash/')


def get_index_pe_ratio_data(index_name):

    import glob
    import pandas as pd

    glued_data = pd.DataFrame()


    import os
    cwd = os.getcwd()
    print('CWD = ',cwd)

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        print(f)


    file_path = './mysite/'+index_name+'/*.csv'
    print('\n *********************** \n file = ',file_path)
    for file_name in glob.glob(file_path):
        x = pd.read_csv(file_name, low_memory=False)
        glued_data = pd.concat([glued_data,x],axis=0)


    print('index_name = ',index_name,'\n',glued_data.dtypes,'\n',glued_data.shape,'\n ***********************')


    glued_data['Mean_PE'] = glued_data['P/E'].mean()

    glued_data['1std_dev_PE'] = glued_data['Mean_PE']+glued_data['P/E'].std()
    glued_data['Neg_1std_dev_PE'] = glued_data['Mean_PE']-glued_data['P/E'].std()

    glued_data['1_5_std_dev_PE'] = glued_data['Mean_PE']+(1.5*glued_data['P/E'].std())



    glued_data['2std_dev_PE'] = glued_data['Mean_PE']+(2*glued_data['P/E'].std())
    glued_data['Neg_2std_dev_PE'] = glued_data['Mean_PE']-(2*glued_data['P/E'].std())


    # glued_data['Mean_PE'] = glued_data['P/E'].mean()
    # glued_data['Mean_PE'] = glued_data['P/E'].mean()
    # glued_data['Mean_PE'] = glued_data['P/E'].mean()

    return glued_data


def plot_PE_Ratio_Chart(index_name):

    glued_data = get_index_pe_ratio_data(index_name)

    import plotly.express as px
    import plotly.graph_objects as go

    x = glued_data['Date']
    fig = px.line(glued_data, x='Date', y='P/E')

    fig.add_trace(go.Scatter(
        x=x, y=glued_data['Mean_PE'],
        hoverinfo='x+y',
        mode='lines',
        name = 'Mean',
        line=dict(width=2, color='black'),
    ))

    fig.add_trace(go.Scatter(
        x=x, y=glued_data['1_5_std_dev_PE'],
        hoverinfo='x+y',
        mode='lines',
        name = '1.5 Std Dev',
        line=dict(width=4, color='yellow'),
    ))


    fig.add_trace(go.Scatter(
        x=x, y=glued_data['1std_dev_PE'],
        hoverinfo='x+y',
        mode='lines',
        name='1 Std Dev',
        line=dict(width=4, color='red'),
    ))

    fig.add_trace(go.Scatter(
        x=x, y=glued_data['Neg_1std_dev_PE'],
        hoverinfo='x+y',
        mode='lines',
        name='Negative 1 Std Dev',
        line=dict(width=4, color='green'),
    ))


    fig.add_trace(go.Scatter(
        x=x, y=glued_data['2std_dev_PE'],
        hoverinfo='x+y',
        mode='lines',
        name='2 Std Dev',
        line=dict(width=4, color='red'),
    ))

    fig.add_trace(go.Scatter(
        x=x, y=glued_data['Neg_2std_dev_PE'],
        hoverinfo='x+y',
        mode='lines',
        name='Negative 2 Std Dev',
        line=dict(width=4, color='green'),
    ))



    fig.update_xaxes(rangeslider_visible=True,
                        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
                        )
    )
    return fig




app.layout = html.Div([
        dcc.Dropdown(
        id='index-name-dropdown',
        options=[
            {'label': 'NIFTY 50', 'value': 'NIFTY 50'},
            {'label': 'NIFTY Bank', 'value': 'NIFTY Bank'},
            {'label': 'NIFTY Pharma', 'value': 'NIFTY Pharma'}
        ],
        value='NIFTY 50',
        style=dict(
                    width='40%',
                    display='inline-block',
                    verticalAlign="middle"
                )

    ),
    dcc.Graph(id='pe-ratio-chart')
])


@app.callback(
    dash.dependencies.Output('pe-ratio-chart', component_property='figure'),
    [dash.dependencies.Input('index-name-dropdown', component_property='value')])
def update_pe_ratio_chart(value):
    if value=="NIFTY 50":
        return plot_PE_Ratio_Chart("NIFTY_50_PE_RATIO")
    elif value=="NIFTY Bank":
        return plot_PE_Ratio_Chart("NIFTY Bank PE Ratio")
    elif value=="NIFTY Pharma":
        return plot_PE_Ratio_Chart("NIFTY Pharma PE Ratio")
    else:
        return plot_PE_Ratio_Chart("NIFTY_50_PE_RATIO")


if __name__ == '__main__':
    app.run_server(debug=True)