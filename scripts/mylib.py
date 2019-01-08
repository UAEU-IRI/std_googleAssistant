import RPi.GPIO as GPIO
import serial
from time import sleep
   
class behaviours:
	def __init__(self):
		try: 
			self.obj = serial.Serial('/dev/ttyS0',9600)
		except: 
				pass	 
	def closeHand(self):
	  self.obj.write('l')
	  
	def victoryFunction(self):
		self.obj.write('v')
	  
class Servo:
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False) 
	
	def attach(self,pin):
		GPIO.setup(pin, GPIO.OUT)
		self.p = GPIO.PWM(pin, 50)

	
	def write(self,ang):
		self.p.start((ang*5.0)/180.0+5.0)
		
	def __del__(self):
		p.stop()
		GPIO.cleanup()
