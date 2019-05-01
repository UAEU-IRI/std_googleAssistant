from tkinter import *
from subprocess import call

def Next():
 root.destroy()
 call(['python', 'Apps.py'])

def Back():
 root.destroy()
 call(['python', 'Home.py'])

class GUI:
    def __init__(self, master):
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     self.label_1 = Label(frame, text="Username:", bg="white", font=("Agency FB", 18))
     self.label_2 = Label(frame, text="Password:", bg="white", font=("Agency FB", 18))
     self.entry_1 = Entry(frame)
     self.entry_2 = Entry(frame)
     self.label_1.grid(row=0, sticky=E)
     self.label_2.grid(row=1, sticky=E)
     self.entry_1.grid(row=0, column=1)
     self.entry_2.grid(row=1, column=1)
     
root= Tk()
photo = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Login.png")
photoB = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Exit.png")
photoN = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Next.png")
back = Button(root, bg="white", command=Back)
back.config(image=photoB)
next = Button(root, bg="white", command= Next)
next.config(image=photoN)
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
back.pack(side="left",anchor=NW)
next.pack(side="bottom", anchor=NE)
quitButton.pack(side="right", anchor=NE)
label = Label(root, image=photo)
label.pack()
b= GUI(root)
root.title("Intelligent Fellow")
root.geometry("1000x920")
root.configure(background='white')
root.mainloop()
