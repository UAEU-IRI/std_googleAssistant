from tkinter import *
from tkinter import ttk
import calendar

class main:
    def __init__(self,master):
        self.master=master
        self.month=IntVar()
        self.year = IntVar()
        self.months = (1,2,3,4,5,6,7,8,9,10,11,12)
        self.widgets()
        
    def getcalc(self):
        m=self.month.get()
        y=self.year.get()
        cal=calendar.month(y,m,2,1)
        self.area.delete(0.0,END)
        self.area.insert(0.0, cal)
    
    def widgets(self):
        Label(self.master,text="Calendar",font=("freesansbold",30),bd=10).pack()
        f=Frame(self.master,padx=10,pady=10)
        Label(f,text="Month: ",font=("freesansbold",13)).grid()
        mon=ttk.Combobox(f,width=7,font=("freesansbold",13),values=self.months,textvariable=self.month)
        mon.grid(row=0,column=1)
        mon.current(0)
        Label(f, text="Year: ", font=("freesansbold", 13)).grid(row=0,column=2)
        ttk.Entry(f, width=7, font=("freesansbold", 13),textvariable=self.year).grid(row=0, column=3)
        f.pack()
        self.area=Text(self.master,font=("",15,"bold"),width=20,height=9,bd=20)
        self.area.pack()
        Button(self.master,command=self.getcalc,text="Get Calendar",font=("",15,"bold"),bd=10).pack()
        
        

if __name__== "__main__":
    root = Tk()
    main(root)
    root.title("Calendar")
    root.mainloop()
    