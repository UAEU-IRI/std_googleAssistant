#might not use it
from tkinter import *

class GUI:
    def __init__(self, master):
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     self.label_1 = Label(frame, text="Chapter 1", bg="white", font=("Helvetica", 14))
     self.label_2 = Label(frame, text="Chapter 2", bg="white", font=("Helvetica", 14))
     self.label_3 = Label(frame, text="Chapter 3", bg="white", font=("Helvetica", 14))
     self.label_4 = Label(frame, text="Chapter 4", bg="white", font=("Helvetica", 14))
     self.label_5 = Label(frame, text="Chapter 5", bg="white", font=("Helvetica", 14))
     self.label_6 = Label(frame, text="Chapter 6", bg="white", font=("Helvetica", 14))
     self.label_7 = Label(frame, text="Chapter 7", bg="white", font=("Helvetica", 14))
     self.label_8 = Label(frame, text="Chapter 8", bg="white", font=("Helvetica", 14))
     self.label_9 = Label(frame, text="Chapter 9", bg="white", font=("Helvetica", 14))
     self.label_10 = Label(frame, text="Chapter 10", bg="white", font=("Helvetica", 14))
     self.label_11 = Label(frame, text="Chapter 11", bg="white", font=("Helvetica", 14))
     self.label_12 = Label(frame, text="Chapter 12", bg="white", font=("Helvetica", 14))
     self.label_13 = Label(frame, text="Chapter 13", bg="white", font=("Helvetica", 14))
     self.label_14 = Label(frame, text="Chapter 14", bg="white", font=("Helvetica", 14))
     self.label_15 = Label(frame, text="Chapter 15", bg="white", font=("Helvetica", 14))
     self.label_16 = Label(frame, text="Chapter 16", bg="white", font=("Helvetica", 14))
     self.label_17 = Label(frame, text="Chapter 17", bg="white", font=("Helvetica", 14))
     self.button1 = Button(frame, bg="white")
     self.button1.config(image=photo1)
     self.button2 = Button(frame, bg="white")
     self.button2.config(image=photo1)
     self.button3 = Button(frame, bg="white")
     self.button3.config(image=photo1)
     self.button4 = Button(frame, bg="white")
     self.button4.config(image=photo1)
     self.button5 = Button(frame, bg="white")
     self.button5.config(image=photo1)
     self.button6 = Button(frame, bg="white")
     self.button6.config(image=photo1)
     self.button7 = Button(frame, bg="white")
     self.button7.config(image=photo1)
     self.button8 = Button(frame, bg="white")
     self.button8.config(image=photo1)
     self.button9 = Button(frame, bg="white")
     self.button9.config(image=photo1)
     self.button10 = Button(frame, bg="white")
     self.button10.config(image=photo1)
     self.button11 = Button(frame, bg="white")
     self.button11.config(image=photo1)
     self.button12 = Button(frame, bg="white")
     self.button12.config(image=photo1)
     self.button13 = Button(frame, bg="white")
     self.button13.config(image=photo1)
     self.button14 = Button(frame, bg="white")
     self.button14.config(image=photo1)
     self.button15 = Button(frame, bg="white")
     self.button15.config(image=photo1)
     self.button16 = Button(frame, bg="white")
     self.button16.config(image=photo1)
     self.button17 = Button(frame, bg="white")
     self.button17.config(image=photo1)
     self.label_1.grid(row=0, column=0)
     self.label_2.grid(row=1, column=0)
     self.label_3.grid(row=2, column=0)
     self.label_4.grid(row=3, column=0)
     self.label_5.grid(row=4, column=0)
     self.label_6.grid(row=0, column=2)
     self.label_7.grid(row=1, column=2)
     self.label_8.grid(row=2, column=2)
     self.label_9.grid(row=3, column=2)
     self.label_10.grid(row=4, column=2)
     self.label_11.grid(row=0, column=4)
     self.label_12.grid(row=1, column=4)
     self.label_13.grid(row=2, column=4)
     self.label_14.grid(row=3, column=4)
     self.label_15.grid(row=4, column=4)
     self.label_16.grid(row=0, column=6)
     self.label_17.grid(row=1, column=6)
     self.button1.grid(row=0, column=1)
     self.button2.grid(row=1, column=1)
     self.button3.grid(row=2, column=1)
     self.button4.grid(row=3, column=1)
     self.button5.grid(row=4, column=1)
     self.button6.grid(row=0, column=3)
     self.button7.grid(row=1, column=3)
     self.button8.grid(row=2, column=3)
     self.button9.grid(row=3, column=3)
     self.button10.grid(row=4, column=3)
     self.button11.grid(row=0, column=5)
     self.button12.grid(row=1, column=5)
     self.button13.grid(row=2, column=5)
     self.button14.grid(row=3, column=5)
     self.button15.grid(row=4, column=5)
     self.button16.grid(row=0, column=7)
     self.button17.grid(row=1, column=7)
        
root= Tk()
#photo = PhotoImage(file="Piano.png")
photo1 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Play.png")
photoB = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Exit.png")
back = Button(root, bg="white")
back.config(image=photoB)
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
back.pack(side="left",anchor=NW)
quitButton.pack(side="right", anchor=NE)
#label = Label(root, image=photo)
#label.pack()
b= GUI(root)
root.title("Intelligent Fellow")
root.geometry("1000x920")
root.configure(background='white')
root.mainloop()
