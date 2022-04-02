import unittest
from datetime import datetime

import vehicle_delay_between_stops


class MyTestCase(unittest.TestCase):

    def test_build_between_stops_from_row(self):
        row = 'WAWA;208_2_448_1445;208;9227;4006_02;Dickensa;2021-12-11T14:23:42;0;4005_10;Bitwy Warszawskiej 1920 r.;2021-12-11T14:23:26;0;0;4005_10;Bitwy Warszawskiej 1920 r.'

        vehicle_lives = vehicle_delay_between_stops.build_from_row(row.split(';'))

        self.assertEqual(vehicle_lives.city_code, 'WAWA')
        self.assertEqual(vehicle_lives.course_identifier, '208_2_448_1445')
        self.assertEqual(vehicle_lives.line, '208')
        self.assertEqual(vehicle_lives.vehicle_number, '9227')

        self.assertEqual(vehicle_lives.current_stop_id, '4006_02')
        self.assertEqual(vehicle_lives.current_stop_name, 'Dickensa')
        self.assertEqual(vehicle_lives.time, datetime(2021, 12, 11, 14, 23, 42))
        self.assertEqual(vehicle_lives.delay_in_seconds, 0)

        self.assertEqual(vehicle_lives.previous_stop_id, '4005_10')
        self.assertEqual(vehicle_lives.previous_stop_name, 'Bitwy Warszawskiej 1920 r.')
        self.assertEqual(vehicle_lives.time_minus_1_stop, datetime(2021, 12, 11, 14, 23, 26))
        self.assertEqual(vehicle_lives.delay_in_seconds_minus_1_stop, 0)

        self.assertEqual(vehicle_lives.delta_delay_in_seconds, 0)
        self.assertEqual(vehicle_lives.delay_at_stop_id, '4005_10')
        self.assertEqual(vehicle_lives.delay_at_stop_name, 'Bitwy Warszawskiej 1920 r.')

        self.assertEqual(vehicle_lives.get_bus_stops_key(), 'WAWA::4005_10->4006_02')
        self.assertEqual(vehicle_lives.get_bus_stops_key_by_hour(), 'WAWA::4005_10->4006_02::14:00')


if __name__ == '__main__':
    unittest.main()
