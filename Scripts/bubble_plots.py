import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('/home/danial/Desktop/mydash/dash_plotly_course_material/Plotly-Dashboards-with-Dash-master/Data/mpg.csv')
# print (df.head())
# print (df.columns)
# print (df.describe())

# df = df.sort_values('mpg', ascending=False)
data = [go.Scatter(x=df['horsepower'],
                   y = df['mpg'],
                   text = df['name'],
                   mode = 'markers',
                   marker = dict(size = df['weight']/100,
                                 color = df['cylinders'],
                                 showscale = True))] # marker = dict(size = 2*df['cylinders']

layout = go.Layout(title = 'Bubble chart', hovermode = 'closest')#, hovermode = 'x'
fig = go.Figure(data = data, layout=layout)
pyo.plot(fig)

# print(df['mpg'].isnull().sum())