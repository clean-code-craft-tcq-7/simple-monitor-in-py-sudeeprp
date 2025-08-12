
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


def alert_if_not_in_range(value, min_value, max_value, alert_message):
  if not is_in_range(value, min_value, max_value):
    displayAlertMessage(alert_message)
    return False
  return True

def temperature_ok(temperature):
  return alert_if_not_in_range(temperature, 95, 102, 'Temperature critical!')

def pulse_rate_ok(pulseRate):
  return alert_if_not_in_range(pulseRate, 60, 100, 'Pulse Rate is out of range!')

def spo2_ok(spo2):
  return alert_if_not_in_range(spo2, 90, 100, 'Oxygen Saturation out of range!')

def blood_sugar_ok(bloodSugar):
  return alert_if_not_in_range(bloodSugar, 70, 110, 'Blood Sugar is out of range!')

def vitals_ok(temperature, pulseRate, spo2):
  return temperature_ok(temperature) and pulse_rate_ok(pulseRate) and spo2_ok(spo2)

def report_is_normal(report):
  return (temperature_ok(report['temperature']) and
          pulse_rate_ok(report['pulseRate']) and
          spo2_ok(report['spo2']) and
          blood_sugar_ok(report['bloodSugar']))
