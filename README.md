# EC463_SW28
This repo is for EC463 Mini software project.
We (Hayato Nakamura and Quinn Meurer) are implementing Home Sensor application using mainly Python/Flask and some JavaScript.

## Home Sensor

[Live Demo](https://sw-miniproject.herokuapp.com/)
[Video Demo](https://youtu.be/r9fRvjjXQ_k)

### Client side
- Single Sign On for account management
- Access to the server database to register new sensors and delete existing sensors
- Get real-time sensor data
- Get current weather data
- View graphs of sensor data
- View account info in profile page

### Server side
- stores list of sensors and their associated user ID in a SQLITE3 database
- provide API to client app to get sensors and add/delete sensors
- serve web pages to client
- establish websocket connection with client to communicate stream of sensor data in real time

## How to run
- 

## Acknowledgement
used library and frameworks
- flask (server and client)
- httplib2 (client)
- plotly (client)
- openweathermap.org
- atlastk (removed)
