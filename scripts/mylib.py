import RPi.GPIO as GPIO
import serial
from time import sleep
   
class behaviours:
	def __init__(self):
		self.obj = serial.Serial('/dev/ttyS0',9600)
	
	def closeHand(self):
	  self.obj.write('l')
	  
	def victoryFunction(self):
		self.obj.write('v')
		
	def openHand(self):
		self.obj.write('o')
		
	def showNumberOne(self):
		self.obj.write('1')
		
	def showNumberTwo(self):
		self.obj.write('2')
		
	def showNumberThree(self):
		self.obj.write('3')
		
	def showNumberFour(self):
		self.obj.write('4')
		
	def showNumberFive(self):
		self.obj.write('5')
		
	def countingNumbers(self):
		self.obj.write('c')
		
	def thumbUp(self):
		self.obj.write('t')
		
	def Hi(self):
		self.obj.write('h')
		
	def Bye(self):
		self.obj.write('b')
		
	def PlaySRP(self):
		self.obj.write('p')
		
	def Memory(self):
		self.obj.write('s')
		
	def HandWakeUp(self):
		self.obj.write('w')
	
	def finishResponse(self):
		self.obj.write('r')
	  
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
