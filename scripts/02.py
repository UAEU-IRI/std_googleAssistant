import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)


GPIO.output(12,GPIO.HIGH)
