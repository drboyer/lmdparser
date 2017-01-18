import unittest
from lmdparser.GLMObservation import GLMObservation
import datetime

ship_teststring = '201701712563WDE3568  9   1.1 999.9 220  4.6 99.9 100 9999.9 1026.0  3.3  1.0  2.0 45.70 82.80'

class TestStringConversion(unittest.TestCase):
    def test_ship_location(self):
        obs = GLMObservation.convert_string(ship_teststring)
        self.assertEqual(obs.ship_latitude, 45.70)
        self.assertEqual(obs.ship_longitude, -82.80)

    def test_ship_report(self):
        obs = GLMObservation.convert_string(ship_teststring)

        self.assertEqual(obs.obs_time, datetime.datetime(2017, 1, 17, 12, 56, 0))
        self.assertEqual(obs.station_id, 'WDE3568')
        self.assertEqual(obs.station_type, 'Ship Report')
        self.assertEqual(obs.water_body, None)
        self.assertEqual(obs.air_temp, 1.1)
        self.assertEqual(obs.dewpoint, None)
        self.assertEqual(obs.wind_direction, 220)
        self.assertEqual(obs.wind_speed, 4.6)
        self.assertEqual(obs.wind_gust, None)
        self.assertEqual(obs.cloud_cover, 100)
        self.assertEqual(obs.solar_radiation, None)
        self.assertEqual(obs.pressure, 1026.0)
        self.assertEqual(obs.water_temp, 3.3)
        self.assertEqual(obs.sig_wave_height, 1.0)
        self.assertEqual(obs.wave_period, 2.0)
        self.assertEqual(obs.ship_latitude, 45.70)
        self.assertEqual(obs.ship_longitude, -82.80)

if __name__ == '__main__':
    unittest.main()