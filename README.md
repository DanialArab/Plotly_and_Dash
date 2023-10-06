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
3. [Dash Basics - Layout](#11)
   1. [Dash layout](#12)
   2. [Converting Plotly to Dash](#13)
4. [Dashboard components](#14)
   1. [html components](#15)
   2. [Core components](#16)
   3. [Markdown with Dash](#17)
   4. [Using help() with Dash](#18) 

   
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

      import pandas as pd
      import plotly.graph_objs as go
      import plotly.offline as pyo 
      
      
      df = pd.read_csv('/home/danial/Desktop/mydash/dash_plotly_course_material/Plotly-Dashboards-with-Dash-master/Data/2010SantaBarbaraCA.csv')
      
      # print (df.head())
      
      data = [go.Heatmap(x=df['DAY'], y = df['LST_TIME'],
                   z = df['T_HR_AVG'].values.tolist())]
      
      layput= go.Layout(title = 'SB CA Temps')
      
      fig = go.Figure(data=data, layout=layput) 
      pyo.plot(fig)

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/heatmap_plot.png)

we can have multiple heatmaps on the same plot, we use tools from plotly to generate subplots:

      import pandas as pd
      import plotly.graph_objs as go
      import plotly.offline as pyo 
      from plotly import tools
      
      directory = '/home/danial/Desktop/mydash/dash_plotly_course_material/Plotly-Dashboards-with-Dash-master/Data/'
      
      df1 = pd.read_csv(directory + '2010SantaBarbaraCA.csv')
      df2 = pd.read_csv(directory + '2010SitkaAK.csv')
      df3 = pd.read_csv(directory + '2010YumaAZ.csv')
      
      trace1 = go.Heatmap(x=df1['DAY'], 
                          y = df1['LST_TIME'],
                          z = df1['T_HR_AVG'], 
                          colorscale='Jet',
                          zmin = 5,
                          zmax = 40)
      
      trace2 = go.Heatmap(x=df2['DAY'], 
                          y = df2['LST_TIME'],
                          z = df2['T_HR_AVG'], 
                          colorscale='Jet',
                          zmin = 5,
                          zmax = 40)
      
      trace3 = go.Heatmap(x=df3['DAY'], 
                          y = df3['LST_TIME'],
                          z = df3['T_HR_AVG'], 
                          colorscale='Jet',
                          zmin = 5,
                          zmax = 40)
      
      fig = tools.make_subplots(rows=1, cols=3, 
                                subplot_titles=['SB CA', 'Sitka AK', 'Yuma AZ'],
                                shared_yaxes=False)
      
      fig.append_trace (trace1, 1, 1)
      fig.append_trace (trace2, 1, 2)
      fig.append_trace (trace3, 1, 3)
      
      fig['layout'].update(title='Temps for three cities')
      pyo.plot(fig)

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/heatmaps_subplots.png)

<a name="11"></a>
## Dash Basics - Layout

+ Dash is for creating dashboards purely in Python.
+ Typically, for things in the past, you would have had to have known all the front-end technologies to create a dashboard web application such as HTML, CSS, and JavaScript. But Dash allows you to do this all purely in Python, and then these dashboards are served as web applications.
+ We can connect and interact with dashboards
+ Dash apps are mainly composed of two parts: 
   + The layout of the app, which describes what the application actually looks like. It is where your visualizations are going to go inside your dashboard.
   + The second part of Dash describes the interactivity of the application. For example, if you move a slider in your dashboard, how does that affect the visualization?
+ The good news is you don't actually need to know any HTML or CSS to use dash. We get to do all of this purely in Python:
   + Most HTML tags are provided as Python classes within dash
+ Dash offers two distinct component libraries:
   + dash_html_components library contains a Python component for every HTML tag like the first-level heading H1
   + dash_core_components library offers higher-level interactive components that are generated with JavaScript, HTML, and CSS through the React.js library

<a name="12"></a>
### Dash layout

         import dash
         import dash_core_components as dcc 
         import dash_html_components as html 
         
         
         app = dash.Dash()
         
         app.layout = html.Div(
         
             children = [html.H1('Hello Dash!'), 
                         html.Div('Dash: web dashboaards with Python')
         
             ]
         )
         
         if __name__ == '__main__':
             app.run_server()


with a plot incorporated in the dashboard:

         import dash
         import dash_core_components as dcc 
         import dash_html_components as html 
         
         
         app = dash.Dash()
         
         app.layout = html.Div(
         
             children = [html.H1('Hello Dash!'), 
                         html.Div('Dash: web dashboaards with Python'),
                         dcc.Graph(id='example',
                                    figure={'data': [
                                        {'x':[1,2,3], 'y':[4,1,2], 'type': 'bar', 'name':'SF'},
                                        {'x':[1,2,3], 'y':[2,4,5], 'type': 'bar', 'name':'NYC'}
                                    ],
                                            'layout':{
                                                'title': ' BAR PLOTS'
                                            }})
         
             ]
         )
         
         if __name__ == '__main__':
             app.run_server()

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/dashboard.png)
  

      import dash
      import dash_core_components as dcc 
      import dash_html_components as html 
      
      
      app = dash.Dash()
      
      colors = {'background': '#111111', 'text': '#7FDBFF'}
      
      app.layout = html.Div(
      
          children = [html.H1('Hello Dash!', style ={'textAlign': 'center',
                                                     'color': colors['text']}), 
      
                      dcc.Graph(id='example',
                                 figure={'data': [
                                     {'x':[1,2,3], 'y':[4,1,2], 'type': 'bar', 'name':'SF'},
                                     {'x':[1,2,3], 'y':[2,4,5], 'type': 'bar', 'name':'NYC'}
                                 ],
                                         'layout':{
                                             'plot_bgcolor': colors['background'],
                                             'paper_bgcolor': colors['background'],
                                             'font': {'color': colors['text']},
                                             'title': ' BAR PLOTS'
                                         }})
      
          ], style={'backgroundColor': colors['background']}
      )
      
      if __name__ == '__main__':
          app.run_server()


![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/dashboard_styling.png)


<a name="13"></a>
### Converting Plotly to Dash 

+ Dash allows us to easily insert Plotly graphs into the dashboard.

      import dash
      import dash_core_components as dcc
      import dash_html_components as html
      import plotly.graph_objs as go 
      import numpy as np
      
      app = dash.Dash()
      
      np.random.seed(42)
      
      random_x = np.random.randint(1, 101, 100)
      random_y = np.random.randint(1, 101, 100)
      
      
      app.layout = html.Div([dcc.Graph(id='scatterplot',
                                       figure = {'data':[
                                           go.Scatter(
                                               x = random_x,
                                               y=random_y,
                                               mode = 'markers',
                                               marker ={
                                                   'size' : 12,
                                                   'color': 'rgb(51,201,153)',
                                                   'symbol': 'pentagon',
                                                   'line': {'width': 2}
                                               }
                                           )],
                                       'layout': go.Layout(title='My Scatterplot',
                                                           xaxis = {'title': 'Some X title'})},
                                                           
                                       ), dcc.Graph(id='scatterplot2',
                                       figure = {'data':[
                                           go.Scatter(
                                               x = random_x,
                                               y=random_y,
                                               mode = 'markers',
                                               marker ={
                                                   'size' : 12,
                                                   'color': 'rgb(200,201,53)',
                                                   'symbol': 'pentagon',
                                                   'line': {'width': 2}
                                               }
                                           )],
                                       'layout': go.Layout(title='My Scatterplot2',
                                                           xaxis = {'title': 'Some X title'})},
                                                           
                                       )])
      
      if __name__ == '__main__':
          app.run_server()
    
![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/converting_plotly_to_dash.png)


<a name="14"></a>
## Dashboard components

+ Dash components are provided by two main libraries:
   + dash_html_components
   + dash_core_components 
+ html components describe the layout of the page including placement and alignment of different graphs, you can apply CSS stylings to those HTML components
+ dcc components describe the individual graphs themselves 

<a name="15"></a>
### html components

Dash allows us to leverage previous knowledge of HTML and CSS to create very customized dashboards:
+ the main process is to pick the relevant HTML component from the HTML component library with Dash,
+ then we can insert parameters into the HTML components.
+ then we adjust a CSS style dictionary which allows you to also define a general CSS style dictionary for our entire web application 

Technically, no knowledge of HTML or CSS is truly needed to create a dashboard because we're never actually writing pure HTML or pure CSS. Instead, we're just doing calls to a Python library that does it for us. But in order to actually stylize and customize dashboards, especially to your specific liking, it's really going to be helpful to understand HTML and CSS to really get an idea of what these actual Python calls are doing.

Some clarification:
+ An HTML Div element is a division:
   + It is a section or block of the web app (dashboard)
+ CSS allows for styling HTML elements:
   + fonts, colors, borders, etc.
   + Dash uses dictionaries to pass in CSS style calls

         import dash
         import dash_html_components as html 
         
         app = dash.Dash()
         
         app.layout = html.Div(['This is the outermost Div!',
                                html.Div('This is the inner Div!',
                                         style = {'color': 'red',
                                                  'border': '2px red solid'}),
                                 html.Div('Another inner Div!',
                                          style ={'collor': 'blue',
                                                  'border': '3px blue solid'})],
                               style={'color': 'green',
                                      'border': '2px green solid'})
      
      
         if __name__ == '__main__':
             app.run_server()

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/html_components.png)


<a name="16"></a>
### Core components

+ Dah core components are more abstract (higher level) calls that allow us to quickly insert common components into our dashboard
+ A reference to all available dash core components can be found <a href="https://dash.plotly.com/dash-core-components">here</a>


<a name="17"></a>
### Markdown with Dash

<a name="18"></a>
### Using help() with Dash


