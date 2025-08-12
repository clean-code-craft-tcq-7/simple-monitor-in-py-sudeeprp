import unittest
from unittest.mock import patch
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):

    @patch('monitor.displayAlertMessage')
    def test_ok_when_all_vitals_in_range(self, mock_alert):
        self.assertTrue(vitals_ok(98.1, 70, 98))
        mock_alert.assert_not_called()

    @patch('monitor.displayAlertMessage')
    def test_not_ok_when_temperature_low(self, mock_alert):
        self.assertFalse(vitals_ok(94, 70, 98))
        mock_alert.assert_called_once_with('Temperature critical!')

    @patch('monitor.displayAlertMessage')
    def test_not_ok_when_temperature_high(self, mock_alert):
        self.assertFalse(vitals_ok(103, 70, 98))
        mock_alert.assert_called_once_with('Temperature critical!')

    @patch('monitor.displayAlertMessage')
    def test_not_ok_when_pulse_rate_high(self, mock_alert):
        self.assertFalse(vitals_ok(98.1, 102, 70))
        mock_alert.assert_called_once_with('Pulse Rate is out of range!')

    @patch('monitor.displayAlertMessage')
    def test_not_ok_when_pulse_rate_low(self, mock_alert):
        self.assertFalse(vitals_ok(98.1, 40, 70))
        mock_alert.assert_called_once_with('Pulse Rate is out of range!')

    @patch('monitor.displayAlertMessage')
    def test_not_ok_when_spo2_low(self, mock_alert):
        self.assertFalse(vitals_ok(98.1, 70, 85))
        mock_alert.assert_called_once_with('Oxygen Saturation out of range!')


if __name__ == '__main__':
  unittest.main()
