from tkinter import *
import webbrowser
from subprocess import call

def LittlePrincess():
 webbrowser.open(LP, new=new)
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/Robo/RobotHi.py'])

def PeterPan():
 webbrowser.open(PP, new=new)
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/Robo/RobotHi.py'])
 
def Back():
 root.destroy()
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/Robo/AppsRobo.py'])

class GUI:
    def __init__(self, master):
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     self.button1 = Button(frame, bg="white", command=PeterPan)
     self.button1.config(image=photo1)
     self.button2 = Button(frame,bg="white", command=LittlePrincess)
     self.button2.config(image=photo2)
     self.button1.grid(row=0,column=0)
     self.button2.grid(row=0, column=1)
    
root= Tk()
new = 1
PP="http://www.loyalbooks.com/book/peter-pan-by-j-m-barrie"
LP = "http://www.loyalbooks.com/book/a-little-princess-by-frances-hodgson-burnett"
photo = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Audiobook1.png")
label = Label(root,image=photo)
photoB = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Exit.png")
photo1 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/PeterPan.png")
photo2 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/alittlePrincee.png")
back = Button(root, bg="white", command=Back)
back.config(image=photoB)
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
back.pack(side="left",anchor=NW)
quitButton.pack(side="right", anchor=NE)
label.pack(side="top", anchor=N)
b= GUI(root)
root.geometry("1000x920")
root.title("Intelligent Fellow Robo Audiobooks")
root.configure(background='white')
root.mainloop()
