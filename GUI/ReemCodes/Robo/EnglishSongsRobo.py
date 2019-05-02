#might not use it
from tkinter import *
from subprocess import call

def Scars(self, master):
 frame = Frame(master)
 frame.pack()
 frame.configure(background='white')
 call(['aplay', r'C:\Users\Reemy\Documents\GitHub\std_googleAssistant\GUI\Scars.mp3'])

class GUI:
    def __init__(self, master):
     #global object
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     self.label_1 = Label(frame, text="Scars to your beautiful - Alessia Cara", bg="white", font=("Helvetica", 14))
     self.label_2 = Label(frame, text="Scars - Tove Lo", bg="white", font=("Helvetica", 14))
     self.label_3 = Label(frame, text="Hall of fame - The Script", bg="white", font=("Helvetica", 14))
     self.label_4 = Label(frame, text="Unbreakable - Faydee", bg="white", font=("Helvetica", 14))
     self.button1 = Button(frame, bg="white")
     self.button1.config(image=photo1)
     self.button2 = Button(frame, bg="white") #, command=Scars(frame)
     self.button2.config(image=photo1)
     self.button3 = Button(frame, bg="white")
     self.button3.config(image=photo1)
     self.button4 = Button(frame, bg="white")
     self.button4.config(image=photo1)
     self.label_1.grid(row=0, column=0)
     self.label_2.grid(row=1, column=0)
     self.label_3.grid(row=2, column=0)
     self.label_4.grid(row=3, column=0)
     self.button1.grid(row=0, column=1)
     self.button2.grid(row=1, column=1)
     self.button3.grid(row=2, column=1)
     self.button4.grid(row=3, column=1)
     
root= Tk()
#global object
photo = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/English1.png")
photo1 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Play.png")
photoB = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Exit.png")
back = Button(root, bg="white")
back.config(image=photoB)
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
back.pack(side="left",anchor=NW)
quitButton.pack(side="right", anchor=NE)
label = Label(root, image=photo)
label.pack()
b= GUI(root)
#object=GUI(Scars(root,b))
root.title("Intelligent Fellow")
root.geometry("1000x920")
root.configure(background='white')
root.mainloop()
