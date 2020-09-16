# Flask
from flask import Flask, render_template

# plotly 
import plotly
import plotly.graph_objs as go

# other
import json
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    bar1 = create_plot()
    bar2 = create_plot()
    bar3 = create_plot()
    bar = [bar1, bar2, bar3]
    return render_template('home.html', len=len(bar), plot=bar)

def create_plot():
    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe

    data = [
        go.Scatter(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/sensor_management')
def sensor_management():
    return render_template("management.html")

if __name__ == '__main__':
    app.run()