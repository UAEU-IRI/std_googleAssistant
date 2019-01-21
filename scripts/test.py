import serial
from time import sleep

obj = serial.Serial('/dev/ttyACM0',9600)

while True:
    if(obj.inWaiting()>0):
        print(obj.read()==bytes(b'a'))