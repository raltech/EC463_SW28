import plotly
import plotly.graph_objs as go
import json
import numpy as np
import pandas as pd
import sensors


def create_plot(sensorType: str, sensorName: str):
    N = 40
    x = np.linspace(0, 1, N)
    y = []
    sensor = sensors.Sensor(sensorType)
    for i in range(0, N):
        y.append(sensor.getReading()['value'])

    df = pd.DataFrame({'x': x, 'y': y})  # creating a sample dataframe

    data = [
        go.Scatter(
            x=df['x'],  # assign x as the dataframe column 'x'
            y=df['y'],
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
