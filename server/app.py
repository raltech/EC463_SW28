from flask import Flask, jsonify, request, render_template
import db

import plotly
import plotly.graph_objs as go
import json
import numpy as np
import pandas as pd
from plotting import create_plot

app = Flask(__name__)


@app.route('/user/<string:user_id>', methods=['GET'])
def home(user_id: str):
    conn = db.getConnection()
    sensors = db.getSensors(conn, user_id)
    plots = list(map(lambda x: create_plot(x[0], x[1]), sensors))
    names = list(map(lambda x: x[1], sensors))
    sensorTypes = list(map(lambda x: x[0], sensors))
    plotInfo = zip(plots, names, sensorTypes)
    return render_template('home.html', plotInfo=plotInfo)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/sensor_management')
def sensor_management():
    return render_template("sensor_management.html")


"""


@app.route('/user/<string:user_id>/sensors', methods=['GET'])
def get_sensors(user_id: str):
    conn = db.getConnection()
    print(db.getSensors(conn, user_id))
    return jsonify(success=True)

"""


@app.route('/user/<string:user_id>/sensors', methods=['POST'])
def add_sensor(user_id: str):
    conn = db.getConnection()
    try:
        db.addSensor(
            conn, user_id, request.json['sensorType'], request.json['name'])
    except:
        return "Need to supply sensorType: {'temperature', 'humidity} and name", 400
    return jsonify(success=True)


if __name__ == "__main__":
    app.run()
