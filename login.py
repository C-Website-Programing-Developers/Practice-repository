from logging import debug
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(
    __name__,
    # 从国内可顺畅访问的cdn获取所需的原生bootstrap对应css
    external_stylesheets=['https://cdn.staticfile.org/twitter-bootstrap/4.5.2/css/bootstrap.min.css']
)

app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Container(
            [
                dbc.Row(style={'height': '30px'}),  # 利用css设置高度
                dbc.Row(
                    dbc.Col('User‘s Name')
                ),
                dbc.Row(
                    [
                        dbc.Col(dbc.Input(id='input-value1',
                                          placeholder='请输入您的用户名'),
                                width=12),
                        dbc.Col(dbc.Label(id='output-value1'),
                                width=12)
                    ]
                ),
                dbc.Row(
                    dbc.Col('Password')
                ),
                dbc.Row(
                    [
                        dbc.Col(dbc.Input(id='input-value2',
                                          placeholder='请输入您的账户密码'),
                                width=12),
                        dbc.Col(dbc.Label(id='output-value2'),
                                width=12)
                    ]
                ),
                dbc.Row(
                    dbc.Col(
                        [
                            'By signing up you accept our ',
                            html.A('Terms Of Use', href='#')
                        ],
                        width={'size': 10, 'offset': 1},
                        style={'text-align': 'center'}  # 利用css设置文字居中
                    ),
                    style={'margin': '6px'}  # 利用css设置上下留白高度
                ),
                dbc.Row(
                    dbc.Col(
                        # 利用css实现圆角矩形效果
                        dbc.Button('LOGIN', style={'border-radius': '18px'}, block=True),
                        width={'size': 8, 'offset': 2},
                        style={'text-align': 'center'}
                    )
                ),
                dbc.Row(
                    [
                        dbc.Col(html.Hr()),
                        html.P('or', style={'text-align': 'center', 'margin': 0}),
                        dbc.Col(html.Hr())
                    ]
                ),
                dbc.Row(
                    dbc.Col(
                        dbc.Button(
                            'Signup using Google',
                            style={'border-radius': '18px'},
                            block=True,
                            outline=True
                        ),
                        width={'size': 8, 'offset': 2},
                        style={'text-align': 'center'}
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        [
                            "Don't have account? ",
                            html.A('Sign up here', href='#')
                        ],
                        width={'size': 10, 'offset': 1},
                        style={'text-align': 'center'}
                    ),
                    style={'margin': '6px'}
                ),
                html.Br(),
            ],
            style={
                'background-color': '#ededef',  # 设置背景颜色
                'max-width': '480px',  # 为Container部件设置最大宽度
                'border-radius': '12px'
            }
        )
    ]
)


@app.callback(
    [Output('output-value1', 'children'),
     Output('output-value2', 'children')],
    [Input('input-value1', 'value'),
     Input('input-value2', 'value')]
)
def input_to_output(value1, value2):

    try:
        return '用户姓名：' + value1, f'账户密码长度为{len(value2)}'
    except:
        return '等待输入...', '等待输入...'



if __name__ == '__main__':
    app.run_server(debug = True)
