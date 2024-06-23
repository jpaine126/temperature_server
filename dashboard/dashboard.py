import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
from dash import Dash, Input, Output, callback, dcc, html
from plotly.subplots import make_subplots

app = Dash()

app.layout = html.Div(
    [
        html.H1(children="Title of Dash App", style={"textAlign": "center"}),
        html.Button("Submit", id="submit-val", n_clicks=0),
        dcc.Graph(id="graph-content"),
    ]
)


def load_data():
    data = requests.get("http://192.168.1.194:8000/api/readings")
    df = pd.DataFrame.from_records(data.json())
    df["temperature"] = (df["temperature"] * 1.8) + 32
    return df


@callback(Output("graph-content", "figure"), Input("submit-val", "n_clicks"))
def update_graph(value):
    df = load_data()
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=df["time"], y=df["temperature"], name="Temperature (F)"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=df["time"], y=df["humidity"], name="Humidity (%)"),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(title_text="Temperature and Humidity")

    # Set x-axis title
    fig.update_xaxes(title_text="Time")

    # Set y-axes titles
    fig.update_yaxes(title_text="Temperature (F)", secondary_y=False)
    fig.update_yaxes(title_text="Humidity (%)", secondary_y=True)

    return fig


if __name__ == "__main__":
    app.run(debug=True)
