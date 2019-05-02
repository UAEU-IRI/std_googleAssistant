from tkinter import *
from tkinter import font
from datetime import datetime
import time
import json

REM_FILE = "remindersRobo.txt"
reminders = []

class REMINDER():
	def __init__(self, reminder):
		# reminder info tuple
		self.reminder = reminder
		self.root = Tk()
		self.root.title("Reminder!")
		self.root["bg"] = "White"
		self.position_window()
		self.mainFrame = Frame(self.root, padx=10, pady = 10, bg="White")
		self.mainFrame.pack(side="bottom", fill=BOTH, expand=1)
		text = Label(self.mainFrame, text=self.reminder[0], bg="White",
					 font = font.Font(family="Times", size=12),
					 padx=20, pady=10, wraplength=300)
		text.pack(fill=BOTH, expand=1)
		self.buttonRow = Frame(self.mainFrame, padx=10, pady=10, bg="White")
		self.btn1 = Button(self.buttonRow, text="Dismiss", command=self.dismissReminder, bg="White").grid(row=0, column=0)
		self.buttonRow.grid_columnconfigure(1, minsize=10)
		self.buttonRow.pack()
		self.root.mainloop()
	
	def position_window(self):
		self.root.geometry("500x350")


	def dismissReminder(self):
		self.root.destroy()
		reminders.remove(self.reminder)
		with open(REM_FILE, 'w') as f:
			f.write(json.dumps(reminders))

def controller():
	while(True):
		with open(REM_FILE, 'r') as f:
			updated_reminders = json.loads(f.read())
			for reminder in updated_reminders:
				if reminder not in reminders:
					reminders.append(reminder)
		cur_hrs = datetime.now().hour
		cur_mins = datetime.now().minute
		for reminder in reminders:
			rem_hrs = reminder[1]
			rem_mins = reminder[2]
			if cur_hrs == rem_hrs and cur_mins == rem_mins:
				REMINDER(reminder)
		time.sleep(6)

if __name__ == "__main__":
	controller()