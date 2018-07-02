import dash
from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
from pandas_datareader.data import DataReader
import plotly
import random
import time
import plotly.graph_objs as go
from collections import deque
import datetime
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sqlite3
import pandas as pd

########################################################################################################

# app = dash.Dash()
# app.layout = html.Div(
#     children=[html.H1('Pulkit songara'),
#     dcc.Graph(id='example', 
#         figure={
#             'data':[
#                 {
#                     'x':[1, 2, 3, 4, 5], 'y':[2, 8, 7, 4, 5], 'type':'line', 'name':'Boats'
#                 },
#                 {
#                     'x':[1, 2, 3, 4, 5], 'y':[2, 8, 7, 4, 5], 'type':'bar', 'name':'Cars'
#                 },
#                 ],
#             'layout':{
#                 'title':'Basic dash example'
#             }
#         })
# ])
# if __name__ == '__main__':
#    app.run_server(debug=True) 

##########################################################################################

# app = dash.Dash()
# app.layout = html.Div(children=
#                         [
#                             dcc.Input(id='input', value='something', type='text'),
#                             html.Div(id='output')
#                         ])
# @app.callback(
#     Output(component_id='output', component_property='children'),
#     [Input(component_id='input', component_property='value')]
# )
# def update_value(input_data):
#     try:
#         return str(float(input_data)**2)
#     except:
#         return 'error'

# if __name__ == '__main__':
#     app.run_server(debug=True)

###########################################################################################


# start = datetime.datetime(2015,1, 1)
# end = datetime.datetime.now()
# stock = 'TSLA'
# df = web.DataReader(stock, 'morningstar', start, end)


# app = dash.Dash()
# app.layout = html.Div(
#     children=[html.H1('Pulkit songara'),
#     dcc.Graph(id='example', 
#         figure={
#             'data':[
#                 {
#                     'x': df.index, 'y':df.Close, 'type':'line', 'name':stock
#                 },
#                 ],
#             'layout':{
#                 'title':'Basic dash example'
#             }
#         })
# ])
# if __name__ == '__main__':
#     app.run_server(debug=True) 

##########################################################################################




# X = deque(maxlen=20)
# Y = deque(maxlen=20)
# X.append(1)
# Y.append(1)
# app = dash.Dash()
# app.layout = html.Div(
#     [
#         dcc.Graph(id='live-graph', animate=True),
#         dcc.Interval(id='graph-update', interval=1000)
#         ]
#  )

# @app.callback(Output('live-graph', 'figure'), 
#         events=[Event('graph-update', 'interval')])
# def update_graph():
#      global X
#      global Y
#      X.append(X[-1]+1)
#      Y.append(Y[-1]+(Y[-1]*random.uniform(-0.1,0.1)))

#      data = go.Scatter(
#          x=list(X),
#          y=list(Y),
#          name='Scatter',
#          mode='lines+markers'
#      )

#      return{
#          'data':[data],
#          'layout':go.Layout(xaxis=dict(range=[min(X), max(X)]),
#          yaxis=dict(range=[min(Y), max(Y)]))
#      }


# if __name__ == '__main__':
#     app.run_server(debug=True) 





####################################################################################################


# app = dash.Dash('Vehicle-data')

# max_length = 50
# times = deque(maxlen=max_length)
# oil_temps = deque(maxlen=max_length)
# intake_temps = deque(maxlen=max_length)
# coolant_temps = deque(maxlen=max_length)
# rpms = deque(maxlen=max_length)
# speeds = deque(maxlen=max_length)
# throttle_pos = deque(maxlen=max_length)

# data_dict = {
#     'Oil Temperature': oil_temps,
#     'Intake Temperature': intake_temps,
#     'Coolant Temperature': coolant_temps,
#     'RPM': rpms,
#     'Speed': speeds,
#     'Throttle Position': throttle_pos   
# }

# def update_obd_values(times, oil_temps,intake_temps, coolant_temps, rpms, speeds, throttle_pos):
    
