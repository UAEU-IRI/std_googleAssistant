from tkinter import *
import webbrowser
from subprocess import call

def Back():
 root.destroy()
 call(['python', 'Apps.py'])

def openMRA():
 webbrowser.open(MRA, new=new)

def openAA():
 webbrowser.open(AA, new=new)

def openAAlN():
  webbrowser.open(AAlN, new=new)

def openHAB():
 webbrowser.open(HAB, new=new)

class GUI:
    def __init__(self, master):
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     self.button1 = Button(frame, bg="white",command=openMRA)
     self.button1.config(image=photo1)
     self.button2 = Button(frame, bg="white",command=openAA)
     self.button2.config(image=photo2)
     self.button3 = Button(frame, bg="white", command=openAAlN)
     self.button3.config(image=photo3)
     self.button4 = Button(frame, bg="white",command=openHAB)
     self.button4.config(image=photo4)
     self.button1.grid(row=0, column=0)
     self.button2.grid(row=1, column=0)
     self.button3.grid(row=0, column=1)
     self.button4.grid(row=1, column=1)

root= Tk()
new = 1
MRA = "https://soundcloud.com/hussein-abdelkawy/sets/shmnbresddeo"
AA="https://soundcloud.com/telawatcloud/sets/abdulbasithafs"
AAlN = "https://soundcloud.com/shahd-abd-el-aziz/sets/q0cyrjk0xsiw"
HAB = "https://soundcloud.com/ahmed-bob-731271110/sets/68gixqmstfdu"
photo1 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Alafasy.png")
photo2 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Minsha.png")
photo3 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Alnufais.png")
photo4 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/hazzaalbalushi.png")
photo = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Quran1.png")
photoB = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Exit.png")
back = Button(root, bg="white", command=Back)
back.config(image=photoB)
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
back.pack(side="left",anchor=NW)
quitButton.pack(side="right", anchor=NE)
label = Label(root, image=photo)
label.pack()
b= GUI(root)
root.title("Intelligent Fellow")
root.geometry("1000x920")
root.configure(background='white')
root.mainloop()