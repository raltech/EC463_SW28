# Flask
from flask import Flask, render_template, request, abort

# plotly 
import plotly
import plotly.graph_objs as go

# other
import json
import numpy as np
import pandas as pd
import urllib.request
import functools
import os
import geocoder

# google oauth
from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery
import google_auth

app = Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)
app.register_blueprint(google_auth.app)

# openweathermap
API_KEY = ''

def tocelcius(temp):
    return str(round(float(temp) - 273.16,2))

@app.route('/')
def welcome():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()

        g = geocoder.ip('me')
        lat = str(np.floor(g.latlng[0]))
        lon = str(np.floor(g.latlng[1]))

        # source contain json data from api
        try:
            # source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='+API_KEY).read()
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid='+API_KEY).read()
        except:
            city = 'boston (default)'
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=boston&appid='+API_KEY).read()
        
        # converting json data to dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "temp_cel": tocelcius(list_of_data['main']['temp']) + ' Celcius',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "cityname":g.address,
        }

        bar1 = create_plot()
        bar2 = create_plot()
        bar3 = create_plot()
        bar = [bar1, bar2, bar3]

        return render_template('home.html',data=data, len=len(bar), plot=bar, user_info=user_info)

    return render_template('welcome.html')
    # return 'You are not currently logged in.'

@app.route('/home', methods=['GET','POST'])
def home():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
    #     return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"

    """
    Returns page prompting for a zip code or containing weather for a specific zip code
    :return:
    """
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'boston'

    # source contain json data from api
    try:
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='+API_KEY).read()
    except:
        city = 'boston (default)'
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=boston&appid='+API_KEY).read()
    # converting json data to dictionary

    list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "temp_cel": tocelcius(list_of_data['main']['temp']) + 'C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "cityname":str(city),
    }

    bar1 = create_plot()
    bar2 = create_plot()
    bar3 = create_plot()
    bar = [bar1, bar2, bar3]

    return render_template('home.html',data=data, len=len(bar), plot=bar, user_info=user_info)


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
    return render_template("sensor_management.html")

@app.route('/profile')
def profile():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        return render_template("profile.html", user_info=user_info)
    else:
        return render_template("welcome.html")

if __name__ == '__main__':
    app.run()