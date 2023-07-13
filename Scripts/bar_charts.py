import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


path = '/home/danial/Desktop/mydash/dash_plotly_course_material/Plotly-Dashboards-with-Dash-master/Data/2018WinterOlympics.csv'
df = pd.read_csv(path)
# print (df.head())

# data = [go.Bar(x = df['NOC'], 
#                y = df['Total'])]


trace1 = go.Bar(x = df['NOC'], 
                y = df['Gold'], 
                name='Gold', 
                marker={'color':'#FFD700'})

trace2 = go.Bar(x = df['NOC'], 
                y = df['Silver'], 
                name='Silver', 
                marker={'color':'#9EA0A1'})

trace3 = go.Bar(x = df['NOC'], 
                y = df['Bronze'], 
                name='Bronze', 
                marker={'color':'#CD7F32'})

data= [trace1, trace2, trace3]


layout = go.Layout(title = 'Medals') # to get the nested bar charts 
#layout = go.Layout(title = 'Medals', barmode='stack') # to get the stacked bar charts 

fig = go.Figure(data = data, layout = layout)

pyo.plot(fig)