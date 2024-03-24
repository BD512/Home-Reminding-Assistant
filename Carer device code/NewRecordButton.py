from ReminderRecords import *
from RecordDataEntryMain import *
from tkinter import *

class NewRecordButton(Frame):
    def __init__(self, master, records:ReminderRecords, update_class):
        super().__init__(master)
        self.records = records
        self.update_class = update_class
        self.add_button = Button(self, text = 'Add new', bd = '5', command=self.addRecord, width=10)
        self.add_button.grid(row=0, column=0, sticky='nesw')
        
    def addRecord(self):
        self.update_class.updateAllFromRp()
        self.update_class.setEditingMode()
        r = self.records.addRecord()
        record_entry = RecordDetailsEntryMain(master=self.master, record=r, records=self.records)
        self.master.wait_window(record_entry)
        self.update_class.turnOffEditingMode()
        self.update_class.updateAllToRp()
        self.update_class.updateAllFromRp()
        
    def disableButton(self):
        self.add_button["state"] = "disabled"
        
    def enableButton(self):
        self.add_button["state"] = "normal"
        
        
            
            
        
    
        
        
        
    
