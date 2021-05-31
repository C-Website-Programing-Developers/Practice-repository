import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(
    __name__,
    # 从国内可顺畅访问的cdn获取所需的原生bootstrap对应css
    external_stylesheets=['https://cdn.staticfile.org/twitter-bootstrap/4.5.2/css/bootstrap.min.css']
)

app.layout = html.Div(
    dbc.Spinner(dbc.Container(
    [
        html.Br(),
        html.H1('欢迎来到南开大学C语言学习网站！'),
        html.H3('我们励志开发南开人自己的雨课堂！'),
        html.Hr(),
        dcc.Location(id='url'),
        dcc.Link('Part 1 基础知识', href='/pageA', refresh=True),
        html.Br(),
        dcc.Link('Part 2 数据处理与表示', href='/pageB'),
        html.Br(),
        dcc.Link('Part 3 选择与迭代算法', href='/pageC', refresh=True),
        html.Br(),
        dcc.Link('Part 4 结构化数据的处理', href='/pageD'),
        html.Br(),
        dcc.Link('Part 5 模块化', href='/pageE'),
        html.Br(),
        dcc.Link('Part 6 数据存储', href='/pageF', refresh=True),
        html.Br(),
        dcc.Link('Part 7 面向对象方法', href='/pageG'),
        html.Br(),
        dcc.Link('Part 8 继承与多态', href='/pageH'),
        html.Br(),
        dcc.Link('Part 9 输入输出流', href='/pageI', refresh=True),
        html.Br(),
        dcc.Link('Part 10 模板', href='/pageJ'),
        html.Br(),
        dcc.Link('Part 11 数据结构和算法的基本概念.docx', href='/pageK'),
        html.Br(),
        dcc.Link('Part 12 线性表', href='/pageL', refresh=True),
        html.Br(),
        html.Hr(),
        html.H1(id='render-page-content')
    ],
    style={
                'paddingTop': '30px',
                'paddingBottom': '50px',
                'borderRadius': '10px',
                'boxShadow': 'rgb(0 0 0 / 20%) 0px 13px 30px, rgb(255 255 255 / 80%) 0px -13px 30px'
            }
),
fullscreen=True
)
)



@app.callback(
    Output('render-page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
    if pathname == '/':
        return '欢迎来到首页'

    elif pathname == '/pageA':
        return '欢迎来到页面A'

    elif pathname == '/pageB':
        return '欢迎来到页面B'

    elif pathname == '/pageC':
        return '欢迎来到页面C'

    else:
        return '当前页面不存在！'


if __name__ == '__main__':
    app.run_server(debug=True)
