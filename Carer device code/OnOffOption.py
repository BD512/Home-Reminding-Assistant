from tkinter import *
# works :)

class OnOffOption(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.val = IntVar()
        self.on = Radiobutton(self, text="On", variable=self.val, value=1)
        self.on.grid(row=0, column=0) # pack( anchor = W )
        self.off = Radiobutton(self, text="Off", variable=self.val, value=2)
        self.off.grid(row=0, column=1) # pack(anchor = W)
        self.on.deselect()
        self.off.deselect()
        
    def get(self) -> bool:
        if self.val.get() == 1:
            return True
        elif self.val.get() == 2:
            return False
        else:
            return True
        
    def setVals(self, val:bool):
        if val:
            self.on.select()
        else:
            self.off.select()
            
        
