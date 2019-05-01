from tkinter import *
import webbrowser

def openweb():
 webbrowser.open(url, new=new)
 
class GUI:
    def __init__(self, master):
     frame = Frame(master)
     frame.pack()
     frame.configure(background='white')
     self.label_1 = Label(frame, text="إلا دار زايد - حسين الجسمي", bg="white", font=("Helvetica", 14))
     self.label_2 = Label(frame, text="الله ثم الوطن ثم رئيس الدولة", bg="white", font=("Helvetica", 14))
     self.label_3 = Label(frame, text="أنا الإماراتي - وديمة أحمد", bg="white", font=("Helvetica", 14))
     self.button1 = Button(frame, bg="white")
     self.button1.config(image=photo1)
     self.button2 = Button(frame, bg="white",command=openweb)
     self.button2.config(image=photo1)
     self.button3 = Button(frame, bg="white")
     self.button3.config(image=photo1)
     self.label_1.grid(row=0, column=0)
     self.label_2.grid(row=1, column=0)
     self.label_3.grid(row=2, column=0)
     self.button1.grid(row=0, column=1)
     self.button2.grid(row=1, column=1)
     self.button3.grid(row=2, column=1)
root= Tk()
new = 1
url = "https://soundcloud.com/user-523895603/allahthmalwatn/s-He2nG"
photo = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Emirati1.png")
photo1 = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Play.png")
photoB = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Exit.png")
back = Button(root, bg="white")
back.config(image=photoB)
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
back.pack(side="left",anchor=NW)
quitButton.pack(side="right", anchor=NE)
label = Label(root, image=photo)
label.pack()
b= GUI(root)
root.title("Intelligent Fellow")
root.geometry("1000x920")
root.configure(background='white')
root.mainloop()