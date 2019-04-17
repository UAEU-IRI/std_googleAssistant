from tkinter import *

root= Tk()
photo1 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/GirlMusic.gif")
label = Label(root, image=photo1)
label.pack()
root.title("Intelligent Fellow")
root.geometry("1000x920")
root.configure(background='white')
root.mainloop()