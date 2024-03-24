from ReminderImage import *
from ReminderText import *
from tkinter import *
import time

class ReminderImageText(Frame):
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height, highlightbackground="black", highlightthickness=1)
        self.image_width = width
        self.image_height = height*0.7
        self.text_width = width
        self.text_height = height*0.3
        self.image_frame = ReminderImage(self, width=self.image_width, height=self.image_height)
        self.image_frame.grid(row=0, column=0)
        self.text_frame = ReminderText(self, width=self.text_width, height=self.text_height)
        self.text_frame.grid(row=1, column=0)
        self.setDefault()
        
    def setDefault(self):
        self.image_frame.restoreDefault()
        self.text_frame.restoreDefault()
    
    def changeImage(self, new_image_path):
        self.image_frame.changeImage(new_image_path)
        
    def changeText(self, new_text):
        self.text_frame.changeText(new_text)
        
    def changeAll(self, image_path, text):
        self.changeImage(image_path)
        self.changeText(text)
    
        
# a = Tk()
# b = ReminderImageText(a, 800, 480)
# b.pack()
# a.mainloop()
        