from tkinter import *
class GUI:
    def __init__(self, master):
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     self.button1 = Button(frame, bg="white")
     self.button1.config(image=photo1)
     self.button2 = Button(frame,bg="white")
     self.button2.config(image=photo2)
     self.button3 = Button(frame,bg="white")
     self.button3.config(image=photo3)
     self.button4 = Button(frame, bg="white")
     self.button4.config(image=photo4)
     self.back = Button(frame, bg="white")
     self.back.config(image=photoB)
     self.quitButton = Button(frame, command=frame.quit, bg="white")
     self.quitButton.config(image=photoE)
     self.label = Label(frame,image=photo)
     self.back.grid(row=0, column=0)
     self.label.grid(row=0, column=1)
     self.quitButton.grid(row=0, column=3)
     self.button1.grid(row=1,column=1)
     self.button2.grid(row=1, column=2)
     self.button3.grid(row=2, column=1)
     self.button4.grid(row=2, column=2)
root= Tk()
photo = PhotoImage(file="Music.png")
photo1 = PhotoImage(file="Piano1.png")
photo2 = PhotoImage(file="Emirati.png")
photo3 = PhotoImage(file="Relaxation.png")
photo4 = PhotoImage(file="English.png")
photoB = PhotoImage(file="Back.png")
photoE = PhotoImage(file="Exit.png")
b= GUI(root)
root.geometry(1000*920)
root.title("Intelligent Fellow")
root.configure(background='white')
root.mainloop()