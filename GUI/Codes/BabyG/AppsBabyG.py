from tkinter import *
from subprocess import call
import webbrowser

def News():
    root.destroy()
    call(['python', '/home/pi/std_googleAssistant/GUI/Codes/BabyG/NewsBabyG.py'])

def Calculator():
    root.destroy()
    call(['python', 'CalculatorBabyG.py'])

def Remind():
    root.destroy()
    call(['python', 'ReminderFBabyG.py'])
    call(['python', 'RemindBabyG.py'])

def Quran():
    root.destroy()
    call(['python', 'QuranBabyG.py'])

def Music():
    root.destroy()
    call(['python', 'MusicListBabyG.py'])

def AudioBooks():
    root.destroy()
    call(['python', 'AudioBooksBabyG.py'])

def Exercise():
    root.destroy()
    call(['python', 'ExerciseBabyG.py'])

def Games():
    root.destroy()
    call(['python', 'GamesBabyG.py'])

def Weather():
    webbrowser.open(weather, new=new)

def Back():
    root.destroy()
    call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Characters.py'])

class GUI:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        frame.configure(background='white')
        self.button1 = Button(frame, bg="white", command=Remind)
        self.button1.config(image=photo1)
        self.button2 = Button(frame, bg="white", command=Calculator)
        self.button2.config(image=photo2)
        self.button3 = Button(frame, bg="white", command=News)
        self.button3.config(image=photo3)
        self.button4 = Button(frame, bg="white", command=Quran)
        self.button4.config(image=photo4)
        self.button5 = Button(frame, bg="white", command=Music)
        self.button5.config(image=photo5)
        self.button6 = Button(frame, bg="white", command=AudioBooks)
        self.button6.config(image=photo6)
        self.button7 = Button(frame, bg="white", command=Exercise)
        self.button7.config(image=photo7)
        self.button8 = Button(frame, bg="white", command=Games)
        self.button8.config(image=photo8)
        self.button9 = Button(frame, bg="white", command=Weather)
        self.button9.config(image=photo9)
        self.button1.grid(row=0, column=1)
        self.button2.grid(row=0, column=2)
        self.button3.grid(row=0, column=3)
        self.button4.grid(row=1, column=1)
        self.button5.grid(row=1, column=2)
        self.button6.grid(row=1, column=3)
        self.button7.grid(row=2, column=1)
        self.button8.grid(row=2, column=2)
        self.button9.grid(row=2, column=3)

root = Tk()
new = 1
weather = "https://weather.com/weather/today/l/24.21,55.67?par=google"
photo1 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Reminders.png")
photo2 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/calculator.png")
photo3 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/News.png")
photo4 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Quran.png")
photo5 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Music1.png")
photo6 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Audiobook.png")
photo7 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Exercise.png")
photo8 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Games.png")
photo9 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Weather.png")
photoB = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Exit.png")
back = Button(root, bg="white", command=Back)
back.config(image=photoB)
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
back.pack(side="left", anchor=NW)
quitButton.pack(side="right", anchor=NE)
b = GUI(root)
root.title("Intelligent Fellow BabyG Apps")
root.geometry("1000x920")
root.configure(background='white')
root.mainloop()