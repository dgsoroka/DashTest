import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Подсчет количества символов'),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output'),
])


@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_output_div(input_value):
    return 'Вы ввели "{}" и количество символов равно {}'.format(input_value, len(input_value))


if __name__ == '__main__':
    app.run_server(debug=True)
