from ReminderRecords import *
from tkinter import *


class SaveButton(Frame):
    def __init__(self, master, update_class):
        super().__init__(master)
        self.update_class = update_class
        self.save_button = Button(self, text='Save', bd='5', command=self.save, width=10)
        self.save_button.grid(row=0, column=0, sticky='nesw')
        
    def save(self):
        self.update_class.updateAllToRp()
        
    def disableButton(self):
        self.save_button["state"] = "disabled"
        
    def enableButton(self):
        self.save_button["state"] = "normal"
