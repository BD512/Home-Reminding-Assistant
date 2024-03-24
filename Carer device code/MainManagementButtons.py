from SaveButton import *
from RefreshButton import *
from NewRecordButton import *

class MainManagementButtons(Frame):
    def __init__(self, master, records:ReminderRecords, update_class):
        super().__init__(master)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.refresh_button = RefreshButton(self, update_class)
        self.refresh_button.grid(row=0, column=0, sticky="new", rowspan=3)
        self.save_button = SaveButton(self, update_class)
        self.save_button.grid(row=1, column=0, sticky="nsew", rowspan=3) # 
        self.add_button = NewRecordButton(self, records, update_class)
        self.add_button.grid(row=2, column=0, sticky="new", rowspan=3) # 
        
    def disableAllButtons(self):
        self.refresh_button.disableButton()
        self.save_button.disableButton()
        self.add_button.disableButton()
        
    def enableAllButtons(self):
        self.refresh_button.enableButton()
        self.save_button.enableButton()
        self.add_button.enableButton()
