from tkinter import *
import datetime

class CustomizeRepeatability(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.initializeRepeatabilityEntry()
        
    def initializeRepeatabilityEntry(self):
        self.val_option = IntVar()
        self.time_val = Spinbox(self, from_=1,to=604800,wrap=True,textvariable=self.val_option,width=2, state="readonly", justify=CENTER)
        self.time_val.grid(column=0, row=0)
        self.time_option = StringVar(self)
        time_options = ["never", "minutes", "hours", "days", "weeks"]
        self.time_option.set(time_options[0])
        time_menu = OptionMenu(self, self.time_option, *time_options)
        time_menu.grid(row =0, column =1)
        
    def listTimeToDatetime(self, repeat_val:list):
        num = repeat_val[0]
        units = repeat_val[1]
        if units == "never":
            return "Not set"
        elif units == "minutes":
            return datetime.timedelta(minutes=num)
        elif units == "hours":
            return datetime.timedelta(hours=num)
        elif units == "days":
            return datetime.timedelta(days=num)
        elif units == "weeks":
            return datetime.timedelta(weeks=num)
        
        
    def readRepeatTimes(self):
        time_value = self.time_val.get()
        time_units = self.time_option.get()
        time = self.listTimeToDatetime([int(time_value), str(time_units)])
        return time
    
    def setVals(self, time_period:datetime.timedelta):
        try:
            seconds = time_period.total_seconds()
            simple_time = [1, "never"]
            if seconds == 0 or seconds == "Not set" or seconds == False:
                pass
            elif seconds%604800 == 0: # 604800s = 1 week
                simple_time = [int(seconds/604800), "weeks"]
            elif seconds%86400 == 0: # 86400s = 1 day
                simple_time = [int(seconds/86400), "days"]
            elif seconds%3600 == 0: # 3600s = hour
                simple_time = [int(seconds/3600), "hours"]
            elif seconds%60 == 0: # 60s in 1 minute
                simple_time = [int(seconds/60), "minutes"]
            self.val_option.set(simple_time[0])
            self.time_option.set(simple_time[1])
        except:
            simple_time = [1, "never"]
            
            
            
        
            
        
