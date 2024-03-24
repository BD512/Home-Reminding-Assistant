from tkinter import *
import datetime
# works :)


class SelectTime(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.hours = IntVar()
        self.mins = IntVar()
        hours_text = Label(self, text="Hours",font=("Times", 12))
        hours_text.grid(column=0, row=0)
        minutes_text = Label(self, text="Minutes",font=("Times", 12))
        minutes_text.grid(column=1, row=0)
        self.hour_sb = Spinbox(self, from_=0,to=23,wrap=True,textvariable=self.hours,width=2,state="readonly",justify=CENTER)
        self.hour_sb.grid(column=0, row=1)
        self.min_sb = Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.mins,width=2,state="readonly", justify=CENTER)
        self.min_sb.grid(column=1, row=1)

    def getTime(self):
        hours = int(self.hour_sb.get())
        minutes = int(self.min_sb.get())
        return datetime.time(hour=hours, minute=minutes)
    
    def setSbVals(self, time:datetime.time):
        hours = int(time.strftime("%H"))
        minutes = int(time.strftime("%M"))
        self.hours.set(hours)
        self.mins.set(minutes)

# a = Tk()
# b = SelectTime(a)
# b.setSbVals(10, 1)
# b.pack()
# a.mainloop()