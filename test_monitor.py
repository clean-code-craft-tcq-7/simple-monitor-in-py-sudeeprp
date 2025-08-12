import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):

    def test_ok_when_all_vitals_in_range(self):
        self.assertTrue(vitals_ok(98.1, 70, 98))

    def test_not_ok_when_temperature_low(self):
        self.assertFalse(vitals_ok(94, 70, 98))

    def test_not_ok_when_temperature_high(self):
        self.assertFalse(vitals_ok(103, 70, 98))

    def test_not_ok_when_pulse_rate_high(self):
        self.assertFalse(vitals_ok(98.1, 102, 70))

    def test_not_ok_when_pulse_rate_low(self):
        self.assertFalse(vitals_ok(98.1, 40, 70))

    def test_not_ok_when_spo2_low(self):
        self.assertFalse(vitals_ok(98.1, 70, 85))


if __name__ == '__main__':
  unittest.main()
