import unittest
from sensors import Sensor


class TestSensor(unittest.TestCase):
    def test_bad_sensorType(self):
        with self.assertRaises(Exception) as context:
            Sensor("bad value")

        self.assertEqual(
            'sensorType must be in {"temperature", "humidity"}', str(context.exception))

    def test_reading(self):
        temperatureSensor = Sensor("temperature")
        reading = temperatureSensor.getReading()
        self.assertTrue(reading['value'] >= 0 and reading['value'] <= 100)


if __name__ == '__main__':
    unittest.main()
