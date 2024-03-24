from tkinter import *
import time

class ReminderText(Frame):
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height) # # 
        self.txt_label = Label(self, text="", font=('Helvetica bold', 23)) #
        print("Text label width:"+str(width))
        print("Text label height:"+str(height))
        self.txt_label.pack()
        self.txt_label.place(anchor='center', relx=0.5, rely=0.5)
    
    def destroyAll(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        time.sleep(0.01)
    
    def restoreDefault(self):
        self.changeText("No reminders")
        
    def changeText(self, text):
        print(text)
        self.txt_label.config(text=text)
        

