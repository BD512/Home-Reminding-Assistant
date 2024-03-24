from PIL import ImageTk, Image
from tkinter import *
# https://www.tutorialspoint.com/how-to-resize-an-image-using-tkinter

class DisplayImg(Label):
    def __init__(self, master, img_file_path, width=780, height=290):
        super().__init__(master, width=780, height=290)
        # img = Image.open(img_file_path)
        # img.resize(width=self.width, height=self.height)
        img = ImageTk.PhotoImage(file=img_file_path)
        self.config(image=img)
        
    
# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("700x350")

# Create a canvas widget
canvas = DisplayImg(win, 'CO2 graph.png', width=780, height=290)
canvas.pack()

# Load the image
# img=ImageTk.PhotoImage(file='CO2 graph.png')

# Add the image in the canvas
# canvas.create_image(350, 200, image=img, anchor="center")

win.mainloop()

        