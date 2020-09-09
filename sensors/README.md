# sensors
The `Sensor` class can be used to instantiate a temperature or humidity sensor. Once instantiated you can then get readings by calling `getReading()`.

The reading interface that the sensor returns is defined as `SensorReading` in `sensors.py` and is of the shape:  
`{sensorId: str, value: float, timeStamp: str, sensorType: str}`