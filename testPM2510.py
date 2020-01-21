import serial, time

# Create an instance of the REST client.
baudrate = 9600
ser = serial.Serial('/dev/ttyUSB0', baudrate)

while True:
    msg = ser.read(10)
    pm25 = (msg[3] * 256 + msg[2]) / 10.0
    pm10 = (msg[5] * 256 + msg[4]) / 10.0
    print('pmtwofive = %s μ/m^3' % pm25) #For debug only
    print('pmten = %s μ/m^3' % pm10)
    time.sleep(10) #Every 10 sec