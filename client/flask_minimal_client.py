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
@app.route('/<name>')
def hello_world(name=None):
    bar = create_plot()
    return render_template('test.html', name=name, plot=bar)

def create_plot():
    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe

    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/login')
def sso_login():
    # sso login
    pass

if __name__ == '__main__':
    app.run()