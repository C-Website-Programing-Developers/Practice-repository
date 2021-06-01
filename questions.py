import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import json


app = dash.Dash(
    __name__,
    # 从国内可顺畅访问的cdn获取所需的原生bootstrap对应css
    external_stylesheets=['https://cdn.staticfile.org/twitter-bootstrap/4.5.2/css/bootstrap.min.css']
)

app.layout = html.Div(
    dbc.Container(
        dbc.Tabs(
            [
                dbc.Tab(
                    [
                        html.Div(
    dbc.Container(
        [
            html.Br(),
            dbc.Row(dbc.Col('1.下列关于C++类的描述中错误的是()',width={'size': 4, 'offset': 1})
               ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dbc.Button('A', id='A', n_clicks=0),width=1),
                    dbc.Col(html.P('类与类之间可以通过一些手段进行通信和联络', id='A-output')),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(dbc.Button('B', id='B', n_clicks=0),width=1),
                    dbc.Col(html.P('类用于描述事物的属性和对事物的操作', id='B-output'))
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(dbc.Button('C', id='C', n_clicks=0),width=1),
                    dbc.Col(html.P('类与类之间必须是平等的关系，而不能组成层次关系', id='C-output')),
                ]
            )
        ]
    )
)
                    ],
                    label='题目1'
                ),
                dbc.Tab(
                    [
                        html.Br(),
                        html.P('这是选项卡2')
                    ],
                    label='题目2'
                ),
                dbc.Tab(label='查看答题信息',
                        tab_style={'margin-left': 'auto'},
                        active_label_style={'color': 'green'}),
            ]
        ),
        style={'margin-top': '100px'}
    )
)

@app.callback(
    [Output('A-output', 'children'),
     Output('B-output', 'children'),
     Output('C-output', 'children')],
    [Input('A', 'n_clicks'),
     Input('B', 'n_clicks'),
     Input('C', 'n_clicks')],
     [State('A', 'valuea'),
     State('B', 'valueb'),
     State('C', 'valuec')],
    prevent_initial_call=True
)

def input_to_output(A_n_clicks, valuea):

    if A_n_clicks:
        return 'wrong'

def input_to_output(B_n_clicks, valueb):

    if B_n_clicks:
        return 'wrong'

def input_to_output(C_n_clicks, valuec):

    if C_n_clicks:
        return 'right'

if __name__ == '__main__':
    app.run_server(debug=True)
