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
