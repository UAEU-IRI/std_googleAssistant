import RPi.GPIO as GPIO
import serial
from time import sleep
from subprocess import call
   
class behaviours:
	def __init__(self):
		self.obj = serial.Serial('/dev/ttyACM0',9600)
	
	def victoryFunction(self):
		self.obj.write(b'v')
		
	def closeHand(self):
	    self.obj.write(b'l')
		
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
	
	def LeaderMohammed (self):
		self.obj.write (b'm')
		while (self.obj.inWaiting()<1):
			pass
		temp=self.obj.read ()
		if (temp == bytes(b'e')):
					call (['espeak', 'Love'])
					self.obj.write (b'a')
		if (temp == bytes(b'v')):
					call (['espeak', 'Victory'])
					self.obj.write (b'v')
		if (temp == bytes(b'i')):
					call (['espeak', 'Win']) 
					self.obj.write (b'd')

	def countingFingers(self):
		self.obj.write(b'c') 
		while (self.obj.inWaiting()<1):
			pass
		temp=self.obj.read ()
		if (temp == bytes(b'c')): 
					call (['espeak', 'I have 5 fingers'])
		
	def thumbUp(self):
		self.obj.write(b't')
		
	def Out (self):
		self.obj.write (b'u')
 
	def Hi(self):
		self.obj.write(b'h')
		
	def Bye(self):
		self.obj.write(b'b')
		
	def PlaySRP(self):
		self.obj.write(b'p') 
		while (self.obj.inWaiting()<1):
			pass
		temp=self.obj.read ()
		if (temp == bytes(b'w')):
					call (['espeak', 'win'])
				#call (['aplay', '/home/pi/std_googleAssistant/scripts/win.wav']) 
		elif (temp == bytes(b'l')):
					call (['espeak', 'lose'])
				#call (['aplay', '/home/pi/std_googleAssistant/scripts/lose.wav']) 
		elif (temp == bytes(b't')):
					call (['espeak', 'oh we did the same move, let us play again'])
					self.obj.write (b'p')

	def Memory(self):
		self.obj.write(b's')
		while (self.obj.inWaiting()<1):
			pass
		temp=self.obj.read ()
		if (temp == bytes(b'a')):
					call (['espeak', 'win'])		
					#call (['aplay', '/home/pi/std_googleAssistant/scripts/win.wav']) 	
		elif (temp == bytes(b'b')):
					call (['espeak', 'lose'])
					#call (['aplay', '/home/pi/std_googleAssistant/scripts/lose.wav'])
		
	def HandWakeUp(self):
		self.obj.write(b'w')
		call(['aplay','/home/pi/std_googleAssistant/scripts/ding.wav'])
	
	def finishResponse(self):
		self.obj.write(b'r')
	
	def Out(self):
		self.obj.write(b'u')
	  
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
