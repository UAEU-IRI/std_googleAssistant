from tkinter import *
import webbrowser

def openYogaM():
 webbrowser.open(YogaM, new=new)

def openYogaN():
 webbrowser.open(YogaN, new=new)

def openGymN():
 webbrowser.open(GymN, new=new)

def openZum():
 webbrowser.open(Zum, new=new)

class GUI:
    def __init__(self, master):
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     self.button1 = Button(frame, bg="white", command=openGymN)
     self.button1.config(image=photo1)
     self.button2 = Button(frame, bg="white", command=openZum)
     self.button2.config(image=photo2)
     self.button3 = Button(frame, bg="white", command=openGymN)
     self.button3.config(image=photo3)
     self.button4 = Button(frame, bg="white", command=openYogaN)
     self.button4.config(image=photo4)
     self.button1.grid(row=0,column=0)
     self.button2.grid(row=0, column=1)
     self.button3.grid(row=1, column=0)
     self.button4.grid(row=1, column=1)
root= Tk()
new=1
GymN = "https://www.youtube.com/playlist?list=PL4tPnorvk5lD6EhgiR4QyQ9QGVe0_nEgY"
Zum = "https://www.youtube.com/watch?v=wvVHA8JKlRk&list=PL-vzR3I8cyKQQH1D8xK4eK_Uv29LCQ7Fs"
YogaM = "https://www.youtube.com/playlist?list=PLtoPgTTLNMmPtARo33xTzLGkWgNxLZUe-"
YogaN = "https://www.youtube.com/playlist?list=PLtoPgTTLNMmNYNLzTFHwY5la68_Vtlfd6"
photo = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Exercise1.png")
label = Label(root,image=photo)
photoB = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Exit.png")
back = Button(root, bg="white")
back.config(image=photoB)
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
back.pack(side="left",anchor=NW)
quitButton.pack(side="right", anchor=NE)
label.pack(side="top", anchor=N)
photo1 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/GymNadz.png")
photo2 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Zumba.png")
photo3 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/morningYoga.png")
photo4 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/NightYoga.png")
b= GUI(root)
root.geometry("1000x920")
root.title("Intelligent Fellow")
root.configure(background='white')
root.mainloop()