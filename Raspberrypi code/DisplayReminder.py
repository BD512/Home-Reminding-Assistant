from tkinter import *
from PIL import Image, ImageTk

class DisplayReminder(Frame):
    def __init__(self, master):
        super().__init__(master)
        # initialization code which calls the displayImage and displayText functions
        self.width = 800
        self.height = 480
        self.image_label = Label(self)
        # self.image_label.pack()
        self.text_label = Label(self)
        self.text_label.pack()
        
    
    def displayImage(self, image_path:str):
        # displays image at row and column in self
        self.image_label["image"] = ImageTk.PhotoImage(Image.open(image_path).resize((self.width, self.height)))
        self.image_label.pack()
        
    def displayText(self, text:str):
        # displays image at row and column in self
        self.text_label["text"] = text
        
root = Tk()
a = DisplayReminder(root)
a.pack()
a.displayImage("better-groot.jpg")
a.displayText("Hi")
root.mainloop()
        
    