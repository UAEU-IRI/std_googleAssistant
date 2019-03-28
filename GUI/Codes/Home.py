from tkinter import *
from subprocess import call

def Login():
    root.destroy()
    call(['python', 'Login.py'])

def Register():
    root.destroy()
    call(['python', 'Register.py'])

class GUI1:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        frame.configure(background='white')
        self.button1 = Button(frame, bg="white", command=Login)
        self.button1.config(image=photo1)
        self.button2 = Button(frame, bg="white", command=Register)
        self.button2.config(image=photo2)
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        
root= Tk()
photo = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Home.png")
photo1 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Login1.png")
photo2 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/SignUp1.png")
photoE = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Exit.png")
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
quitButton.pack(side="right", anchor=NE)
label = Label(root, image=photo)
label.pack()
b= GUI1(root)
root.title("Intelligent Fellow")
root.geometry("1000x920")
root.configure(background='white')
root.mainloop()
