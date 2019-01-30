import RPi.GPIO as GPIO
import serial
from time import sleep
from subprocess import call
   
class behaviours:
    def __init__(self,assistant):
        self.obj = serial.Serial('/dev/ttyACM0',9600)
        self.assis=assistant

    def VoiceHandler(self):
        while (self.obj.inWaiting()<1):
            pass
        temp=self.obj.read().decode()
        if (temp == str('w')):
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/win.wav'])
                    sleep(1)
                    call (['espeak', 'win'])
        elif (temp == str('l')):
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/lose.wav'])
                    sleep(1)
                    call (['espeak', 'Lose'])
        elif (temp == str('t')):
                    call (['espeak', 'oh we did the same move, let us play again'])
                    self.obj.write (b'p')
        elif (temp == str('a')):       
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/win.wav'])
                    sleep(1)
                    call (['espeak', 'win'])
        elif (temp == str('b')):
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/lose.wav'])
                    sleep(1)
                    call (['espeak', 'Lose'])
        elif (temp == str('c')): 
                    call (['espeak', 'I have 5 fingers'])
        elif (temp == str('e')):
                    call (['espeak', 'Love'])
                    self.obj.write (b'a')
        elif (temp == str('v')):
                    call (['espeak', 'Victory'])
                    self.obj.write (b'v')
        elif (temp == str('i')):
                    call (['espeak', 'Win']) 
                    self.obj.write (b'd')
    
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
        #VoiceHandler()
        while (self.obj.inWaiting()<1):
            pass
        temp=self.obj.read ()
        if (temp == bytes(b'e')):
                    self.assis.send_text_query("love")
                    #call (['espeak', 'Love'])
                    self.obj.write (b'a')
        if (temp == bytes(b'v')):
                    self.assis.send_text_query("Victory")
                    #call (['espeak', 'Victory'])
                    self.obj.write (b'v')
        if (temp == bytes(b'i')):
                    self.assis.send_text_query("Win")
                    #call (['espeak', 'Win']) 
                    self.obj.write (b'd')

    def countingFingers(self):
        self.obj.write(b'c') 
        #VoiceHandler()
        while (self.obj.inWaiting()<1):
            pass
        temp=self.obj.read ()
        if (temp == bytes(b'c')): 
                    self.assis.send_text_query("fingers")
                    #call (['espeak', 'I have 5 fingers'])
        
    def thumbUp(self):
        self.obj.write(b't')
        
    def Out (self):
        self.obj.write (b'u')
 
    def Hi(self):
        self.obj.write(b'h')
        
    def Bye(self):
        self.obj.write(b'b')
        
    def PlaySRP(self, func):
        self.obj.write(b'p') 
        #VoiceHandler()
        sleep(3)
        while (self.obj.inWaiting()<1):
            pass
        temp=self.obj.read().decode()
        if (temp == str('w')):
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/win.wav'])
                    sleep(1)
                    self.assis.send_text_query("win")
                    #call (['espeak', 'win'])
        elif (temp == str('l')):
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/lose.wav'])
                    sleep(1)
                    self.assis.send_text_query("lose")
                    #call (['espeak', 'Lose'])
        elif (temp == str('t')):
                    self.assis.send_text_query("tie")
                    #call (['espeak', 'oh we did the same move, let us play again'])
                    self.obj.write (b'p')

    def Memory(self):
        self.obj.write(b's')
        #VoiceHandler()
        while (self.obj.inWaiting()<1):
            pass
        temp=self.obj.read ()
        if (temp == bytes(b'a')):       
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/win.wav'])
                    sleep(1)
                    self.assis.send_text_query("win")
                    #call (['espeak', 'win'])
        elif (temp == bytes(b'b')):
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/lose.wav'])
                    sleep(1)
                    self.assis.send_text_query("lose")
                    #call (['espeak', 'Lose'])
        
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
