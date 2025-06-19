import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):

    def setUp(self):
        self.car_park = CarPark("456 Sensor Street", 2)
        self.entry_sensor = EntrySensor("E1", True, self.car_park)
        self.exit_sensor = ExitSensor("X1", True, self.car_park)

    def test_entry_sensor_detect_vehicle_adds_car(self):
        initial_count = len(self.car_park.plates)
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), initial_count + 1)

    def test_exit_sensor_detect_vehicle_removes_car(self):
        # First add a car manually
        self.car_park.add_car("FAKE-123")
        initial_count = len(self.car_park.plates)
        self.exit_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), initial_count - 1)

if __name__ == "__main__":
    unittest.main()
