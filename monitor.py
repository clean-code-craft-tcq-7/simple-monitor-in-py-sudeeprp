
from time import sleep
import sys


def displayAlertMessage(message):
  print(message)
  for i in range(6):
    print('\r* ', end='')
    sys.stdout.flush()
    sleep(1)
    print('\r *', end='')
    sys.stdout.flush()
    sleep(1)


def is_in_range(value, min_value, max_value):
  return min_value <= value <= max_value


def temperature_ok(temperature):
  if not is_in_range(temperature, 95, 102):
    displayAlertMessage('Temperature critical!')
    return False
  return True


def pulse_rate_ok(pulseRate):
  if not is_in_range(pulseRate, 60, 100):
    displayAlertMessage('Pulse Rate is out of range!')
    return False
  return True 


def spo2_ok(spo2):
  if not is_in_range(spo2, 90, 100):
    displayAlertMessage('Oxygen Saturation out of range!')
    return False
  return True


def vitals_ok(temperature, pulseRate, spo2):
  return temperature_ok(temperature) and pulse_rate_ok(pulseRate) and spo2_ok(spo2)