#     times.append(time.time())
#     if len(times)==1:
#         oil_temps.append(random.randrange(180, 230))
#         intake_temps.append(random.randrange(95, 115))
#         coolant_temps.append(random.randrange(170, 220))
#         rpms.append(random.randrange(1000, 9500))
#         speeds.append(random.randrange(30, 140))
#         throttle_pos.append(random.randrange(10, 90))
#     else:
#             for data_of_interest in [oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos]:
#                     data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))
#     return times, oil_temps,intake_temps, coolant_temps, rpms, speeds, throttle_pos

# times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos = update_obd_values(times, oil_temps,intake_temps, coolant_temps, rpms, speeds, throttle_pos)


# app.layout = html.Div([
#     html.Div([
#         html.H2('Vehicle Data', style={'float':'left',}),
#     ]),
#     dcc.Dropdown(id='vehicle-data-name',
#     options=[{'label':s, 'value':s}
#         for s in data_dict.keys()],
#     value=['Coolant Temprature', 'Oil Temprature', 'Intake Temprature'],
#     multi=True
#         ),
#     html.Div(children=html.Div(id='graphs'), className='row'),
#     dcc.Interval(
#         id='graph-update',
#         interval=100),
# ], className='container', style={'width':'98%', 'margin-left':10, 'margin-right':10, 'max-width':50000})

# @app.callback(
#     dash.dependencies.Output('graphs', 'children'),
#     [dash.dependencies.Input('vehicle-data-name', 'value')],
#     events = [dash.dependencies.Event('graph-update', 'interval')]
#     )

# def update_graph(data_names):
#     graphs = []
#     update_obd_values(times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos)


#     if len(data_names)>2:
#         class_choice = 'col s12 m6 l4'
#     elif len(data_names) == 2:
#         class_choice = 'col s12 m6 l6'
#     else:
#         class_choice = 'col s12'


#     for data_name in data_names:

#         data = go.Scatter(
#             x=list(times),
#             y=list(data_dict[data_name]),
#             name='Scatter',
#             fill="tozeroy",
#             fillcolor="#6897bb"
#             )

#         graphs.append(html.Div(dcc.Graph(
#             id=data_name,
#             animate=True,
#             figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(times),max(times)]),
#                                                         yaxis=dict(range=[min(data_dict[data_name]),max(data_dict[data_name])]),
#                                                         margin={'l':50,'r':1,'t':45,'b':1},
#                                                         title='{}'.format(data_name))}
#             ), className=class_choice))

#     return graphs


# #     external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
# # for css in external_css:
# #     app.css.append_css({"external_url": css})




# #     external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
# # for js in external_js:
# #     app.scripts.append_script({'external_url': js}) 


# if __name__ == '__main__':
#     app.run_server(debug=True)




###########################################################################################################################


# app = dash.Dash(__name__)
# app.layout = html.Div(
#     [   html.H2('Live Twitter Sentiment'),
#         dcc.Input(id='sentiment_term', value='olympic', type='text'),
#         dcc.Graph(id='live-graph', animate=False),
#         dcc.Interval(
#             id='graph-update',
#             interval=1*1000
#         ),

#     ]
# )
# @app.callback(Output('live-graph', 'figure'),
#               [Input(component_id='sentiment_term', component_property='value')],
#               events=[Event('graph-update', 'interval')])
# def update_graph_scatter(sentiment_term):
#     try:
#         conn = sqlite3.connect('twitter.db')
#         c = conn.cursor()
#         df = pd.read_sql("SELECT * FROM sentiment WHERE tweet LIKE ? ORDER BY unix DESC LIMIT 1000", conn ,params=('%' + sentiment_term + '%',))
#         df.sort_values('unix', inplace=True)
#         df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/2)).mean()

#         df['date'] = pd.to_datetime(df['unix'],unit='ms')
#         df.set_index('date', inplace=True)

#         df = df.resample('1min').mean()
#         df.dropna(inplace=True)
#         X = df.index
#         Y = df.sentiment_smoothed

#         data = plotly.graph_objs.Scatter(
#                 x=X,
#                 y=Y,
#                 name='Scatter',
#                 mode= 'lines+markers'
#                 )

#         return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
#                                                     yaxis=dict(range=[min(Y),max(Y)]),
#                                                     title='Term: {}'.format(sentiment_term))}

#     except Exception as e:
#         with open('errors.txt','a') as f:
#             f.write(str(e))
#             f.write('\n')



# if __name__ == '__main__':
#     app.run_server(debug=True)


