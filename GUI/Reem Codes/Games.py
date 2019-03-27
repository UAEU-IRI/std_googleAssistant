from tkinter import *
from subprocess import call

def Color():
 call(['python', 'colorGame.py'])

def TicTacToe():
 call(['python', 'tictactoe.py'])

def Back():
 call(['python', 'Apps.py'])

class GUI:
    def __init__(self, master):
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     self.button1 = Button(frame, bg="white", command=TicTacToe)
     self.button1.config(image=photo1)
     self.button2 = Button(frame,bg="white", command=Color)
     self.button2.config(image=photo2)
     self.button1.grid(row=0,column=0)
     self.button2.grid(row=0, column=1)
     
root= Tk()
photo = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Games1.png")
label = Label(root,image=photo)
photoB = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Exit.png")
photo1 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/tic-tac-toe.png")
photo2 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Color.png")
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