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