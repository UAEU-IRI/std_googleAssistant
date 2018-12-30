
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 
GPIO.setup(12, GPIO.OUT)


p = GPIO.PWM(12, 50)
p.start(10)
while True:
	p.start(10)
	sleep(2)
	p.start(5)
	sleep(2)


p.stop()
GPIO.cleanup()
