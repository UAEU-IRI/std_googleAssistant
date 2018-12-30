from mylib import Servo
from time import sleep


servo1=Servo();


servo1.attach(12)

while True:
	servo1.write(180)
	sleep(2)
	servo1.write(0)
	sleep(2)

