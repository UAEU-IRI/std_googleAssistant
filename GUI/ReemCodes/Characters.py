from tkinter import *
from subprocess import call

def Back():
 root.destroy()
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/LogoGif.py'])
 
def Kuro():
 root.destroy()
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/Kuro/AppsKuro.py'])

def Robo():
 root.destroy()
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/Robo/AppsRobo.py'])
 
def Baby():
 root.destroy()
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/ReemCodes/BabyG/AppsBabyG.py'])

class GUI:
    def __init__(self, master):
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     self.button1 = Button(frame, bg="white", command=Robo)
     self.button1.config(image=photo1)
     self.button2 = Button(frame,bg="white", command=Kuro)
     self.button2.config(image=photo2)
     self.button3 = Button(frame,bg="white",command=Baby)
     self.button3.config(image=photo3)
     #self.button4 = Button(frame, bg="white")
     #self.button4.config(image=photo4)
     self.button1.grid(row=0,column=0)
     self.button2.grid(row=0, column=1)
     self.button3.grid(row=0, column=2)
     #self.button4.grid(row=0, column=3)

root= Tk()
#photo = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Home.png")
#label = Label(root,image=photo)
label_1 = Label(root, text="Choose Your Fellow", bg="white", font=("Agency FB", 25))
label_1.pack(anchor=N)
photoB = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Exit.png")
back = Button(root, bg="white", command=Back)
back.config(image=photoB)
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
back.pack(side="left",anchor=NW)
quitButton.pack(side="right", anchor=NE)
photo1 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Robo.png")
photo2 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Kuro.png")
photo3 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/BabyG.png")
#photo4 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Johnny.png")
b= GUI(root)
root.geometry("1000x920")
root.title("Intelligent Fellow")
root.configure(background='white')
root.mainloop()