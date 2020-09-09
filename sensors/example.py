"""
Some example usage of the Sensor class
"""

from sensors import Sensor

temperatureSensor = Sensor("temperature")
reading = temperatureSensor.getReading()
reading2 = temperatureSensor.getReading()
reading3 = temperatureSensor.getReading()
print(reading)
print(reading['value'])
print(reading2['value'])
print(reading3['value'])
