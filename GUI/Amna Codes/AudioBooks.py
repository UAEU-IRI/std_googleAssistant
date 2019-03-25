from tkinter import *
import webbrowser

def LittlePrincess():
 webbrowser.open(LP, new=new)

def PeterPan():
 webbrowser.open(PP, new=new)

class GUI:
    def __init__(self, master):
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     #self.button1 = Button(frame, bg="white")
     #self.button1.config(image=photo1)
     #self.button2 = Button(frame,bg="white")
     #self.button2.config(image=photo2)
     self.button1 = Button(frame, text="Peter Pan", bg="white", fg="black", font=("Helvetica", 14), command=PeterPan)
     self.button2 = Button(frame, text="Little Princess", bg="white", fg="black", font=("Helvetica", 14), command=LittlePrincess)
     self.button1.grid(row=0,column=0)
     self.button2.grid(row=0, column=1)

new = 1
PP="http://www.loyalbooks.com/book/peter-pan-by-j-m-barrie"
LP = "http://www.loyalbooks.com/book/a-little-princess-by-frances-hodgson-burnett"
root= Tk()
photo = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Audiobook1.png")
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
b= GUI(root)
root.geometry("1000x920")
root.title("Intelligent Fellow")
root.configure(background='white')
root.mainloop()