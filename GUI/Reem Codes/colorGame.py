import tkinter
import random
from tkinter import messagebox

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30

def startGame(event):
    if timeleft == 30:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))
        
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    win(timeleft)
        
def win(timeleft):
    if(timeleft==0):
     ans = "Time is up, your score is: " +str(score)
     messagebox.showinfo("Score", ans)
      
root = tkinter.Tk()
root.title("COLOR GAME")
root.geometry("500x250")
instructions = tkinter.Label(root, text="Type in the color of the words, and not the word text!",fg="red",font=('Agency FB', 14))
instructions.pack()
scoreLabel = tkinter.Label(root, text="Press enter to start",font=('Agency FB', 14),fg="red")
scoreLabel.pack()
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Agency FB', 14),fg="red")
timeLabel.pack()
label = tkinter.Label(root, font=('Agency FB', 60))
label.pack()
e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()
