from tkinter import *
from ReminderImage import *
from ReminderText import *
from ReminderImageText import *
import time

class MainGui(Tk):
    def __init__(self, height, width):
        super().__init__()
        # self.attributes('-fullscreen',True)
        self.title("Reminders")
        self.height = height
        self.width = width
        self.main_frame = ReminderImageText(self, width=self.width, height=self.height)
        self.main_frame.grid(row=0)

        
    def setImageText(self, image, text):
        try:
            print("Image-txt gui")
            
            self.main_frame.grid_remove()
            self.main_frame.destroy()
            # self.main_frame.destroy()
            # self.main_frame.destroyAll()
            self.main_frame = ReminderImageText(self, width=self.width, height=self.height)
            # self.main_frame.pack_propagate(False)
            self.main_frame.changeAll(image_path=image, text=text)
            self.main_frame.grid(row=0)
            time.sleep(0.01)
        except:
            self.setOnlyText(text+"[could not show image]")
        
    def setOnlyImage(self, image):
        try:
            
            self.main_frame.grid_remove()
            self.main_frame.destroy()
            self.main_frame = ReminderImage(self, width=self.width, height=self.height)
            # self.main_frame.pack_propagate(False)
            self.main_frame.changeImage(new_image_path=image)
            self.main_frame.grid(row=0)
            time.sleep(0.01)
        except:
            self.setOnlyText("Could not show image [press red button for help]")
        
    def setOnlyText(self, msg):
        print(type(self.main_frame))
        # try:
            # self.main_frame.destroyAll()
        # except:
            # self.main_frame.destroy()
        
        self.main_frame.grid_remove()
        self.main_frame.destroy()
        # time.sleep(0.01)
        print(msg)
        self.main_frame = ReminderText(self, width=self.width, height=self.height)
        # self.main_frame.pack_propagate(False)
        self.main_frame.changeText(msg)
        self.main_frame.grid(row=0)
        
        # self.main_frame.place() # allign='center'
        time.sleep(0.01)
        
    def setRingingMode(self):
        self.setOnlyText("Ringing press any button for reminder")
        
    def setNoAlerts(self):
        print("Width:"+str(self.width))
        self.main_frame.destroy()
        self.main_frame = ReminderImageText(self, width=self.width, height=self.height)
        self.main_frame.grid(row=0)
        # self.main_frame.pack_propagate(False)
        self.main_frame.setDefault()
        time.sleep(0.01)
"""

class MainGui(Tk):
    def __init__(self, height, width):
        super().__init__()
        self.geometry(str(width)+"x"+str(height))
        self.resizable(width=False, height=False)
        self.minsize(height=height, width=width)
        self.maxsize(height=height, width=width)
        self.height = height
        self.width = width
        self.main_frame = ReminderImageText(self, width=self.width, height=self.height)
        self.main_frame.grid(row=0, column=0)
        self.layout_mode = "imagetext"
        
    def setImageText(self, image, text):
        try:
            print("Image-txt gui")
            if self.layout_mode != "imagetext":
                self.main_frame.destroy()
                self.main_frame = ReminderImageText(self, width=self.width, height=self.height)
                self.main_frame.pack()
                self.main_frame.pack_propagate(False)
                self.layout_mode = "imagetext"
            self.main_frame.changeAll(image_path=image, text=text)
        except:
            self.setOnlyText(text+"[could not show image]")
        
    def setOnlyImage(self, image):
        try:
            print("Image gui")
            print("Width:"+str(self.width))
            if self.layout_mode != "image":
                self.main_frame.destroy()
                self.main_frame = ReminderImage(self, width=self.width, height=self.height)
                self.main_frame.pack()
                self.main_frame.pack_propagate(False)
                self.layout_mode = "image"
            self.main_frame.changeImage(new_image_path=image)
        except:
            self.setOnlyText("Could not show image [press red button for help]")
        
    def setOnlyText(self, text):
        print("Width:"+str(self.width))
        if self.layout_mode != "text":
            self.main_frame.destroy()
            self.main_frame = ReminderText(self, width=self.width, height=self.height)
            self.main_frame.pack()
            self.main_frame.pack_propagate(False)
            self.layout_mode = "text"
        self.main_frame.changeText(text)
        
    def setRingingMode(self):
        self.setOnlyText("Ringing press any button for reminder")
        
    def setNoAlerts(self):
        print("Width:"+str(self.width))
        if self.layout_mode != "imagetext":
            self.main_frame.destroy()
            self.main_frame = ReminderImageText(self, width=self.width, height=self.height)
            self.main_frame.pack()
            self.main_frame.pack_propagate(False)
            self.layout_mode = "imagetext"
        self.main_frame.setDefault()
"""
  
# a = MainGui(width=780, height=460)
# a.setImageText(image="eg.PNG", text="hi")
# a.setNoAlterts()
# a.setOnlyText("better-groot.jpg")
# a.mainloop()