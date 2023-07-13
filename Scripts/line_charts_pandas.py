import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
df = pd.read_csv('/home/danial/Desktop/mydash/dash_plotly_course_material/Plotly-Dashboards-with-Dash-master/SourceData/nst-est2017-alldata.csv')
# print (df.head())

df2 = df[df['DIVISION'] == '1']
df2.set_index('NAME', inplace=True)
list_of_population_cols = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_population_cols]


data = [go.Scatter(x=df2.columns,
                   y=df2.loc[name], 
                   mode= 'lines', 
                   name=name) for name in df2.index]

pyo.plot(data)