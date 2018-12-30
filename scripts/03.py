import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 
GPIO.setup(12, GPIO.OUT)


p = GPIO.PWM(12, 200)
p.start(10)
while True:
	pass


p.stop()
GPIO.cleanup()
