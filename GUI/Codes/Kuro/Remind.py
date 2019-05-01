from tkinter import *
from tkinter import font
from datetime import datetime
import time
import json

# path to reminders.txt file
REM_FILE = "C:/Users/Reemy/Downloads/desktop_reminder-master/desktop_reminder-master/reminders.txt"

# list of reminders
reminders = []


class REMINDER():
	def __init__(self, reminder):
		# reminder info tuple
		self.reminder = reminder

		# root (top level element) config
		self.root = Tk()
		self.root.title("Reminder!")
		self.root["bg"] = "White"
		self.position_window()

		# main frame (inside root) config
		self.mainFrame = Frame(self.root, padx=10, pady = 10, bg="White")
		self.mainFrame.pack(side="bottom", fill=BOTH, expand=1)

		# reminder label (inside main frame) config
		text = Label(self.mainFrame, text=self.reminder[0], bg="White",
					 font = font.Font(family="Times", size=12),
					 padx=20, pady=10, wraplength=300)
		text.pack(fill=BOTH, expand=1)

		# button frame (inside main frame) config
		self.buttonRow = Frame(self.mainFrame, padx=10, pady=10, bg="White")
		self.btn1 = Button(self.buttonRow, text="Dismiss", command=self.dismissReminder, bg="White").grid(row=0, column=0)
		self.btn2 = Button(self.buttonRow, text="Postpone", command=self.postponeReminder, bg="White").grid(row=0, column=2)
		self.buttonRow.grid_columnconfigure(1, minsize=10)
		self.buttonRow.pack()

		# call mainloop of Tk object
		self.root.mainloop()
	
	def position_window(self):
		self.root.geometry("1000x920")


	def dismissReminder(self):
		'''
		utitlity function to remove reminder form list
		'''
		self.root.destroy()
		reminders.remove(self.reminder)
		with open(REM_FILE, 'w') as f:
			f.write(json.dumps(reminders))


	def postponeReminder(self):
		'''
		utility function to postpone reminder by 5 minutes
		'''
		self.root.destroy()
		reminders.remove(self.reminder)
		self.reminder[2] += 5
		self.reminder[1] += self.reminder[2]/60
		self.reminder[2] %= 60  
		reminders.append(self.reminder)
		with open(REM_FILE, 'w') as f:
			f.write(json.dumps(reminders))
		
		


def controller():
	'''
	Main function to update reminders list
	and show reminders.
	'''
	while(True):

		# update reminder list
		with open(REM_FILE, 'r') as f:
			updated_reminders = json.loads(f.read())
			for reminder in updated_reminders:
				if reminder not in reminders:
					reminders.append(reminder)

		# current hour and minute
		cur_hrs = datetime.now().hour
		cur_mins = datetime.now().minute

		# find reminders to show
		for reminder in reminders:
			rem_hrs = reminder[1]
			rem_mins = reminder[2]
			if cur_hrs == rem_hrs and cur_mins == rem_mins:
				# show reminder window
				REMINDER(reminder)
		
		# delay of 60 seconds	
		time.sleep(6)


if __name__ == "__main__":
	controller()