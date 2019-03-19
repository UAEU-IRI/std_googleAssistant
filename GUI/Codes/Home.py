from tkinter import *

class GUI1:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        frame.configure(background='white')
        self.button1 = Button(frame, text="  Login  ",bg="white", fg="black", font=("Helvetica", 14))
        self.button2 = Button(frame, text="Register",bg="white", fg="red", font=("Helvetica", 14))
        self.button1.pack()
        self.button2.pack()
        self.quitButton = Button(frame, command=frame.quit, bg="white")
        self.quitButton.config(image=photoE)
        self.quitButton.pack()
        
root= Tk()
photo = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Home.png")
photoE = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Exit.png")
label = Label(root, image=photo)
label.pack()
b= GUI1(root)
root.title("Intelligent Fellow")
root.configure(background='white')
root.mainloop()
