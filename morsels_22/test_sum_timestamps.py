import unittest

from morsels_22.sum_timestamps import sum_timestamps


class SumTimeStampsTests(unittest.TestCase):

    """Tests for sum_timestamps."""

    def test_single_timestamp(self):
        self.assertEqual(sum_timestamps(['02:01']), '2:01')
        self.assertEqual(sum_timestamps(['2:01']), '2:01')

    def test_multiple_timestamps(self):
        self.assertEqual(sum_timestamps(['02:01', '04:05']), '6:06')
        self.assertEqual(sum_timestamps(['9:38', '4:45', '3:52']), '18:15')

    def test_many_timestamps(self):
        times = [
            '3:52', '3:29', '3:23', '4:05', '3:24', '2:29', '2:16', '2:44',
            '1:58', '3:21', '2:51', '2:53', '2:51', '3:32', '3:20', '2:40',
            '2:50', '3:24', '3:22', '0:42']
        self.assertEqual(sum_timestamps(times), '59:26')

    def test_no_minutes(self):
        self.assertEqual(sum_timestamps(['00:01', '00:05']), '0:06')
        self.assertEqual(sum_timestamps(['0:38', '0:15']), '0:53')

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_timestamps_over_an_hour(self):
        times = [
            '3:52', '3:29', '3:23', '4:05', '3:24', '2:29', '2:16', '2:44',
            '1:58', '3:21', '2:51', '2:53', '2:51', '3:32', '3:20', '2:40',
            '2:50', '3:24', '1:20', '3:22', '3:26', '0:42', '5:20']
        self.assertEqual(sum_timestamps(times), '1:09:32')
        times2 = [
            '50:52', '34:29', '36:23', '47:05', '32:24', '20:29', '22:16',
            '23:44', '19:58', '30:21', '24:51', '22:53', '23:51', '34:32',
            '36:20', '25:40', '27:50', '39:24', '18:20', '36:22', '4:00',
        ]
        self.assertEqual(sum_timestamps(times2), '10:12:04')

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_allow_optional_hour(self):
        self.assertEqual(sum_timestamps(['1:02:01', '04:05']), '1:06:06')
        self.assertEqual(
            sum_timestamps(['9:05:00', '4:45:10', '3:52']),
            '13:54:02',
        )
        self.assertEqual(sum_timestamps(['1:02:01', '40:01:05', '10:57:30']), '52:00:36')


if __name__ == "__main__":
    unittest.main(verbosity=2)