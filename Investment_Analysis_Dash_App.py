# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:40:07 2020

@author: karth
"""

import pandas as pd
#######################################################################
################ Dependent methods begins ###############################
#######################################################################

################## PE Ratio dependencies begin ##########################
def get_index_pe_ratio_data(index_name):

    import glob
    import pandas as pd
    
    glued_data = pd.DataFrame()
    file_path = '.\\'+index_name+'\\*.csv'
#     print('\n *********************** \n file = ',file_path)
    for file_name in glob.glob('.\\'+index_name+'\\*.csv'):
        x = pd.read_csv(file_name, low_memory=False)
        glued_data = pd.concat([glued_data,x],axis=0)
        glued_data['Date'] =  pd.to_datetime(glued_data['Date'], infer_datetime_format=True)
    
    
#     print('index_name = ',index_name,'\n',glued_data.dtypes,'\n',glued_data.shape,'\n ***********************')


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

def plot_PE_Ratio_Chart(index_name, mean_switch, one_std_dev_switch, neg_one_std_dev_switch, two_std_dev_switch,neg_two_std_dev_switch,one_five_std_dev_switch):
    
    glued_data = get_index_pe_ratio_data(index_name)

    import plotly.express as px
    import plotly.graph_objects as go

    x = glued_data['Date']
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
            x=glued_data['Date'], 
            y=glued_data['P/E'],
            hoverinfo='x+y',
            name = 'P/E',
    ))


    if (mean_switch == True):
        fig.add_trace(go.Scatter(
            x=x, y=glued_data['Mean_PE'],
            hoverinfo='x+y',
            mode='lines',
            name = 'Mean',
            line=dict(width=2, color='black'),
        ))

    if (one_five_std_dev_switch==True):
        fig.add_trace(go.Scatter(
            x=x, y=glued_data['1_5_std_dev_PE'],
            hoverinfo='x+y',
            mode='lines',
            name = '1.5 Std Dev',
            line=dict(width=4, color='yellow'),
        ))

        
    if (one_std_dev_switch == True):
        fig.add_trace(go.Scatter(
            x=x, y=glued_data['1std_dev_PE'],
            hoverinfo='x+y',
            mode='lines',
            name='1 Std Dev',
            line=dict(width=4, color='red'),
        ))

    if (neg_one_std_dev_switch == True):
        fig.add_trace(go.Scatter(
            x=x, y=glued_data['Neg_1std_dev_PE'],
            hoverinfo='x+y',
            mode='lines',
            name='Negative 1 Std Dev',
            line=dict(width=4, color='green'),
        ))


    if (two_std_dev_switch == True):
        fig.add_trace(go.Scatter(
            x=x, y=glued_data['2std_dev_PE'],
            hoverinfo='x+y',
            mode='lines',
            name='2 Std Dev',
            line=dict(width=4, color='red'),
        ))

    if (neg_two_std_dev_switch == True):
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
            ]),
            )
            )

    fig.update_layout(title={
        'text': " P/E Ratio for index : "+ index_name,
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        plot_bgcolor='rgb(230,230,230)',
        hovermode= 'x')
        
    return fig


################# PE Ratio dependencies end ############################

################ CAGR and Index price dependencies begin #####################
def get_index_data(index_name):

    import glob
    import pandas as pd
    
    index_DF = pd.DataFrame()
    file_path = '.\\'+index_name+'\\*.csv'
#     print('\n *********************** \n file = ',file_path)
    for file_name in glob.glob('.\\'+index_name+'\\*.csv'):
        x = pd.read_csv(file_name, low_memory=False)
        index_DF = pd.concat([index_DF,x],axis=0)
        index_DF['Date'] =  pd.to_datetime(index_DF['Date'], infer_datetime_format=True)
        index_DF['Year'] = index_DF['Date'].dt.year
        index_DF['Month'] = index_DF['Date'].dt.month_name()
    
#     print('index_name = ',index_name,'\n',glued_data.dtyPrices,'\n',glued_data.shaPrice,'\n ***********************')


    index_DF['Mean_Price'] = index_DF['Close'].mean()

    index_DF['1std_dev_Price'] = index_DF['Mean_Price']+index_DF['Close'].std()
    index_DF['Neg_1std_dev_Price'] = index_DF['Mean_Price']-index_DF['Close'].std()

    index_DF['1_5_std_dev_Price'] = index_DF['Mean_Price']+(1.5*index_DF['Close'].std())


    index_DF['2std_dev_Price'] = index_DF['Mean_Price']+(2*index_DF['Close'].std())
    index_DF['Neg_2std_dev_Price'] = index_DF['Mean_Price']-(2*index_DF['Close'].std())

    return index_DF



def plot_index_price_chart(index_name, mean_switch, one_std_dev_switch, neg_one_std_dev_switch, two_std_dev_switch,neg_two_std_dev_switch,one_five_std_dev_switch):
    
    glued_data = get_index_data(index_name)

    import plotly.express as px
    import plotly.graph_objects as go

    x = glued_data['Date']
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
            x=glued_data['Date'], 
            y=glued_data['Close'],
            hoverinfo='x+y',
            name = index_name+' Stock Price',
    ))


    if (mean_switch == True):
        fig.add_trace(go.Scatter(
            x=x, y=glued_data['Mean_Price'],
            hoverinfo='x+y',
            mode='lines',
            name = 'Mean',
            line=dict(width=2, color='black'),
        ))

    if (one_five_std_dev_switch==True):
        fig.add_trace(go.Scatter(
            x=x, y=glued_data['1_5_std_dev_Price'],
            hoverinfo='x+y',
            mode='lines',
            name = '1.5 Std Dev',
            line=dict(width=4, color='yellow'),
        ))

        
    if (one_std_dev_switch == True):
        fig.add_trace(go.Scatter(
            x=x, y=glued_data['1std_dev_Price'],
            hoverinfo='x+y',
            mode='lines',
            name='1 Std Dev',
            line=dict(width=4, color='red'),
        ))

    if (neg_one_std_dev_switch == True):
        fig.add_trace(go.Scatter(
            x=x, y=glued_data['Neg_1std_dev_Price'],
            hoverinfo='x+y',
            mode='lines',
            name='Negative 1 Std Dev',
            line=dict(width=4, color='green'),
        ))


    if (two_std_dev_switch == True):
        fig.add_trace(go.Scatter(
            x=x, y=glued_data['2std_dev_Price'],
            hoverinfo='x+y',
            mode='lines',
            name='2 Std Dev',
            line=dict(width=4, color='red'),
        ))

    if (neg_two_std_dev_switch == True):
        fig.add_trace(go.Scatter(
            x=x, y=glued_data['Neg_2std_dev_Price'],
            hoverinfo='x+y',
            mode='lines',
            name='Negative 2 Std Dev',
            line=dict(width=4, color='green'),
        ))

    fig.update_layout(title={
        'text': " Stock Price for Index:  "+ index_name,
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        plot_bgcolor='rgb(230,230,230)',
        hovermode= 'x')
        

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
    


def get_index_data_from_csv(index_name):
    
    import glob
    import pandas as pd
    
    index_DF = pd.DataFrame()
    file_path = '.\\'+index_name+'\\*.csv'
#     print('\n *********************** \n file = ',file_path)
    for file_name in glob.glob('.\\'+index_name+'\\*.csv'):
        x = pd.read_csv(file_name, low_memory=False)
        index_DF = pd.concat([index_DF,x],axis=0)
    
    
    index_DF['Date'] =  pd.to_datetime(index_DF['Date'], infer_datetime_format=True)
    index_DF['Year'] = index_DF['Date'].dt.year
    index_DF['Month'] = index_DF['Date'].dt.month_name()
    return index_DF


def get_nifty_value_by_year(year,nifty_DF):
    nifty_DF = nifty_DF[['Date','Year','Close']]
    nifty_DF.sort_values(['Date'],ascending=[True],inplace=True)
    nifty_DF.reset_index(drop=True,inplace=True)
    if year <= nifty_DF['Year'].max():
        nifty_value = nifty_DF[nifty_DF['Year']==year]['Close'].iloc[0]
    else:
        nifty_value = 0
    return nifty_value

def calculate_CAGR(begin_year,end_year,nifty_DF):
    begin_year_value = get_nifty_value_by_year(begin_year,nifty_DF)
    end_year_value = get_nifty_value_by_year(end_year,nifty_DF)
    time_window = end_year - begin_year
    
    # CAGR formula - time_window should be a positive integer and greater than 0
    cagr = (((end_year_value/begin_year_value)**(1/time_window))-1)
    
    return begin_year_value,end_year_value,time_window,cagr

def calculate_rolling_CAGR(years,nifty_DF):
    
    
    first_year_in_data =  nifty_DF['Year'].min()
    last_year_in_data =  nifty_DF['Year'].max()
    
    
    index=0
    i=0
    begin_year_rolling = first_year_in_data
    end_year_rolling = first_year_in_data+years

    main_cagr_rolling_DF = pd.DataFrame()
    
    while end_year_rolling<=last_year_in_data:
        cagr_rolling_DF = pd.DataFrame()
        
        if i >0:
            begin_year_rolling = begin_year_rolling+1
            end_year_rolling = begin_year_rolling + years
           

        cagr_rolling_DF.loc[index,'Begin_Year'] = begin_year_rolling
        cagr_rolling_DF.loc[index,'End_Year'] = end_year_rolling
        cagr_rolling_DF.loc[index,'Time_Window_yrs'] = str(begin_year_rolling) +"-" + str(end_year_rolling)
        begin_year_value,end_year_value,time_window,cagr = calculate_CAGR(begin_year_rolling,end_year_rolling,nifty_DF)
        cagr_rolling_DF.loc[index,'CAGR'] = cagr
        
#       #other necessary fields for validation purposes - Begin

        cagr_rolling_DF.loc[index,'Being_Year_Nifty_Value'] = begin_year_value
        cagr_rolling_DF.loc[index,'End_Year_Nifty_Value'] = end_year_value
        cagr_rolling_DF.loc[index,'Time_Window'] = time_window
        cagr_rolling_DF.loc[index,'End_Value/Begin_Value'] = (end_year_value/begin_year_value)
        cagr_rolling_DF.loc[index,'1/time_window'] = 1/time_window
        cagr_rolling_DF.loc[index,'End_Value/Begin_Value ^ 1/time_window)'] = ((end_year_value/begin_year_value)**(1/time_window))
        cagr_rolling_DF.loc[index,'CAGR_Pandas_Calc'] = cagr_rolling_DF.loc[index,'End_Value/Begin_Value ^ 1/time_window)'] -1
        cagr_rolling_DF.loc[index,'CAGR %'] = cagr*100

        #other necessary fields for validation purposes - End
        
#         print('Index = ',index,' Begin : ',begin_year_rolling,' End : ',end_year_rolling,' Time_window: ',time_window,' CAGR = ',cagr_rolling_DF.loc[index,'CAGR'])
        main_cagr_rolling_DF.reset_index(drop=True,inplace=True)
        if (end_year_rolling <= last_year_in_data):
            main_cagr_rolling_DF = pd.concat([main_cagr_rolling_DF,cagr_rolling_DF],ignore_index=True)
        i = i+1
        
    main_cagr_rolling_DF['CAGR %'] = pd.Series(["{0:.2f}%".format(val * 100) for val in main_cagr_rolling_DF['CAGR']], index = main_cagr_rolling_DF.index)
    
    return main_cagr_rolling_DF

def plot_rolling_CAGR(num_years,index_name):

    import plotly.graph_objects as go
    
    nifty_DF = get_index_data_from_csv(index_name)
    cagr_rolling_DF = calculate_rolling_CAGR(num_years,nifty_DF)

    x = cagr_rolling_DF['Time_Window_yrs']
    cagr_rolling_DF['My_Retirement_Target'] = 13

    for index,row in enumerate(cagr_rolling_DF.values):
        if cagr_rolling_DF.loc[index]['CAGR'] > 0:
            cagr_rolling_DF.loc[index,'bar_color'] = 'green'
        else:
            cagr_rolling_DF.loc[index,'bar_color'] =  'red'

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=x,
            y=cagr_rolling_DF['CAGR %'],
            name = 'Rolling NIFTY_50 CAGR%',
            text=cagr_rolling_DF['CAGR %'],
            textposition='auto',
            marker = {'color': cagr_rolling_DF['bar_color']}
        ))

    fig.add_trace(
        go.Scatter(
            x=x,
            y=cagr_rolling_DF['My_Retirement_Target'],
            name='Retirement Target %'
        ))
    
    fig.update_layout(title={
        'text': str(num_years) + " yrs Rolling CAGR analysis for index : "+ index_name,
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        plot_bgcolor='rgb(230,230,230)')

    return fig


################ CAGR and Index price dependencies end ########################

#######################################################################
################ Dependent methods ends ###############################
#######################################################################
        
    
################### Dash App begins ############################

def run_investment_analysis_dash_app():
    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    import dash_bootstrap_components as dbc 


       
    body = dbc.Container([
        
    html.Div([
            dcc.Dropdown(
            id='index-name-dropdown',
            options=[
                {'label': 'NIFTY 50', 'value': 'NIFTY 50'},
                {'label': 'NIFTY Bank', 'value': 'NIFTY Bank'},
                {'label': 'NIFTY Pharma', 'value': 'NIFTY Pharma'},
                {'label': 'NIFTY IT', 'value': 'NIFTY IT'}
            ],
            value='NIFTY 50',
           ),
        
        html.Br(),
        html.Div([dcc.Checklist(id='my-checklist',
    options=[
        {'label': 'Average or Mean', 'value': 'mean_switch'},
        {'label': '1 Standard Deviation', 'value': 'one_std_dev_switch'},
        {'label': '-1 Standard Deviation', 'value': 'neg_one_std_dev_switch'},
        {'label': '2 Standard Deviations', 'value': 'two_std_dev_switch'},
        {'label': '-2 Standard Deviation', 'value': 'neg_two_std_dev_switch'},
        {'label': '1.5 Standard Deviations', 'value': 'one_five_std_dev_switch'}
    ],
    value=[]
    )]),
        
        html.Br(),
        dcc.Graph(id='pe-ratio-chart'),
        html.Br(),
        html.Img(src="https://i.ibb.co/q7Sh5y2/index-buying-guide.jpg"),
        html.Br(),
        dcc.Checklist(id='index-price-chart-checklist',
        options=[
        {'label': 'Average or Mean', 'value': 'mean_switch'},
        {'label': '1 Standard Deviation', 'value': 'one_std_dev_switch'},
        {'label': '-1 Standard Deviation', 'value': 'neg_one_std_dev_switch'},
        {'label': '2 Standard Deviations', 'value': 'two_std_dev_switch'},
        {'label': '-2 Standard Deviation', 'value': 'neg_two_std_dev_switch'},
        {'label': '1.5 Standard Deviations', 'value': 'one_five_std_dev_switch'}
        ],
        value=[]
        ),
        
        html.Br(),
        dcc.Graph(id='index-price-chart'),
        html.Br(),
        html.Div([
        html.Label('Select Time Window slots in years to calculate Rolling CAGR', id='time-window-label'),
        dcc.Slider(
                id='time-window-slider',
                min=1,
                max=29,
                value=10,
                step=1,
                marks={
                        1: '1',
                        5: '5',
                        10: '10',
                        15: '15',
                        20: '20',
                        25: '25',
                        29: '29',                   
                    },
            ),
            
        ],style = dict(width= '45%')),
        
        html.Br(),
        
        html.Div(id='slider-output-container',style = 
                     dict(display= 'inline-block',
                         width= '40%',
                         verticalAlign="middle",
                         textAlign="middle")),
        
        dcc.Graph(id='rolling-cagr-chart')
    ])
    ])
    
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = 'Investment Analysis Dash App - Karthik Anumalasetty'
    app.layout = body
    
    
    @app.callback(
        dash.dependencies.Output('pe-ratio-chart', component_property='figure'),
        [dash.dependencies.Input('index-name-dropdown', component_property='value'),
        dash.dependencies.Input('my-checklist', component_property='value')])
    def update_pe_ratio_chart(value, checkList):

        mean_switch=False
        one_std_dev_switch=False
        neg_one_std_dev_switch=False
        two_std_dev_switch=False
        neg_two_std_dev_switch=False
        one_five_std_dev_switch=False       

        if (len(checkList) >0):
            for each_switch in checkList:
                if (each_switch == "mean_switch"):
                    mean_switch=True
                elif (each_switch == "one_std_dev_switch"):
                    one_std_dev_switch=True
                elif (each_switch == "one_five_std_dev_switch"):
                    one_five_std_dev_switch=True
                elif (each_switch == "neg_one_std_dev_switch"):                    
                     neg_one_std_dev_switch=True
                elif (each_switch == "two_std_dev_switch"):
                     two_std_dev_switch=True
                elif (each_switch == "neg_two_std_dev_switch"):
                    neg_two_std_dev_switch=True    
        
        
        if value=="NIFTY 50":
            return plot_PE_Ratio_Chart("NIFTY_50_PE_Ratio", mean_switch, one_std_dev_switch, neg_one_std_dev_switch, two_std_dev_switch,neg_two_std_dev_switch,one_five_std_dev_switch)
        elif value=="NIFTY Bank":
            return plot_PE_Ratio_Chart("NIFTY_Bank_PE_Ratio",mean_switch, one_std_dev_switch, neg_one_std_dev_switch, two_std_dev_switch,neg_two_std_dev_switch,one_five_std_dev_switch)
        elif value=="NIFTY Pharma":
            return plot_PE_Ratio_Chart("NIFTY_Pharma_PE_Ratio",mean_switch, one_std_dev_switch, neg_one_std_dev_switch, two_std_dev_switch,neg_two_std_dev_switch,one_five_std_dev_switch)
        elif value=="NIFTY IT":
            return plot_PE_Ratio_Chart("NIFTY_IT_PE_Ratio",mean_switch, one_std_dev_switch, neg_one_std_dev_switch, two_std_dev_switch,neg_two_std_dev_switch,one_five_std_dev_switch)
        else:
            return plot_PE_Ratio_Chart("NIFTY_50_PE_Ratio",mean_switch, one_std_dev_switch, neg_one_std_dev_switch, two_std_dev_switch,neg_two_std_dev_switch,one_five_std_dev_switch)

        
    @app.callback(
    dash.dependencies.Output('index-price-chart', component_property='figure'),
    [dash.dependencies.Input('index-name-dropdown', component_property='value'),
    dash.dependencies.Input('index-price-chart-checklist', component_property='value')])
    def update_index_price_chart(value, checkList):

        mean_switch=False
        one_std_dev_switch=False
        neg_one_std_dev_switch=False
        two_std_dev_switch=False
        neg_two_std_dev_switch=False
        one_five_std_dev_switch=False       

        if (len(checkList) >0):
            for each_switch in checkList:
                if (each_switch == "mean_switch"):
                    mean_switch=True
                elif (each_switch == "one_std_dev_switch"):
                    one_std_dev_switch=True
                elif (each_switch == "one_five_std_dev_switch"):
                    one_five_std_dev_switch=True
                elif (each_switch == "neg_one_std_dev_switch"):                    
                     neg_one_std_dev_switch=True
                elif (each_switch == "two_std_dev_switch"):
                     two_std_dev_switch=True
                elif (each_switch == "neg_two_std_dev_switch"):
                    neg_two_std_dev_switch=True    
        
        
        if value=="NIFTY 50":
            return plot_index_price_chart("NIFTY_50", mean_switch, one_std_dev_switch, neg_one_std_dev_switch, two_std_dev_switch,neg_two_std_dev_switch,one_five_std_dev_switch)
        elif value=="NIFTY Bank":
            return plot_index_price_chart("NIFTY_Bank",mean_switch, one_std_dev_switch, neg_one_std_dev_switch, two_std_dev_switch,neg_two_std_dev_switch,one_five_std_dev_switch)
        elif value=="NIFTY Pharma":
            return plot_index_price_chart("NIFTY_Pharma",mean_switch, one_std_dev_switch, neg_one_std_dev_switch, two_std_dev_switch,neg_two_std_dev_switch,one_five_std_dev_switch)
        elif value=="NIFTY IT":
            return plot_index_price_chart("NIFTY_IT",mean_switch, one_std_dev_switch, neg_one_std_dev_switch, two_std_dev_switch,neg_two_std_dev_switch,one_five_std_dev_switch)
        else:
            return plot_index_price_chart("NIFTY_50",mean_switch, one_std_dev_switch, neg_one_std_dev_switch, two_std_dev_switch,neg_two_std_dev_switch,one_five_std_dev_switch)


    @app.callback(
        dash.dependencies.Output('rolling-cagr-chart', component_property='figure'),
        [dash.dependencies.Input('index-name-dropdown', component_property='value'),
        dash.dependencies.Input('time-window-slider', component_property='value')])
    def update_rolling_cagr_chart(index_name,num_years):
        
        if index_name=="NIFTY 50":
            index_name = 'NIFTY_50'
            return plot_rolling_CAGR(num_years,index_name)
        elif index_name=="NIFTY Bank":
            index_name = 'NIFTY_Bank'
            return plot_rolling_CAGR(num_years,index_name)
        elif index_name=="NIFTY Pharma":
            index_name = 'NIFTY_Pharma'
            return plot_rolling_CAGR(num_years,index_name)
        elif index_name=="NIFTY IT":
            index_name = 'NIFTY_IT'
            return plot_rolling_CAGR(num_years,index_name)
        else:
            index_name = 'NIFTY_50'
#             print('################ we are in else condition ##############')
            return plot_rolling_CAGR(num_years,index_name)

    @app.callback(
        dash.dependencies.Output('slider-output-container', component_property='children'),
        [dash.dependencies.Input('time-window-slider', component_property='value')])
    def update_num_years_selected(num_years):
        slider_output = " Time Window slots selected = " + str(num_years) +" years"
        return slider_output
    
    app.run_server(debug=False)

if __name__ == '__main__':
    run_investment_analysis_dash_app()
