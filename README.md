# EC463_SW28
This repo is for EC463 Mini software project.
We (Hayato Nakamura and Quinn Meurer) are implementing Home Sensor application using mainly Python/Flask and some JavaScript.

## Home Sensor
- [Live Demo](https://sw-miniproject.herokuapp.com/)  
  - Our app is hosted using Heroku platform, and you can access it by clicking the link above.
- [Video Demo](https://youtu.be/r9fRvjjXQ_k)
  - You can watch video demonstration of our app by clicking the link above.

#### Application Features
- **Client side**
  - Single Sign On for account management
  - Access to the server database to register new sensors and delete existing sensors
  - Display real-time sensor data in home page.
  - Display plot of the historical sensor data in home page.
  - Display current weather data 
    - Users can update their location anytime in profile page.
  - View account info associated with google account in profile page.
  - Logout button to safely log out from our app.

- **Server side**
  - stores list of sensors and their associated user ID in a SQLITE3 database
  - provide API to client app to get sensors and add/delete sensors
  - serve web pages to client
  - establish websocket connection with client to communicate stream of sensor data in real time

## How to run
**Note: our app is hosted [here](https://sw-miniproject.herokuapp.com/) so that you can play with it without installing**
After cloning our repo into your local computer, install necessary libraries listed in requirement.txt.
Then, create a run.sh file under server folder with the following content:
```
export FN_AUTH_REDIRECT_URI=http://127.0.0.1:8040/google/auth
export FN_BASE_URI=http://127.0.0.1:8040
export FN_CLIENT_ID=INSERT_Google_OAuth_2.0_Client_ID
export FN_CLIENT_SECRET=INSERT_Google_OAuth_2.0_Client_Secret_Key
export WEATHER_API_KEY=INSERT_Openweathermap_API_KEY

export FLASK_APP=app.py
export FLASK_DEBUG=1
export FN_FLASK_SECRET_KEY=1234

python3 -m flask run -p 8040
```
In order to run our app, you need to have two api keys:
1. OpenWeatherMap
   - https://openweathermap.org/api
2. Google OAuth 2.0 Client
   - https://console.cloud.google.com/apis/credentials 

Once you set up your account, replace 
```
export FN_CLIENT_ID=INSERT_Google_OAuth_2.0_Client_ID
export FN_CLIENT_SECRET=INSERT_Google_OAuth_2.0_Client_Secret_Key
export WEATHER_API_KEY=INSERT_Openweathermap_API_KEY
```
with your IDs and Keys.

Finally, you can type 
```
cd server
. run.sh
```
in your terminal to run our app.
With the default setting, you should be able to access the web app by going to http://127.0.0.1:8040 in your browser.

## Testing Application
- [x] Support Google SSO
- [x] Receive and display temperature and humidity from a sensor
- [x] Plot historical sensor data
- [x] Users have access and can see the weather information for the their location
- [x] Multiple people can access the app
- [x] Multiple sources of temperature and humidity
  - Users can easily add/delete sensors within app
- [x] Multiple temperature or humidity sources can be associated with a user
  - Every sensors are associated with unique user id obtained from their Google account.

## Acknowledgement
Used library and frameworks
- flask (server and client)
- plotly (client)
- OpenWeatherMap API
  - https://openweathermap.org/api
- Google OAuth 2.0 Client
   - https://console.cloud.google.com/apis/credentials 
