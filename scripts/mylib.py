import RPi.GPIO as GPIO
import serial
from time import sleep
from subprocess import call
   
class behaviours:
	def __init__(self):
		self.obj = serial.Serial('/dev/ttyS0',9600)
	
	def closeHand(self):
	  self.obj.write(b'l')
	  
	def victoryFunction(self):
		self.obj.write(b'v')
		
	def openHand(self):
		self.obj.write(b'o')
		
	def showNumberOne(self):
		self.obj.write(b'1')
		
	def showNumberTwo(self):
		self.obj.write(b'2')
		
	def showNumberThree(self):
		self.obj.write(b'3')
		
	def showNumberFour(self):
		self.obj.write(b'4')
		
	def showNumberFive(self):
		self.obj.write(b'5')
		
	def countingNumbers(self):
		self.obj.write(b'c')
		
	def thumbUp(self):
		self.obj.write(b't')
		
	def Hi(self):
		self.obj.write(b'h')
		
	def Bye(self):
		self.obj.write(b'b')
		
	def PlaySRP(self):
		self.obj.write(b'p')
		
	def Memory(self):
		self.obj.write(b's')
		
	def HandWakeUp(self):
		call(['aplay','/home/pi/std_googleAssistant/scripts/ding.wav'])
		self.obj.write(b'w')
	
	def finishResponse(self):
		self.obj.write(b'r')
	  
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
