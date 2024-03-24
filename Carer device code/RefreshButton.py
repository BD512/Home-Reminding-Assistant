from tkinter import *

class RefreshButton(Frame):
    def __init__(self, master, update_class):
        super().__init__(master)
        self.update_class = update_class
        self.refresh_button = Button(self, text = 'Refresh', bd = '5', command=self.refresh, width=10)
        self.refresh_button.grid(row=0, column=0, sticky='nesw')
        
    def refresh(self):
        self.update_class.updateAllFromRp()
    
    def disableButton(self):
        self.refresh_button["state"] = "disabled"
        
    def enableButton(self):
        self.refresh_button["state"] = "normal"
    
        
    
        
    
        
