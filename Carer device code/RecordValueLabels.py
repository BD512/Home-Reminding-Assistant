from tkinter import *
from ReminderRecord import ReminderRecord

class DatetimeLabel(Frame):
    def __init__(self, master, record):
        super().__init__(master, highlightbackground="black", highlightthickness=1)
        self.record = record
        self.val = Label(self, text=str(self.record.getDatetime()))
        self.val.grid(row=0, column=0, sticky="nsew")
        
    def changeVal(self, record):
        self.record = record
        self.val.config(text=str(self.record.getDatetime()))
        
class TextLabel(Frame):
    def __init__(self, master, record):
        super().__init__(master, highlightbackground="black", highlightthickness=1)
        self.record = record
        self.val = Label(self, text=str(self.record.getText()))
        self.val.grid(row=0, column=0, sticky="nsew")
        
    def changeVal(self, record):
        self.record = record
        self.val.config(text=str(self.record.getText()))
        
class RepeatLabel(Frame):
    def __init__(self, master, record):
        super().__init__(master, highlightbackground="black", highlightthickness=1)
        self.record = record
        self.val = Label(self, text=str(self.record.getRepeatPeriod()))
        self.val.grid(row=0, column=0, sticky="nsew")
        
    def changeVal(self, record):
        self.record = record
        self.val.config(text=str(self.record.getRepeatPeriod()))
        
class ImagePathLabel(Frame):
    def __init__(self, master, record):
        super().__init__(master, highlightbackground="black", highlightthickness=1, width=10)
        self.record = record
        self.val = Label(self, text=str(self.record.getOsImagePath()))
        self.val.grid(row=0, column=0, sticky="nsew")
        
    def changeVal(self, record):
        self.record = record
        self.val.config(text=str(self.record.getOsImagePath()))
        

class AudioPathLabel(Frame):
    def __init__(self, master, record):
        super().__init__(master, highlightbackground="black", highlightthickness=1, width=10)
        self.record = record
        self.val = Label(self, text=str(self.record.getOsAudioPath()))
        self.val.grid(row=0, column=0, sticky="nsew")
        
    def changeVal(self, record):
        self.record = record
        self.val.config(text=str(self.record.getOsAudioPath()))
        
class RingLabel(Frame):
    def __init__(self, master, record):
        super().__init__(master, highlightbackground="black", highlightthickness=1)
        self.record = record
        ring = self.record.getRing()
        if ring:
            self.val = Label(self, text="On")
        else:
            self.val = Label(self, text="Off")
        self.val.grid(row=0, column=0, sticky="nsew")
        
    def changeVal(self, record):
        self.record = record
        ring = self.record.getRing()
        if ring:
            self.val.config(text="On")
        else:
            self.val.config(text="Off")
            

class ResponseLabel(Frame):
    def __init__(self, master, record):
        super().__init__(master, highlightbackground="black", highlightthickness=1)
        self.record = record
        self.val = Label(self, text=str(self.record.getResponseStatus()))
        self.val.grid(row=0, column=0, sticky="nsew")
        
    def changeVal(self, record):
        self.record = record
        self.val.config(text=str(self.record.getResponseStatus()))

        
        