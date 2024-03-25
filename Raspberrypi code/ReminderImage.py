# Import Module
from tkinter import *
# from ReminderText import *
from PIL import *
from PIL import Image, ImageTk



class ReminderImage(Frame):
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height)
        self.image_width = width
        self.image_height = height
        self.default_image = "/home/we-were-groot/Documents/PA_rp_2024/Raspberrypi/default.jpg"
        self.image_label = Label(self)
        self.restoreDefault()
        
    def destroyAll(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        time.sleep(0.01)
        
    def changeImage(self, new_image_path):
        # try:
        self.image_label.destroy()
        image = Image.open(new_image_path)
        resize_image = self.resizeImage(image) # image.resize((self.width, self.height))
        self.img = ImageTk.PhotoImage(resize_image)
        self.image_label = Label(self, image=self.img)
        self.image_label.image = self.img
        self.image_label.grid(row=0, column=0)
        self.image_label.place(anchor='center', relx=0.5, rely=0.5)
        # except:
            # print("Unable to display image")
            
    def restoreDefault(self):
        self.changeImage(self.default_image)

    def resizeImage(self, image):
        width, height = image.size
        print(width/self.image_width)
        print(height/self.image_height)
        if width/self.image_width >= height/self.image_height:
            print("Resize height")
            i = image.resize((int(self.image_width), int(self.image_width*(height/width))))
        else:
            print("Resize width")
            i = image.resize((int(self.image_height*(width/height)), int(self.image_height)))
        return i
    
# a = Tk()
# a.resizable(False,False)
# b = ReminderImage(a, 780, 368)
# b.pack()
# c = ReminderText(a, width=780, height=100)
# c.restoreDefault()
# c.pack()
# b.changeImage("eg.PNG")
# a.mainloop()
