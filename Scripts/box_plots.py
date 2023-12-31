
import plotly.offline as pyo
import plotly.graph_objs as go

y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [
    go.Box(
        y=y,
        boxpoints='outliers', # all --> display all the original data points
        jitter=0.3,      # spread them out so they all appear
        pointpos=-1.8   # offset them to the left of the box
    )
]
pyo.plot(data, filename='box1.html')