import serial
from time import sleep
from subprocess import call

obj = serial.Serial('/dev/ttyACM0',9600)
sleep(3)
obj.write(b'p')
    

while True:
    if(obj.inWaiting()>0):
        temp=obj.read().decode()
        if(temp==str('w')):
            call (['aplay', '/home/pi/std_googleAssistant/scripts/lose.wav'])
            sleep(1)
            call (['espeak', 'I won, thank you for the game'])