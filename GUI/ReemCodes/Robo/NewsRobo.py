from tkinter import *
import webbrowser
from subprocess import call

def Back():
 root.destroy()
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/Robo/AppsRobo.py'])

def openEY():
 webbrowser.open(EY, new=new)

def openB():
 webbrowser.open(B, new=new)

def openGN():
 webbrowser.open(GN, new=new)

class GUI:
    def __init__(self, master):
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     self.button1 = Button(frame, bg="white", fg="black", font=("Helvetica", 14), command=openEY)
     self.button1.config(image=photo1)
     self.button2 = Button(frame, bg="white", fg="black", font=("Helvetica", 14), command=openB)
     self.button2.config(image=photo2)
     self.button3 = Button(frame, bg="white", fg="black", font=("Helvetica", 14), command=openGN)
     self.button3.config(image=photo3)
     self.button1.grid(row=0,column=0)
     self.button2.grid(row=0, column=1)
     self.button3.grid(row=0, column=2)

new = 1
EY="https://www.emaratalyoum.com/"
B = "https://www.albayan.ae/"
GN = "https://globalnews.ca"
root= Tk()
photo = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/News1.png")
label = Label(root,image=photo)
photoB = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Exit.png")
photo1 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/ematatalyoum.png")
photo2 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/AlBayan.png")
photo3 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/GlobalNews.png")
back = Button(root, bg="white", command=Back)
back.config(image=photoB)
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
back.pack(side="left",anchor=NW)
quitButton.pack(side="right", anchor=NE)
label.pack(side="top", anchor=N)
b= GUI(root)
root.geometry("1000x920")
root.title("Intelligent Fellow")
root.configure(background='white')
root.mainloop()
