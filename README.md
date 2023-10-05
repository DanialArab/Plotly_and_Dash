# Plotly and Dash

This repo documents my understanding of interactive/updatable dashboards using Python libraries. All the scripts are attached here at <a href="https://github.com/DanialArab/Plotly_and_Dash/tree/main/Scripts">Python scripts</a>. 

Reference: <a href='https://www.udemy.com/course/interactive-python-dashboards-with-plotly-and-dash/'>Interactive Python Dashboards with Plotly and Dash Udemy course</a>


![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/course%20materials.PNG)

1. [Introduction](#1)
2. [Plotly Basics](#2)
   1. [Scatter Plots](#3)
   2. [Line Charts](#4)
   3. [Bar Charts](#5)
   4. [Bubble Plots](#6)
   5. [Box Plots](#7)
   6. [Histograms](#8)
   7. [Distribution plots (Distplots)](#9)
   8. [Heatmaps](#10)



   
<a name="1"></a>
## Introduction

Introduction

+ Dash is built upon Flask.
+ Matplotlib creates **static image files**
+ Seaborn, uses matplotlib on the backend, is designed to cteate nice looking statistical plots (**static plots**)
+ Plotly:
  + is the open source library which is a general data visualization librray focused on **interactive** visualizations
  + has libraries for JavaScript, React, R, and Python (the most popular version is the Python library)
  + using plotly Python library we can craete interactive plots as **.html** files
  + while users can still interact with these plots (zoom in, select, hover over), these plots cannot be connected to chaniging data sources that is why we need Dash
  + so plotly is great when we want some little interactive image that you knwo the data source behind it is going to be static and not changing
+ Dash:
  + we often want plots to be able to interact with each other, interact with components, or have plots update in real time. To accomplish these we need a dashboard
  + Dash is an open source library from the Plotly company that allows you to create a full dashboard with multiple components, interactivity, and multiple plots
  + instead of creating an .html file, Dash produces a dashboard web application at a local url (127.0.0.1:8050) in which we can interact with the dashboard
  + since Dash renders a full web app, we can then deploy our dashboards online for other people to use 


<a name="2"></a>
## Plotly Basics

Documentation: https://plotly.com/python/
    
<a name="3"></a>
### Scatter plots

They allow the comparison of two variables for a set of data.

      import numpy as np
      import plotly.offline as pyo
      import plotly.graph_objs as go
      
      np.random.seed(42)
      
      random_x = np.random.randint(0, 101, 100)
      random_y = np.random.randint(0, 101, 100)
      data = [go.Scatter(x=random_x, 
                        y=random_y, 
                        mode='markers',
                        marker = dict(
                            size = 12,
                            color = 'rgb(51, 204, 153)',
                            symbol = 'pentagon',
                            line = {'width': 2}
                        ))]
      
      layout = go.Layout(title = 'Hello First Plot',
                         xaxis = {'title': 'MY X AXIS'},
                         yaxis = dict(title = 'MY Y AXIS'),
                         hovermode = 'closest')
      fig = go.Figure(data = data, layout = layout)
      
      pyo.plot(fig, filename='scatter.html')

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/scatter_plots.png)


<a name="4"></a>
### Line Charts

+ A line chart displays a series of data points (markers) connected by line segments
+ It is similar to a scatter plot except that the measurement points are **ordered (typically by their x-axis value)** and joined with straight line segments
+ Often used to visualize a **trend in data over intervals of time - known as a time series** 

      import numpy as np
      import plotly.offline as pyo
      import plotly.graph_objs as go
      
      np.random.seed(56)
      
      x_val = np.linspace(0, 1, 100)
      y_val = np.random.randn(100)
      
      trace0 = go.Scatter(x=x_val, 
                          y=y_val + 5, 
                          mode ='markers', 
                          name = 'markers')
      
      trace1 = go.Scatter(x=x_val, 
                          y=y_val, 
                          mode ='lines', 
                          name = 'my lines')
      
      
      trace2 = go.Scatter(x=x_val, 
                          y=y_val-5, 
                          mode ='lines+markers', 
                          name = 'my favorite')
      
      
      data =[trace0, trace1, trace2]
      
      layout = go.Layout(title='Line Charts')
      
      fig = go.Figure(data = data, layout=layout)
      
      pyo.plot(fig, filename='line_chart.html')


![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/line_charts.png)


<a name="5"></a>
### Bar Charts

+ A bar chart presents **categorical data** with rectangular bars with heights (or lengths) proportional to the values that they represent
+ Typically the x-axis is the categories and the y-axis is the count (number of occurances) in each category
+ The y-axis can also be any aggregarion (count, sum, average, etc.)
+ Stacked bar charts vs. nested bar charts 

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

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/bar_charts.png)

<a name="6"></a>
### Bubble Plots

+ Bubble charts are very similar to Scatter plots, except we now convey a **third variable's information** through the **size of the markers**
+ We can also continue to add variable information by coloring points based on a category

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

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/bubble_charts.png)

<a name="7"></a>
### Box Plots 

+ Box plots visualize the variation of a feature by depicting the **continuous numerical data through quartiles**
+ we can then separate the data based on a categorical feature to compare the continuous feature based on category
+ the Box plot is a way of visually displaying the data distribution through their quartiles
+ Quartiles separate the data into 4 equal parts
+ the middle line is the median
+ The IQR is the interquartile range (the length of the filled in box Q3 - Q1)
+ Depending on the stylying, max and min values are shown with 'whiskers'
+ a Box plot identifies outliers from the median compared to the rest of the data
+ Outliers are the values larger or smaller than Q3 or Q1, respectively, by at least 1.5 times the IQR
+ Outliers are displayed as singular markers outside the whiskers
+ we can actually use Box plots to perform a real analysis


      import plotly.offline as pyo
      import plotly.graph_objs as go
      
      y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]
      
      data = [
          go.Box(
              y=y,
              boxpoints='all', # all --> display all the original data points
              jitter=0.3,      # spread them out so they all appear
              pointpos=-1.8   # offset them to the left of the box
          )
      ]
      pyo.plot(data, filename='box1.html')

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/box_plots_all.png)

      
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

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/box_plots_outliers.png)

<a name="8"></a>
### Histograms  

+ displays an accurate representation of the overal distribution of a **continuous** feature
+ to get the same thing for the categorical features we have bar charts, histograms are only for the continuous feature analysis
+ to craete a histogram, we divide the entire range of values of the continuous feature into a series of intervals, which are known as bins
+ then we count the number of occurences per bin (per interval range)
+ we can change the bin size to get either more or less detail
+ increased bin size --> decreased number of bins
+ to get more details: decreased bin size --> increased number of bins 

      import plotly.offline as pyo
      import plotly.graph_objs as go
      import pandas as pd
      
      
      df = pd.read_csv('/home/danial/Desktop/mydash/dash_plotly_course_material/Plotly-Dashboards-with-Dash-master/Data/mpg.csv')
      
      data =[go.Histogram(x = df.mpg, xbins = dict(start = 0, end = 50, size = 2))]
      
      layout = go.Layout(title = 'Histogram')
      fig = go.Figure(data = data, layout = layout)
      pyo.plot(fig)

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/histogram.png)

<a name="9"></a>
### Distribution plots (Distplots)

+ typically layer three plots on top of one another
+ the first is histogram, where each data point is placed inside a bin of similar values
+ the second is a **rug plot** - marks are placed along the x-axis for every data point, which lets you see the distribution of values inside each bin 
+ third, **kernel density estimate** or KDE line that tries to describe the general shape of the distribution 

      import numpy as np
      import plotly.offline as pyo
      import plotly.figure_factory as ff
      
      # x = np.random.randn(1000)
      
      x1 = np.random.randn(200) -2
      x2 = np.random.randn(200)
      x3 = np.random.randn(200) + 2
      x4 = np.random.randn(200) + 4
      
      hist_data = [x1, x2, x3, x4] 
      
      group_labels =['x1', 'x2', 'x3', 'x4']
      
      fig = ff.create_distplot(hist_data, group_labels, bin_size=[.2,.1,.3,.4])
      pyo.plot(fig)

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/dist_plots.png)

<a name="10"></a>
### Heatmaps

+ Heatmaps allow the visualization of three features
+ Categorical or continuous features along the X and Y axis to make up a grid, and then a **third continuous feature** displayed through a color scale.
