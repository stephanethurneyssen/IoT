import serial, time
from grove.grove_air_quality_sensor_v1_3 import GroveAirQualitySensor
import seeed_dht
from Adafruit_IO import Client, RequestError, Feed

ADAFRUIT_IO_USERNAME = "StephaneThurneyssen"
ADAFRUIT_IO_KEY = "aio_sbdd13JnvgvZxpg4IEFOS6tdTAEn"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# connect to alalog pin 2(slot A2)
PIN = 0
baudrate = 9600
ser = serial.Serial('/dev/ttyUSB0', baudrate)
# for DHT11/DHT22
sensor2 = seeed_dht.DHT("22", 12)

sensor = GroveAirQualitySensor(PIN)

def create_feed_if_not_exist(feed_name):
    global feed_to_create
    try:
        feed_to_create = aio.feeds(feed_name)
    except RequestError:  # Doesn't exist, create a new feed
        feed = Feed(name=feed_name)
        feed_to_create = aio.create_feed(feed)

create_feed_if_not_exist("pmtwofive")
create_feed_if_not_exist("pmten")
create_feed_if_not_exist("temp")
create_feed_if_not_exist("humidity")
create_feed_if_not_exist("airquality")

while True:
    value = sensor.value        
#     if value > 100:
#         print("{}, High Pollution.".format(value))
#     else:
#         print("{}, Air Quality OK.".format(value)) 
    msg = ser.read(10)
    pm25 = (msg[3] * 256 + msg[2]) / 10.0
    pm10 = (msg[5] * 256 + msg[4]) / 10.0
#     print('pmtwofive = %s μ/m^3' % pm25) #For debug only
#     print('pmten = %s μ/m^3' % pm10)
    humi, temp = sensor2.read()
#     if not humi is None:
#         print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor2.dht_type, humi, temp))
#     else:
#         print('DHT{0}, humidity & temperature: {1}'.format(sensor2.dht_type, temp))
        
    aio.send('pmtwofive', pm25)
    aio.send('pmten', pm10)
    aio.send('airquality', format(value))
    aio.send('temp', temp)
    aio.send('humidity', humi)
        
    time.sleep(10) #Every 5 sec
    

    
    