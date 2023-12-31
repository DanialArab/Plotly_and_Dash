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
5. [Interactive components](#19)
   1. [Single callbacks for interactivity](#20)
   2. [Dash callbacks for graphs ](#21)
   3. [Multiple inputs](#22)
   4. [Multiple outputs](#23)
6. [Controlling callbacks with State](#24)
7. [Interacting with visualizations](#25)
   1. [Hover over data](#26)
   2. [Click data](#27)
   3. [Selection data](#28)
  
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

      import dash
      import dash_core_components as dcc
      import dash_html_components as html 
      
      app = dash.Dash()
      
      app.layout = html.Div([
      
          html.Label('Dropdown'),
          dcc.Dropdown(options=[{'label': 'New York City',
                                 'value': 'NYC'},
                                 {'label': 'San Fransisco',
                                 'value': 'SF'}],
                      value='SF'),
      
          html.Label('Slider'), 
          dcc.Slider(min=-10, max=10, step=0.5, value=0,
                     marks={i: i for i in range(-10, 10)}),
      
          html.P(html.Label('Some Radio Items')),
          dcc.RadioItems(options=[{'label': 'New York City',
                                 'value': 'NYC'},
                                 {'label': 'San Fransisco',
                                 'value': 'SF'}],
                          value='SF')
      ])
      
      
      if __name__ == '__main__':
          app.run_server()


![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/core_components.png)

<a name="17"></a>
### Markdown with Dash

+ Dashboards can also display markdown text which allows for links, italics, bold texts, bullet lists, and a lot more functionality, more than just a normal string.
+ more details  <a href="https://commonmark.org/help">here</a> 

      import dash
      import dash_core_components as dcc
      import dash_html_components as html 
      
      app = dash.Dash()
      
      markkdown_txt = """
      ### Dash and Markdown
      Dash apps can be written in maarkdown.
      [links](http://commonmark.org/help)
      
      """
      
      app.layout = html.Div(
          dcc.Markdown(children=markkdown_txt)
      )
      
      
      if __name__ == '__main__':
          app.run_server()
    
![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/markdown.png)

<a name="18"></a>
### Using help() with Dash


      import dash_html_components as html 
      
      print(help(html.Div))

returns me back:

      Help on class Div in module builtins:
      
      class Div(dash.development.base_component.Component)
       |  A Div component.
       |  
       |  
       |  Keyword arguments:
       |  - children (optional): The children of this component
       |  - id (optional): The ID of this component, used to identify dash components
       |  in callbacks. The ID needs to be unique across all of the
       |  components in an app.
       |  - n_clicks (optional): An integer that represents the number of times
       |  that this element has been clicked on.
       |  - key (optional): A unique identifier for the component, used to improve
       |  performance by React.js while rendering components
       |  See https://reactjs.org/docs/lists-and-keys.html for more info
       |  - accessKey (optional): Defines a keyboard shortcut to activate or add focus to the element.
       |  - className (optional): Often used with CSS to style elements with common properties.
       |  - contentEditable (optional): Indicates whether the element's content is editable.
       |  - contextMenu (optional): Defines the ID of a <menu> element which will serve as the element's context menu.
       |  - dir (optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
       |  - draggable (optional): Defines whether the element can be dragged.
       |  - hidden (optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
       |  - lang (optional): Defines the language used in the element.
       |  - spellCheck (optional): Indicates whether spell checking is allowed for the element.
       |  - style (optional): Defines CSS styles which will override styles previously set.
       |  - tabIndex (optional): Overrides the browser's default tab order and follows the one specified instead.
       |  - title (optional): Text to be displayed in a tooltip when hovering over the element.
       |  - fireEvent (optional): A callback for firing events to dash.
       |  
       |  Available events:
       |  
       |  Method resolution order:
       |      Div
       |      dash.development.base_component.Component
       |      collections.abc.MutableMapping
       |      collections.abc.Mapping
       |      collections.abc.Collection
       |      collections.abc.Sized
       |      collections.abc.Iterable
       |      collections.abc.Container
       |      object
       |  
       |  Methods defined here:
       |  
       |  __init__(self, children=None, **kwargs)
       |  
       |  __repr__(self)
       |  
       |  ----------------------------------------------------------------------
       |  Data and other attributes defined here:
       |  
       |  __abstractmethods__ = frozenset()
       |  
       |  ----------------------------------------------------------------------
       |  Methods inherited from dash.development.base_component.Component:
       |  
       |  __delitem__(self, id)
       |      Delete items by ID in the tree of children.
       |  
       |  __getitem__(self, id)
       |      Recursively find the element with the given ID through the tree
       |      of children.
       |  
       |  __iter__(self)
       |      Yield IDs in the tree of children.
       |  
       |  __len__(self)
       |      Return the number of items in the tree.
       |  
       |  __setitem__(self, id, item)
       |      Set an element by its ID.
       |  
       |  to_plotly_json(self)
       |  
       |  traverse(self)
       |      Yield each item in the tree.
       |  
       |  ----------------------------------------------------------------------
       |  Data descriptors inherited from dash.development.base_component.Component:
       |  
       |  __dict__
       |      dictionary for instance variables (if defined)
       |  
       |  __weakref__
       |      list of weak references to the object (if defined)
       |  
       |  ----------------------------------------------------------------------
       |  Methods inherited from collections.abc.MutableMapping:
       |  
       |  clear(self)
       |      D.clear() -> None.  Remove all items from D.
       |  
       |  pop(self, key, default=<object object at 0x7f1036302050>)
       |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
       |      If key is not found, d is returned if given, otherwise KeyError is raised.
       |  
       |  popitem(self)
       |      D.popitem() -> (k, v), remove and return some (key, value) pair
       |      as a 2-tuple; but raise KeyError if D is empty.
       |  
       |  setdefault(self, key, default=None)
       |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
       |  
       |  update(*args, **kwds)
       |      D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
       |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
       |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
       |      In either case, this is followed by: for k, v in F.items(): D[k] = v
       |  
       |  ----------------------------------------------------------------------
       |  Methods inherited from collections.abc.Mapping:
       |  
       |  __contains__(self, key)
       |  
       |  __eq__(self, other)
       |      Return self==value.
       |  
       |  get(self, key, default=None)
       |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
       |  
       |  items(self)
       |      D.items() -> a set-like object providing a view on D's items
       |  
       |  keys(self)
       |      D.keys() -> a set-like object providing a view on D's keys
       |  
       |  values(self)
       |      D.values() -> an object providing a view on D's values
       |  
       |  ----------------------------------------------------------------------
       |  Data and other attributes inherited from collections.abc.Mapping:
       |  
       |  __hash__ = None
       |  
       |  __reversed__ = None
       |  
       |  ----------------------------------------------------------------------
       |  Class methods inherited from collections.abc.Collection:
       |  
       |  __subclasshook__(C) from abc.ABCMeta
       |      Abstract classes can override this to customize issubclass().
       |      
       |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
       |      It should return True, False or NotImplemented.  If it returns
       |      NotImplemented, the normal algorithm is used.  Otherwise, it
       |      overrides the normal algorithm (and the outcome is cached).
      
      None

<a name="19"></a>
## Interactive components


<a name="20"></a>
### Single callbacks for interactivity

So we already understand how we can adjust the layout of a dash application through the use of components, either HTML components or dash core components. Now let's see how to interact and connect to those same components through the use of **callbacks** through the following steps:

+ Create a function to return some desired output
+ Decorate that function with an **@app.callback** decorator
   + Set an output to a component id
   + Set an input to a component id
+ Connect the desired properties

      import dash
      import dash_html_components as html 
      import dash_core_components as dcc
      from dash.dependencies import Input, Output
      
      app = dash.Dash()
      
      app.layout = html.Div([
          dcc.Input(id='my-id', value='Initial Text', type='text'),
          html.Div(id='my-div')
      ])
      
      @app.callback(Output(component_id='my-div', component_property='children'),
                    [Input(component_id='my-id', component_property='value')])
      def update_output_div(input_value):
          return f'You entered: {input_value}'
      
      if __name__ == '__main__':
          app.run_server()

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/Callbacks.png)


<a name="21"></a>
### Dash callbacks for graphs 

      import dash
      import dash_html_components as html
      import dash_core_components as dcc
      from dash.dependencies import Input, Output
      import plotly.graph_objs as go
      import pandas as pd
      
      df = pd.read_csv('/home/danial/Desktop/mydash/dash_plotly_course_material/Plotly-Dashboards-with-Dash-master/Data/gapminderDataFiveYear.csv')
      
      
      # print(df.head())
      
      app = dash.Dash()
      
      year_options =[]
      
      for year in df['year'].unique():
          year_options.append({'label':str(year), 'value': year})
          
      app.layout = html.Div([
          dcc.Graph(id='graph'),
          dcc.Dropdown(id='year-picker', 
                       options=year_options,
                       value=df['year'].min())
      ])
      
      @app.callback(Output('graph', 'figure'),
                    [Input('year-picker', 'value')])
      def update_figure(selected_year):
      
          # Data only for the selected year from dropdown 
          filtered_df = df[df['year'] == selected_year]
          traces = []
          for continent_name in filtered_df['continent'].unique():
              df_by_continent = filtered_df[filtered_df['continent']==continent_name]
              traces.append(go.Scatter(
                  x = df_by_continent['gdpPercap'],
                  y = df_by_continent['lifeExp'],
                  mode='markers',
                  opacity=0.7,
                  marker ={'size': 15},
                  name=continent_name
              ))
          return {'data':traces,
                  'layout': go.Layout(title='My Plot',
                                      xaxis = {'title': 'GDP per Cap', 'type': 'log'},
                                      yaxis = {'title': 'Life Expectancy'}
                                      )}
      
      if __name__ == '__main__':
          app.run_server()

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/callbacks_for_graphs.png)

<a name="22"></a>
### Multiple inputs

Let's see how we can connect multiple inputs to a single output in a graph. 

      import dash
      import dash_html_components as html
      import dash_core_components as dcc
      from dash.dependencies import Input, Output
      import plotly.graph_objs as go
      import pandas as pd
      
      df = pd.read_csv('/home/danial/Desktop/mydash/dash_plotly_course_material/Plotly-Dashboards-with-Dash-master/Data/mpg.csv')
      
      # print(df.head())
      
      
      app = dash.Dash()
      
      features = df.columns
      
      app.layout = html.Div([
          html.Div([
              dcc.Dropdown(id='xaxis',
                           options=[{'label': i, 'value': i} for i in features],
                           value='displacement')
          ], style={'width': '48%', 'display': 'inline-block'}),
          html.Div([
              dcc.Dropdown(id='yaxis',
                           options=[{'label': i, 'value': i} for i in features],
                           value='mpg')
          ], style={'width': '48%', 'display': 'inline-block'}),
          dcc.Graph(id='feature-graphic')
      
      ], style={'padding': 10})
      
      
      @app.callback(Output('feature-graphic', 'figure'),
                    [Input('xaxis', 'value'),
                     Input('yaxis', 'value')])
      def update_graph(xaxis_name, yaxis_name):
          return {'data': [go.Scatter(x=df[xaxis_name], 
                                      y = df[yaxis_name],
                                      text = df['name'],
                                      mode = 'markers',
                                      marker = {'size': 15,
                                                'opacity': 0.5,
                                                'line': {'width': 0.5, 'color': 'white'}})]
                  
                  
                  , 'layout': go.Layout(title = 'My Dashboard for MPG',
                                        xaxis={'title': xaxis_name},
                                        yaxis = {'title': yaxis_name},
                                        hovermode='closest')}
      
      if __name__ == '__main__':
          app.run_server()
          
![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/multiple_inputs.png)

<a name="23"></a>
### Multiple outputs

      import dash
      import dash_html_components as html
      import dash_core_components as dcc
      from dash.dependencies import Input, Output
      import plotly.graph_objs as go
      import pandas as pd
      
      df = pd.read_csv('/home/danial/Desktop/mydash/dash_plotly_course_material/Plotly-Dashboards-with-Dash-master/Data/wheels.csv')
      
      # print(df.head())
      
      app = dash.Dash()
      
      app.layout = html.Div([
          dcc.RadioItems(id='wheels',
                         options = [{'label': i, 'value': i} for i in df['wheels'].unique()],
                         value = 1
                         ),
          html.Div(id='wheels-output'),
          html.Hr(),
          dcc.RadioItems(id='colors',
                         options = [{'label': i, 'value': i} for i in df['color'].unique()],
                         value = 'blue'),
          html.Div(id='colors-output')
      ], style = {'fontFamily': 'helvetica', 'fontize': 18})
      
      
      @app.callback(Output('wheels-output', 'children'),
                  [Input('wheels', 'value')])
      def callback_a(wheels_value):
          return f"You chose {wheels_value}"
      
      
      @app.callback(Output('colors-output', 'children'),
                  [Input('colors', 'value')])
      def callback_b(colors_value):
          return f"You chose {colors_value}"
      
      
      if __name__ == '__main__':
          app.run_server()
          
![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/multiple_outputs.png)

let's see how we can update the image:

      import dash
      import dash_html_components as html
      import dash_core_components as dcc
      from dash.dependencies import Input, Output
      import plotly.graph_objs as go
      import pandas as pd
      import base64
      
      directory = '/home/danial/Desktop/mydash/dash_plotly_course_material/Plotly-Dashboards-with-Dash-master/Data/'
      
      df = pd.read_csv(directory+'wheels.csv')
      # print(df.head())
      
      app = dash.Dash()
      
      def encode_image(image_file):
          encoded = base64.b64encode(open(image_file, 'rb').read())
          return f'data:{directory}+image/png;base64,{encoded.decode()}' 
      
      
      app.layout = html.Div([
          dcc.RadioItems(id='wheels',
                         options = [{'label': i, 'value': i} for i in df['wheels'].unique()],
                         value = 1
                         ),
          html.Div(id='wheels-output'),
          html.Hr(),
          dcc.RadioItems(id='colors',
                         options = [{'label': i, 'value': i} for i in df['color'].unique()],
                         value = 'blue'),
          html.Div(id='colors-output'),
          html.Img(id='display-image', src='children', height=300)
      ], style = {'fontFamily': 'helvetica', 'fontize': 18})
      
      
      @app.callback(Output('wheels-output', 'children'),
                  [Input('wheels', 'value')])
      def callback_a(wheels_value):
          return f"You chose {wheels_value}"
      
      
      @app.callback(Output('colors-output', 'children'),
                  [Input('colors', 'value')])
      def callback_b(colors_value):
          return f"You chose {colors_value}"
      
      
      @app.callback(Output('display-image', 'src'),
                    [Input('wheels', 'value'),
                     Input('colors', 'value')]) 
      def callback_image(wheel, color):
          path = directory + 'Images/'
          return encode_image(path+df[(df['wheels']==wheel) &\
                                           (df['color']== color)]['image'].values[0])
                                          
      
      if __name__ == '__main__':
          app.run_server()
    
![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/multiple_outputs_2.png)


<a name="24"></a>
## Controlling callbacks with State

+ In the previous interactive examples, we have seen how inputs **immediately** affect outputs: as soon as values are entered the page updates to reflect any changes
+ What if we want to wait before displaying the page? what is we want time to enter a series of changes before submitting them? ---> State
+ We achieve this using **dash.dependencies.State**
+ Dash offers the ability to store saved changes and send them back on command
+ You can think of this as hitting a submit button on a form
+ **State() is added to the @app.callback along with an Input() and Output()**
+ The state is then connected to a component id and a property id to report back
+ You can check the component API docs to see what properties are available for the components 

      import dash
      import dash_html_components as html
      import dash_core_components as dcc
      from dash.dependencies import Input, Output, State 
      
      
      app = dash.Dash()
      
      app.layout = html.Div([
          dcc.Input(id='number-in', value=1, style={'fontSize': 24}),
          html.Button(id='submit-button',
                      n_clicks=0,
                      children='Submit Here',
                      style={'fontSize': 24}),
          html.H1(id='number-out')
      ])
      
      
      @app.callback(Output('number-out', 'children'),
                    [Input('submit-button', 'n_clicks')],
                    [State('number-in', 'value')])
      
      def output(n_clicks, number):
          return f"{number} was typed in, and button was clicked {n_clicks} times"
      
      if __name__ == '__main__':
          app.run_server() 

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/controlling_callbacks_with_state.png)

<a name="25"></a>
## Interacting with visualizations

<a name="26"></a>
### Hover over data

+ When we hover over Plotly graphs, information is displayed
+ This info can be served internally using **JSON** and then parsed for specific info
+ Every graph has a **hoverData** component property that can be accessed

      import dash
      import dash_core_components as dcc
      import dash_html_components as html 
      from dash.dependencies import Input, Output
      import plotly.graph_objs as go 
      import pandas as pd
      import json 
      import base64
      
      app = dash.Dash()
      
      directory = '/home/danial/Desktop/mydash/dash_plotly_course_material/Plotly-Dashboards-with-Dash-master/Data/' 
      
      df = pd.read_csv(directory + 'wheels.csv')
      
      
      def encode_image(image_file):
          encoded = base64.b64encode(open(image_file, 'rb').read())
          return f'data:{directory}+image/png;base64,{encoded.decode()}' 
      
      # print(df.head())
      
      app.layout = html.Div([
          html.Div(dcc.Graph(id='wheels-plot',
                             figure={'data': [go.Scatter(
                                 x=df['color'],
                                 y=df['wheels'],
                                 dy = 1,
                                 mode='markers',
                                 marker ={'size': 15}
                             )],
                                  'layout': go.Layout(title='Test', hovermode='closest')}), 
                                  style={'width': '30%', 'float': 'left'}),
          html.Div([html.Img(id='hover-data', src='children', height = 300)],
                   style = {'paddingTop': 35})
      ])
      
      @app.callback(Output('hover-data', 'src'),
                    [Input('wheels-plot', 'hoverData')])
      def callback_image(hoverData):
          wheel = hoverData['points'][0]['y']
          color = hoverData['points'][0]['x']
          path = directory + 'Images/'
          return encode_image(path+df[(df['wheels']==wheel) &\
                                             (df['color']== color)]['image'].values[0])
      
      if __name__ == '__main__':
          app.run_server()

![](https://github.com/DanialArab/images/blob/main/Plotly_and_Dash/hover-over-data.png)

<a name="27"></a>
### Click data

The only required change to the previous script, above, is 

      @app.callback(Output('hover-data', 'src'),
                    [Input('wheels-plot', 'clickData')])

now, to see the changes in the dashboard we do need to click on the plot and not just hover over it.

<a name="28"></a>
### Selection data

