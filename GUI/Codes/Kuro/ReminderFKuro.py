from tkinter import *
import json
from subprocess import call

REM_FILE = "/home/pi/std_googleAssistant/GUI/Codes/Kuro/remindersKuro.txt"

def Back():
    root.destroy()
    call(['python', '/home/pi/std_googleAssistant/GUI/Codes/Kuro/AppsKuro.py'])

root = Tk()
root.title("Intelligent Fellow Kuro Reminder")
photo = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Reminders1.png")
photoB = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/Exit.png")
back = Button(root, bg="white", command=Back)
back.config(image=photoB)
quitButton = Button(root, command=root.quit, bg="white")
quitButton.config(image=photoE)
back.pack(side="left", anchor=NW)
quitButton.pack(side="right", anchor=NE)
label = Label(root, image=photo)
label.pack()

class REMINDER():
    def __init__(self):
        self.position_window()
        self.mainFrame = Frame(root, padx=10, pady=10)
        self.mainFrame.pack()
        self.fieldRow1 = Frame(self.mainFrame, padx=5, pady=5)
        Label(self.fieldRow1, text="Remind me about:").grid(row=0, column=0)
        self.rem = Entry(self.fieldRow1)
        self.rem.grid(row=0, column=1)
        self.fieldRow1.pack()
        self.fieldRow2 = Frame(self.mainFrame, padx=5, pady=5)
        Label(self.fieldRow2, text="Remind me at:", width=15).grid(row=0, column=0)
        self.hrs = Entry(self.fieldRow2, width=5)
        self.hrs.grid(row=0, column=1)
        Label(self.fieldRow2, text=":").grid(row=0, column=2)
        self.mins = Entry(self.fieldRow2, width=5)
        self.mins.grid(row=0, column=3)
        self.clk = StringVar()
        self.clk.set('AM')
        OptionMenu(self.fieldRow2, self.clk, 'AM', 'PM').grid(row=0, column=4)
        self.fieldRow2.pack()
        self.buttonRow = Frame(self.mainFrame, padx=10, pady=10)
        self.btn1 = Button(self.buttonRow, text="Save", command=self.saveReminder).grid(row=0, column=0)
        self.btn2 = Button(self.buttonRow, text="Cancel", command=self.cancelReminder).grid(row=0, column=2)
        self.buttonRow.grid_columnconfigure(1, minsize=10)
        self.buttonRow.pack()
        root.mainloop()
    
    def position_window(self):
        root.geometry("1000x920")
    
    def saveReminder(self):
        reminder = self.rem.get().strip()
        hrs = int(self.hrs.get().strip())
        mins = int(self.mins.get().strip())
        clk = self.clk.get()
        if clk == 'PM':
            hrs += 12
        with open(REM_FILE, 'r+') as f:
            reminders = json.loads(f.read())
            f.seek(0)
            reminders.append((reminder, hrs, mins))
            f.write(json.dumps(reminders))
            f.truncate()
        root.destroy()
    
    def cancelReminder(self):
        root.destroy()

if __name__ == "__main__":
    REMINDER()