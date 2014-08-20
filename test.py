import unittest
from pressure_bot import *

class TestMTB(unittest.TestCase):

	def test_diff_ordered_dates_seconds(self):
		start_date = '2014-07-22 12:51:22'
		end_date = '2014-07-22 12:51:23'
		self.assertEqual(get_time_diff(end_date, start_date), '1 second')

	def test_diff_ordered_dates_minutes(self):
		start_date = '2014-07-22 12:43:22'
		end_date = '2014-07-22 12:51:34'
		self.assertEqual(get_time_diff(end_date, start_date), '8 minutes 12 seconds')

	def test_diff_ordered_dates_hours(self):
		start_date = '2014-07-22 11:41:24'
		end_date = '2014-07-22 12:51:26'
		self.assertEqual(get_time_diff(end_date, start_date), '1 hour 10 minutes 2 seconds')

	def test_diff_ordered_dates_days(self):
		start_date = '2014-07-20 11:41:24'
		end_date = '2014-07-22 12:51:26'
		self.assertEqual(get_time_diff(end_date, start_date), '2 days 1 hour 10 minutes 2 seconds')

	def test_diff_ordered_dates_weeks(self):
		start_date = '2014-07-05 11:41:24'
		end_date = '2014-07-22 12:51:26'
		self.assertEqual(get_time_diff(end_date, start_date), '2 weeks 3 days 1 hour 10 minutes 2 seconds')

if __name__ == '__main__':
    unittest.main()