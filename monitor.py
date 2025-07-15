
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


def vitals_ok(temperature, pulseRate, spo2):
  if temperature > 102 or temperature < 95:
    displayAlertMessage('Temperature critical!')
    return False
  elif pulseRate < 60 or pulseRate > 100:
    displayAlertMessage('Pulse Rate is out of range!')
    return False
  elif spo2 < 90:
    displayAlertMessage('Oxygen Saturation out of range!')
    return False
  return True
