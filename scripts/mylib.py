import RPi.GPIO as GPIO
import serial
from time import sleep
from subprocess import call
from tkinter import*
import webbrowser
   
class behaviours:
    def __init__(self):
        self.obj = serial.Serial('/dev/ttyACM0',9600)

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
        temp=self.obj.read().decode()
        if (temp == str('e')):
                    #self.assis.send_text_query("love")
                    call (['espeak', 'Love'])
                    self.obj.write (b'a')
        if (temp == str('v')):
                    #self.assis.send_text_query("Victory")
                    call (['espeak', 'Victory'])
                    self.obj.write (b'v')
        if (temp == str('i')):
                    #self.assis.send_text_query("Win")
                    call (['espeak', 'Win']) 
                    self.obj.write (b'd')

    def countingFingers(self):
        self.obj.write(b'c') 
        #call (['espeak', '1'])
        #call (['espeak', '2'])
        #call (['espeak', '3'])
        #call (['espeak', '4'])
        #call (['espeak', '5'])
        call (['espeak', 'I have 5 fingers'])
        #VoiceHandler()
        #while (self.obj.inWaiting()<1):
        #    pass
        #temp=self.obj.read().decode()
        #if (temp == str('c')): 
                    #self.assis.send_text_query("fingers")
        
    def On(self):
        self.obj.write(b'q') 
        while (self.obj.inWaiting()<1):
            pass
        temp=self.obj.read().decode()
        if (temp == str('q')): 
                    #self.assis.send_text_query("fingers")
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/Voice/HandOn.wav'])

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
        #VoiceHandler()
        #sleep(3)
        call (['aplay', '/home/pi/std_googleAssistant/scripts/Voice/Intro.wav'])
        while (self.obj.inWaiting()<1):
            pass
        temp=self.obj.read().decode()
        if (temp == str('w')):
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/Voice/win.wav'])
                    #self.assis.send_text_query("win")
                    call (['espeak', 'win'])
        elif (temp == str('l')):
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/Voice/lose.wav'])
                    #self.assis.send_text_query("lose")
                    call (['espeak', 'Lose'])
        elif (temp == str('t')):
                    #self.assis.send_text_query("tie")
                    call (['espeak', 'oh we did the same move, let us play again'])
                    self.obj.write (b'p')

    def Memory(self):
        self.obj.write(b's')
        #VoiceHandler()
        while (self.obj.inWaiting()<1):
            pass
        temp=self.obj.read().decode()
        if (temp == str('a')):       
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/Voice/win.wav'])
                    sleep(1)
                    #self.assis.send_text_query("win")
                    call (['espeak', 'win'])
        elif (temp == str('b')):
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/Voice/lose.wav'])
                    sleep(1)
                    #self.assis.send_text_query("lose")
                    call (['espeak', 'Lose'])
        
    def HandWakeUp(self):
        self.obj.write(b'w')
        call(['aplay','/home/pi/std_googleAssistant/scripts/Voice/ding.wav'])
    
    def finishResponse(self):
        self.obj.write(b'r')
    
    def Out(self):
        self.obj.write(b'u')
      
    def BTS(self):
        self.obj.write(b'z')
        call(['aplay','/home/pi/std_googleAssistant/scripts/Voice/IDOL.wav'])

    def Funny(self):
        self.obj.write(b'y')
        call(['aplay','/home/pi/std_googleAssistant/scripts/Voice/Funny1.wav'])
        
    def IFA(self):
        self.obj.write(b'n')
        call(['python','/home/pi/std_googleAssistant/GUI/Codes/LogoGif.py'])
        
    def Characters(self):
        self.obj.write(b'n')
        call(['python','/home/pi/std_googleAssistant/GUI/Codes/Characters.py'])

    def Apps(self):
        self.obj.write(b'n')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/AppsRobo.py'])

    def Remind(self):
        self.obj.write(b'n')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/ReminderFRobo.py'])

    def Calculator(self):
        self.obj.write(b'n')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/CalculatorRobo.py'])

    def News(self):
        self.obj.write(b'n')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/NewsRobo.py'])

    def Quran(self):
        self.obj.write(b'n')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/QuranRobo.py'])

    def Music(self):
        self.obj.write(b'n')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/MusicRobo.py'])
        
    def Audiobooks(self):
        self.obj.write(b'n')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/AudioBooksRobo.py'])

    def Exercise(self):
        self.obj.write(b'n')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/ExerciseRobo.py'])

    def Games(self):
        self.obj.write(b'n')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/GamesRobo.py'])

    def Weather(self):
        self.obj.write(b'n')
        webbrowser.open(weather, new=new)

    def TTT(self):
        self.obj.write(b'n')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/tictactoeRobo.py'])

    def Color(self):
        self.obj.write(b'n')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/colorGameRobo.py'])
         
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
