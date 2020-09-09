import uuid
import random
from typing import TypedDict
from abc import ABC
from datetime import datetime


class SensorReading(TypedDict):
    sensorId: str
    value: float
    timeStamp: str
    sensorType: str


class Sensor:
    def __init__(self, sensorType: str):
        if sensorType != "temperature" and sensorType != "humiditity":
            raise Exception(
                'sensorType must be in {"temperature", "humidity"}')

        self.lastValue: float = None
        self.sensorType: str = sensorType
        self.sensorId: str = str(uuid.uuid4())

    def getReading(self) -> SensorReading:
        newValue = None
        if self.lastValue is None:
            # If this is the first value for this sensor pick a random float between 0 and 100
            newValue = random.random() * 100
        else:
            # newValue is some random number in the range of .9 * lastValue to 1.1 * lastValue
            newValue = self.lastValue + \
                (random.random() * .2 - .1) * self.lastValue

        reading: SensorReading = {
            'sensorId': self.sensorId,
            'value': newValue,
            'timeStamp': datetime.now().strftime("%H:%M:%S"),
            'sensorType': self.sensorType
        }

        self.lastValue = newValue
        return reading
