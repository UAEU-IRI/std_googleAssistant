# Source code: https://github.com/Lavakumar999/Python-Tkinter-FrameWork/blob/master/Tic-tac-toe.py
# adjusted design
from tkinter import *
from tkinter import messagebox
from subprocess import call

def Back():
 window.destroy()
 call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Codes/Kuro/GamesKuro.py'])

def clicked1():
    global turn
    if btn1["text"]==" ":
        if turn==1:
            turn =2
            btn1["text"]="X"
        elif turn==2:
            turn=1
            btn1["text"]="O"
        check()

def clicked2():
    global turn
    if btn2["text"]==" ":
        if turn==1:
            turn =2
            btn2["text"]="X"
        elif turn==2:
            turn=1
            btn2["text"]="O"
        check()

def clicked3():
    global turn
    if btn3["text"]==" ":
        if turn==1:
            turn =2
            btn3["text"]="X"
        elif turn==2:
            turn=1
            btn3["text"]="O"
        check()

def clicked4():
    global turn
    if btn4["text"]==" ":
        if turn==1:
            turn =2
            btn4["text"]="X"
        elif turn==2:
            turn=1
            btn4["text"]="O"
        check()

def clicked5():
    global turn
    if btn5["text"]==" ":
        if turn==1:
            turn =2
            btn5["text"]="X"
        elif turn==2:
            turn=1
            btn5["text"]="O"
        check()

def clicked6():
    global turn
    if btn6["text"]==" ":
        if turn==1:
            turn =2
            btn6["text"]="X"
        elif turn==2:
            turn=1
            btn6["text"]="O"
        check()

def clicked7():
    global turn
    if btn7["text"]==" ":
        if turn==1:
            turn =2
            btn7["text"]="X"
        elif turn==2:
            turn=1
            btn7["text"]="O"
        check()

def clicked8():
    global turn
    if btn8["text"]==" ":
        if turn==1:
            turn =2
            btn8["text"]="X"
        elif turn==2:
            turn=1
            btn8["text"]="O"
        check()

def clicked9():
    global turn
    if btn9["text"]==" ":
        if turn==1:
            turn =2
            btn9["text"]="X"
        elif turn==2:
            turn=1
            btn9["text"]="O"
        check()
flag=1

def check():
    global flag
    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]
    flag=flag+1
    if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
        win(btn1["text"])
    if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
        win(btn4["text"])
    if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
        win(btn7["text"])
    if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
        win(btn1["text"])
    if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
        win(btn2["text"])
    if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
        win(btn3["text"])
    if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
        win(btn1["text"])
    if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
        win(btn7["text"])
    if flag ==10:
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Codes/Kuro/AppsKuro.py'])
        window.destroy()

def win(player):
    ans = "Game complete " +player + " wins "
    messagebox.showinfo("Congratulations", ans)
    call(['python', 'C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Codes/Kuro/KuroWin.py'])
    window.destroy()

window=Tk()
window.title("Tic Tac Toe Game Kuro")
window.geometry("1000x920")
lbl=Label(window,text="Player 1: X",font=('Agency FB','15', 'bold'))
lbl.grid(row=3,column=0)
lbl=Label(window,text="Player 2: O",font=('Agency FB','15', 'bold'))
lbl.grid(row=4,column=0)
photo = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/tic-tac-toe1.png")
label = Label(window,image=photo)
label.grid(row=1,column=4)
photoB = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Back.png")
photoE = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Exit.png")
back = Button(window, bg="white", command=Back)
back.config(image=photoB)
quitButton = Button(window, command=window.quit, bg="white")
quitButton.config(image=photoE)
back.grid(row=1,column=0)
quitButton.grid(row=1,column=5)
turn=1
btn1 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Agency FB','25', 'bold'),command=clicked1)
btn1.grid(column=1, row=2)
btn2 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Agency FB','25', 'bold'),command=clicked2)
btn2.grid(column=2, row=2)
btn3 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Agency FB','25', 'bold'),command=clicked3)
btn3.grid(column=3, row=2)
btn4 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Agency FB','25', 'bold'),command=clicked4)
btn4.grid(column=1, row=3)
btn5 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Agency FB','25', 'bold'),command=clicked5)
btn5.grid(column=2, row=3)
btn6 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Agency FB','25', 'bold'),command=clicked6)
btn6.grid(column=3, row=3)
btn7 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Agency FB','25', 'bold'),command=clicked7)
btn7.grid(column=1, row=4)
btn8 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Agency FB','25', 'bold'),command=clicked8)
btn8.grid(column=2, row=4)
btn9 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Agency FB','25', 'bold'),command=clicked9)
btn9.grid(column=3, row=4)
window.mainloop()