#########################################################################################################################


# app = dash.Dash('Vehicle-data')

# max_length = 50
# times = deque(maxlen=max_length)
# oil_temps = deque(maxlen=max_length)
# intake_temps = deque(maxlen=max_length)

# data_dict = {
#     'Oil Temperature': oil_temps, 
# }

# def update_obd_values(times, oil_temps):
    
#     times.append(time.time())
#     if len(times)==1:
#         oil_temps.append(random.randrange(180, 230))
#     else:
#             # for data_of_interest in [oil_temps, intake_temps]:
#             #         data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))
#         return times, oil_temps

# times, oil_temps = update_obd_values(times, oil_temps)


# app.layout = html.Div([
#     html.Div([
#         html.H2('Vehicle Data', style={'float':'left',}),
#     ]),
#     dcc.Input(id='vehicle-data-name',
#     value=[ 'Oil Temprature'],
#         ),
#     html.Div(children=html.Div(id='graphs'), className='row'),
#     dcc.Interval(
#         id='graph-update',
#         interval=100),
# ], className='container', style={'width':'98%', 'margin-left':10, 'margin-right':10, 'max-width':50000})

# @app.callback(
#     dash.dependencies.Output('graphs', 'children'),
#     [dash.dependencies.Input('vehicle-data-name', 'value')],
#     events = [dash.dependencies.Event('graph-update', 'interval')]
#     )

# def update_graph(data_names):
#     graphs = []
#     update_obd_values(times, oil_temps)


#     # if len(data_names)>2:
#     #     class_choice = 'col s12 m6 l4'
#     # elif len(data_names) == 2:
#     #     class_choice = 'col s12 m6 l6'
#     # else:
#     class_choice = 'col s12'


# data = go.Scatter(
#             x=list(times),
#             y=list(data_dict[data_name]),
#             name='Scatter',
#             fill="tozeroy",
#             fillcolor="#6897bb"
#             )
# graphs.append(html.Div(dcc.Graph(
#             id=data_name,
#             animate=True,
#             figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(times),max(times)]),
#                                                         yaxis=dict(range=[min(data_dict[data_name]),max(data_dict[data_name])]),
#                                                         margin={'l':50,'r':1,'t':45,'b':1},
#                                                         title='{}'.format(data_name))}
#             ), className=class_choice))

#             return graphs


# #     external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
# # for css in external_css:
# #     app.css.append_css({"external_url": css})




# #     external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
# # for js in external_js:
# #     app.scripts.append_script({'external_url': js}) 


# if __name__ == '__main__':
#     app.run_server(debug=True)

########################################################################################################################3


# app = dash.Dash()
# app.layout =  html.Div([
#         html.H2('Vehicle Data', style={'float':'left',}),
    
#        html.Div(children=html.Div(id='graphs'), className='row'),
#     dcc.Interval(
#         id='graph-update',
#         interval=100),
#         ]),

# @app.callback(
#     Output(component_id='output', component_property='children'),
#     [Input(component_id='input', component_property='value')]
# )
# if __name__ == '__main__':
#    app.run_server(debug=True) 

#############################################################################################################

X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)
app = dash.Dash()
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(id='graph-update', interval=1000)
        ]
 )

@app.callback(Output('live-graph', 'figure'), 
        events=[Event('graph-update', 'interval')])
def update_graph():
     global X
     global Y
     X.append(X[-1]+1)
     Y.append(Y[-1]+(Y[-1]*random.uniform(-0.1,0.1)))
    #  count = 1
    #  if count==1:
    #     X.append(random.randrange(180, 230))
    #     Y.append(random.randrange(150, 190))
    #  else:
    #     X.append(X[-1]+X[-1]*random.uniform(-0.0001,0.0001))
    #     Y.append(Y[-1]+Y[-1]*random.uniform(-0.0001,0.0001))

     data = go.Scatter(
         x=list(X),
         y=list(Y),
         name='Scatter',
         mode='lines+markers'
     )

     return{
         'data':[data],
         'layout':go.Layout(xaxis=dict(range=[min(X), max(X)]),
         yaxis=dict(range=[min(Y), max(Y)]))
     }


if __name__ == '__main__':
    app.run_server(debug=True) 

