import RPi.GPIO as GPIO
import serial
from time import sleep
from subprocess import call
from tkinter import*
import webbrowser

new = 1
P = "https://soundcloud.com/user-523895603/sets/piano/s-gS99x"
AS = "https://soundcloud.com/user-523895603/sets/arabic-songs/s-zrNLZ"
R = "https://soundcloud.com/user-523895603/sets/nature/s-fTUVx"
ES = "https://soundcloud.com/user-523895603/sets/english-songs/s-VLtCf"
weather = "https://weather.com/weather/today/l/24.21,55.67?par=google"
EY="https://www.emaratalyoum.com/"
B = "https://www.albayan.ae/"
GN = "https://globalnews.ca"
PP="http://www.loyalbooks.com/book/peter-pan-by-j-m-barrie"
LP = "http://www.loyalbooks.com/book/a-little-princess-by-frances-hodgson-burnett"
MRA = "https://soundcloud.com/hussein-abdelkawy/sets/shmnbresddeo"
AA="https://soundcloud.com/telawatcloud/sets/abdulbasithafs"
AAlN = "https://soundcloud.com/shahd-abd-el-aziz/sets/q0cyrjk0xsiw"
HAB = "https://soundcloud.com/ahmed-bob-731271110/sets/68gixqmstfdu"
GymN = "https://www.youtube.com/playlist?list=PL4tPnorvk5lD6EhgiR4QyQ9QGVe0_nEgY"
Zum = "https://www.youtube.com/watch?v=wvVHA8JKlRk&list=PL-vzR3I8cyKQQH1D8xK4eK_Uv29LCQ7Fs"
YogaM = "https://www.youtube.com/playlist?list=PLtoPgTTLNMmPtARo33xTzLGkWgNxLZUe-"
YogaN = "https://www.youtube.com/playlist?list=PLtoPgTTLNMmNYNLzTFHwY5la68_Vtlfd6"

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
        temp=self.obj.read().decode()
        if (temp == str('e')):
                    call (['espeak', 'Love'])
                    self.obj.write (b'a')
        if (temp == str('v')):
                    call (['espeak', 'Victory'])
                    self.obj.write (b'v')
        if (temp == str('i')):
                    call (['espeak', 'Win']) 
                    self.obj.write (b'd')

    def countingFingers(self):
        self.obj.write(b'c')
        call (['espeak', 'I have 5 fingers'])
        
    def On(self):
        self.obj.write(b'q') 
        while (self.obj.inWaiting()<1):
            pass
        temp=self.obj.read().decode()
        if (temp == str('q')):
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
        call (['aplay', '/home/pi/std_googleAssistant/scripts/Voice/Intro.wav'])
        while (self.obj.inWaiting()<1):
            pass
        temp=self.obj.read().decode()
        if (temp == str('w')):
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/Voice/win.wav'])
                    sleep(1)
                    call (['espeak', 'win'])
                    sleep(1)
                    call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/RoboWin.py'])
        elif (temp == str('l')):
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/Voice/lose.wav'])
                    sleep(1)
                    call (['espeak', 'Lose'])
                    sleep(1)
                    call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/RoboLost.py'])
        elif (temp == str('t')):
                    call (['espeak', 'oh we did the same move, let us play again'])
                    self.obj.write (b'p')

    def Memory(self):
        self.obj.write(b's')
        while (self.obj.inWaiting()<1):
            pass
        temp=self.obj.read().decode()
        if (temp == str('a')):       
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/Voice/win.wav'])
                    sleep(1)
                    call (['espeak', 'win'])
        elif (temp == str('b')):
                    call (['aplay', '/home/pi/std_googleAssistant/scripts/Voice/lose.wav'])
                    sleep(1)
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
        self.obj.write(b'h')
        call(['python','/home/pi/std_googleAssistant/GUI/Codes/LogoGif.py'])
        
    def Characters(self):
        self.obj.write(b'h')
        call(['python','/home/pi/std_googleAssistant/GUI/Codes/Characters.py'])

    def Apps(self):
        self.obj.write(b'h')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/AppsRobo.py'])

    def Remind(self):
        self.obj.write(b'h')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/ReminderFRobo.py'])
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/RemindRobo.py'])

    def Calculator(self):
        self.obj.write(b'h')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/CalculatorRobo.py'])

    def News(self):
        self.obj.write(b'c')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/NewsRobo.py'])

    def Quran(self):
        self.obj.write(b'h')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/QuranRobo.py'])

    def Music(self):
        self.obj.write(b'h')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/MusicListRobo.py'])
        
    def Audiobooks(self):
        self.obj.write(b'h')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/AudioBooksRobo.py'])

    def Exercise(self):
        self.obj.write(b'h')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/ExerciseRobo.py'])

    def Games(self):
        self.obj.write(b'c')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/GamesRobo.py'])

    def Weather(self):
        self.obj.write(b'h')
        webbrowser.open(weather, new=new)

    def TTT(self):
        self.obj.write(b'c')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/tictactoeRobo.py'])

    def Color(self):
        self.obj.write(b'c')
        call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Robo/colorGameRobo.py'])
        
    def ArabicS(self):
        self.obj.write(b'c')
        webbrowser.open(AS, new=new)

    def EnglishS(self):
        self.obj.write(b'h')
        webbrowser.open(ES, new=new)

    def Piano(self):
        self.obj.write(b'c')
        webbrowser.open(P, new=new)

    def Relax(self):
        self.obj.write(b'c')
        webbrowser.open(R, new=new)
        
    def EmiratY(self):
        self.obj.write(b'c')
        webbrowser.open(EY, new=new)

    def Bayan(self):
        self.obj.write(b'h')
        webbrowser.open(B, new=new)

    def GN(self):
        self.obj.write(b'c')
        webbrowser.open(GN, new=new)

    def PP(self):
        self.obj.write(b'c')
        webbrowser.open(PP, new=new)
        
    def LP(self):
        self.obj.write(b'c')
        webbrowser.open(LP, new=new)

    def GymNadz(self):
        self.obj.write(b'h')
        webbrowser.open(GymN, new=new)

    def Zumba(self):
        self.obj.write(b'c')
        webbrowser.open(Zum, new=new)

    def MYoga(self):
        self.obj.write(b'c')
        webbrowser.open(YogaM, new=new)

    def NYoga(self):
        self.obj.write(b'c')
        webbrowser.open(YogaN, new=new)

    def Alafasy(self):
        self.obj.write(b'h')
        webbrowser.open(MRA, new=new)

    def Alminshawy(self):
        self.obj.write(b'c')
        webbrowser.open(AA, new=new)

    def Ahmed(self):
        self.obj.write(b'c')
        webbrowser.open(AAlN, new=new)

    def Hazza(self):
        self.obj.write(b'c')
        webbrowser.open(HAB, new=new)
         
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
