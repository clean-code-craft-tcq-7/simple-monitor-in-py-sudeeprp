
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


def temperature_ok(temperature):
  if temperature > 102 or temperature < 95:
    displayAlertMessage('Temperature critical!')
    return False
  return True


def pulse_rate_ok(pulseRate):
  if pulseRate < 60 or pulseRate > 100:
    displayAlertMessage('Pulse Rate is out of range!')
    return False
  return True 


def spo2_ok(spo2):
  if spo2 < 90:
    displayAlertMessage('Oxygen Saturation out of range!')
    return False
  return True


def vitals_ok(temperature, pulseRate, spo2):
  return temperature_ok(temperature) and pulse_rate_ok(pulseRate) and spo2_ok(spo2)
