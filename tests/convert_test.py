import unittest
from lmdparser.GLMObservation import GLMObservation
import datetime

# Static input string to test
test_string1 = '20163260000045172   09  -4.9 999.9 360  8.0 99.9 999 9999.9 1027.2  8.8  2.0 99.9'

class TestStringConversion(unittest.TestCase):
    def test_convert_string_to_datadict(self):
        self.maxDiff = 1000
        expected_dict = {'station_type': 'Buoy', 'water_body': 'Superior', 'air_temp': '-4.9',
                         'dewpoint': '999.9', 'wind_dir': '360', 'wind_speed': '8.0', 
                         'wind_gust': '99.9', 'cloud_cover': '999', 'solar': '9999.9', 
                         'pressure': '1027.2', 'water_temp': '8.8', 'wave_height': '2.0',
                         'wave_period': '99.9'}

        self.assertDictEqual(GLMObservation.convert_string_to_datadict(test_string1), expected_dict)

    def test_convert_string_instance(self):
        output_obj = GLMObservation.convert_string(test_string1)
        self.assertIsInstance(output_obj, GLMObservation)

    def test_properties1(self):
        obs = GLMObservation.convert_string(test_string1)
        
        self.assertEqual(obs.obs_time, datetime.datetime(2016, 11, 21, 0, 0, 0))
        self.assertEqual(obs.station_id, '45172')
        self.assertEqual(obs.station_type, 'Buoy')
        self.assertEqual(obs.water_body, 'Superior')
        self.assertEqual(obs.air_temp, -4.9)
        self.assertEqual(obs.dewpoint, None)
        self.assertEqual(obs.wind_direction, 360)
        self.assertEqual(obs.wind_speed, 8.0)
        self.assertEqual(obs.wind_gust, None)
        self.assertEqual(obs.cloud_cover, None)
        self.assertEqual(obs.solar_radiation, None)
        self.assertEqual(obs.pressure, 1027.2)
        self.assertEqual(obs.water_temp, 8.8)
        self.assertEqual(obs.sig_wave_height, 2.0)
        self.assertEqual(obs.wave_period, None)

if __name__ == '__main__':
    unittest.main()