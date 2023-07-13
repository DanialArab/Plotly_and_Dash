# Plotly and Dash

Reference: Interactive Python Dashboards with Plotly and Dash Udemy course


1. [Introduction](#1)
2. [Plotly Basics](#2)
   1. [Scatter PLots](#3)
   2. [Line Charts](#4)
   3. [Bar Charts](#5)



   
<a name="1"></a>
## Introduction

Introduction

+ Dash is built upon Flask.
+ Matplotlib creates static image files
+ Seaborn is designed to ctaete nice looking statistical plots (static plots)
+ Plotly:
  + is the open source library which is a general data visualization librray focused on **interactive** visualizations
  + has libraries for JavaScript, React, R, and Python (the most popular version is the Python library)
  + using plotly Python library we can craete interactive plots as **.html** files
  + while users can still interact with these plots (zoom in, select, hover over), these plots cannot be connected to chaniging data sources that is why we need Dash
  + so plotly is great when we want some little interactive image that you knwo the data source behind it is going to be static and not changing
+ Dash:
  + we often want plots to be able to interact with each other, interact with components, or have plots update in real time. To accomplish these we need a dashboard
  + Dash is an open source librray from the Plotly company that allows you to create a full dashboard with multiple components, interactivity, and multiple plots
  + Dash produces a dashboard web applicationin in which we can interact with the dashboard
  + since Dash renders a full web app, we can then deploy our dashboards online for other people to use 


<a name="2"></a>
## Plotly Basics

Documentation: https://plotly.com/python/
    
<a name="3"></a>
### Scatter plots

They allow the comparison of two variables for a set of data.

<a name="4"></a>
### Line Charts

+ A line chart displays a series of data points (markers) connected by line segments
+ It is similar to a scatter plot except that the measurement points are **ordered (typically by their x-axis value)** and joined with straight line segments
+ Often used to visualize a **trend in data over intervals of time - known as a time series** 

<a name="5"></a>
### Bar Charts

+ A bar chart presents **categorical data** with rectangular bars with heights (or lengths) proportional to the values that they represent
+ Typically the x-axis is the categories and the y-axis is the count (number of occurances) in each category
+ The y-axis can also be any aggregarion (count, sum, average, etc.)
+ Stacked bar charts vs. nested bar charts 




