import time
from grove.grove_air_quality_sensor_v1_3 import GroveAirQualitySensor

# connect to alalog pin 2(slot A2)
PIN = 0

sensor = GroveAirQualitySensor(PIN)

print('Detecting ...') 
while True:
    value = sensor.value        
    if value > 100:
        print("{}, High Pollution.".format(value))
    else:
        print("{}, Air Quality OK.".format(value))
    time.sleep(.1)
