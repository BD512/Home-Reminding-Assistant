from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import os

class FileUpload(Frame): 
    def __init__(self, master, file_types:list=[("all", "*.*")]):
        super().__init__(master)
        self.file_types = file_types
        self.path = "\\"
        # self.frame = Frame(root)
        self.box_contents = StringVar()
        self.path_entry = Entry(self, state="readonly", textvariable=self.box_contents)
        self.path_entry.grid(column=0, row=0)
        self.upload_button = Button(self, text = 'Find', bd = '5', command = self.findAndSavePath).grid(column=2, row=0)
        
        
    def selectFilePath(self) -> str:
        filetypes = self.file_types
        print(filetypes)
        f = fd.askopenfile(filetypes=filetypes, initialdir=self.path)
        print(self.path)
        if f:
            filepath = os.path.abspath(f.name)
            return filepath
        return ""
    
    def findAndSavePath(self) -> None:
        p = self.selectFilePath()
        if len(p) > 0:
            self.path = p
            # self.path_entry.delete(0, END)
            # self.path_entry.insert(0, str(self.path))
            self.box_contents.set(self.path)
        
    def setPath(self, path:str):
        self.box_contents.set(path)
        self.path = path
        
    def getPath(self) -> str:
        return self.path
    
# a = Tk()
# b = FileUpload(a)
# b.pack()
# a.mainloop()