from tkinter import *
import webbrowser
from subprocess import call

def Back():
 root.destroy()
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/Robo/AppsRobo.py'])

def openPiano():
 webbrowser.open(P, new=new)
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/Robo/RoboSleep.py'])

def openArabicSongs():
 webbrowser.open(AS, new=new)
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/Robo/RoboMusic.py'])

def openRelaxation():
 webbrowser.open(R, new=new)
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/Robo/RoboSleep.py'])

def openEnglishSongs():
 webbrowser.open(ES, new=new)
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/Robo/RoboMusic.py'])

class GUI:
    def __init__(self, master):
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     self.button1 = Button(frame, bg="white", command=openPiano)
     self.button1.config(image=photo1)
     self.button2 = Button(frame,bg="white", command=openArabicSongs)
     self.button2.config(image=photo2)
     self.button3 = Button(frame,bg="white", command=openRelaxation)
     self.button3.config(image=photo3)
     self.button4 = Button(frame, bg="white", command=openEnglishSongs)
     self.button4.config(image=photo4)
     self.button1.grid(row=2,column=0)
     self.button2.grid(row=2, column=1)
     self.button3.grid(row=2, column=2)
     self.button4.grid(row=2, column=3)
     
root= Tk()
new = 1
P = "https://soundcloud.com/user-523895603/sets/piano/s-gS99x"
AS = "https://soundcloud.com/user-523895603/sets/arabic-songs/s-zrNLZ"
R = "https://soundcloud.com/user-523895603/sets/nature/s-fTUVx"
ES = "https://soundcloud.com/user-523895603/sets/english-songs/s-VLtCf"
photo = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Music.png")
label = Label(root,image=photo)
photoB = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Exit.png")
back = Button(root, bg="white", command=Back)
back.config(image=photoB)
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
back.pack(side="left",anchor=NW)
quitButton.pack(side="right", anchor=NE)
label.pack(side="top", anchor=N)
photo1 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Piano1.png")
photo2 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Emirati.png")
photo3 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Relaxation.png")
photo4 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/English.png")
b= GUI(root)
root.geometry("1000x920")
root.title("Intelligent Fellow Robo Music")
root.configure(background='white')
root.mainloop()
