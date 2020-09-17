from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_socketio import SocketIO
import db
import sensors

import random
import plotly
import plotly.graph_objs as go
import json
import numpy as np
import pandas as pd
from plotting import create_plot
import urllib.request
import functools
import os

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth

app = Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)
app.register_blueprint(google_auth.app)
socketio = SocketIO(app)

API_KEY = os.environ.get("WEATHER_API_KEY", default=False) # openweathermap

def tocelcius(temp):
    return str(round(float(temp) - 273.16,2))

@app.route('/')
def welcome():
    if google_auth.is_logged_in():
        return redirect(url_for('home'))
    return render_template('welcome.html',)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if not google_auth.is_logged_in():
        return redirect(url_for('welcome'))

    user_id = google_auth.get_user_info()['id']
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'boston'

    try:
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='+API_KEY).read()
    except:
        city = 'boston (default)'
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=boston&appid='+API_KEY).read()

    list_of_data = json.loads(source)
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "temp_cel": tocelcius(list_of_data['main']['temp']) + 'C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "cityname":str(city).title(),
    }

    conn = db.getConnection()
    sensors = db.getSensors(conn, user_id)
    plots = list(map(lambda x: create_plot(x[0], x[1]), sensors))
    names = list(map(lambda x: x[1], sensors))
    sensorTypes = list(map(lambda x: x[0], sensors))
    plotInfo = zip(plots, names, sensorTypes)
    return render_template('home.html', plotInfo=plotInfo, data=data, user_info=google_auth.get_user_info())


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/sensor_management')
def sensor_management():
    id = google_auth.get_user_info()['id']
    return render_template("sensor_management.html", user_id = id)

@app.route('/profile')
def profile():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        return render_template("profile.html", user_info=user_info)
    else:
        return redirect(url_for('welcome'))


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

@app.route('/user/<string:user_id>/sensors/delete', methods=['POST'])
def delete_sensor(user_id: str):
    conn = db.getConnection()
    db.deleteSensor(conn, user_id, request.json['name'], request.json['sensorType'])
    return jsonify(success=True)

@socketio.on('test')
def test(payload, methods=["GET","POST"]):
    print("YOYOYOOYOYOY")

@socketio.on('getVal')
def sendVal(payload, methods=["GET", "POST"]):
    x = sensors.Sensor(payload['sensorType'], payload['previousValue'])
    socketio.emit(payload['name'] + payload['sensorType'], x.getReading()['value'])

if __name__ == "__main__":
    socketio.run()
