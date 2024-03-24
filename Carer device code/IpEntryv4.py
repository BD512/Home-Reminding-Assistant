from tkinter import *
from Validation import *
from IpDetailsMain import *
import time
# works but neaten up!!

class IpEntry(Frame):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text="IP address:", font='Helvetica 14', padx=5, pady=5).grid(column=0, row=2)
        self.ip_entry = Entry(self)
        self.ip_entry.grid(column=2, row=2)
        Label(self, text="Username (optional):", font='Helvetica 14', padx=5, pady=5).grid(column=0, row=3)
        self.name_entry = Entry(self)
        self.name_entry.grid(column=2, row=3)
        Label(self, text="Password (optional):", font='Helvetica 14', padx=5, pady=5).grid(column=0, row=4)
        self.password_entry = Entry(self)
        self.password_entry.grid(column=2, row=4)
        Label(self, text="Port number (optional):", font='Helvetica 14', padx=5, pady=5).grid(column=0, row=5)
        self.port_entry = Entry(self)
        self.port_entry.grid(column=2, row=5)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        
    def close(self): # destroys the frame
        self.destroy()
        
    def readIp(self) -> str: # reads and returns the IP address the IP address entry box.  
        return self.ip_entry.get()
    
    def readUserName(self) -> str: # reads and returns the username from the username entry box. 
        user = self.name_entry.get()
        if user == "":
            return "anonymous"
        else:
            return self.name_entry.get()
    
    def readPassword(self) -> str: # reads and returns password from password entry box
        return self.password_entry.get()
    
    def readPortNumber(self) -> str: # returns port number value but returns 21 if no port number entered
        val = self.port_entry.get()
        if not (len(val) == 0):
            return val
        else:
            return "21"
    
    def readAllValues(self):
        return [self.readIp(), self.readUserName(), self.readPassword(), self.readPortNumber()]
    
    
class IpEntryWindow(Toplevel):
    def __init__(self, main_window, ip_details:IpDetailsMain):
        super().__init__(main_window)
        self.ip_entry = IpEntry(self)
        self.ip_entry.grid(row=0, column=0)
        self.ip_details_instance = ip_details
        self.invalid_label = Label(self, font='Helvetica 14', fg="red")
        self.invalid_label.grid(row=1, column=0)
        self.enter_button = Button(self, text='Enter', bd='5', command=self.trySaveIpDetails)
        self.enter_button.grid(column=1, row=0)
        self.title("IP detials for connection")
        self.ip_address = str()
        self.port_number = int()
        self.username = str()
        self.password = str()
        self.saved = False
        self.grab_set()
        
    def isSaved(self):
        if self.saved:
            return True
        else:
            return False
        
    def readIpDetails(self) -> list:
        return self.ip_entry.readAllValues()
    
    def getIp(self) -> str:
        try:
            return self.ip_address
        except:
            return None
    
    def getPort(self) -> int:
        try:
            return self.port_number
        except:
            return None
    
    def getUserName(self) -> str:
        try:
            return self.username
        except:
            return None
        
    
    def getPassword(self) -> str:
        try:
            return self.password
        except:
            return None
        
        
    def trySaveIpDetails(self) -> None:
        ip_details = self.readIpDetails()
        address = ip_details[0]
        user = ip_details[1]
        password = ip_details[2]
        port = ip_details[3]
        if not Validation().validIp(address):
            self.showInvalidLabel("IP address")
        elif not Validation().validPort(port):
            self.showInvalidLabel("Port number")
        else:
            self.ip_address = address
            self.port_number = int(port)
            self.username = user
            self.password = password
            self.saved = True
            self.ip_details_instance.editVals(self.ip_address, self.port_number, self.username, self.password)
            self.ip_details_instance.saveEditedVals()
            time.sleep(2)
            self.destroy()
        
            
    def showInvalidLabel(self, invalid_parameter) -> None:
        self.invalid_label.config(text=(invalid_parameter+" invalid."))
        
# c = Tk()
# d = IpDetailsMain()
# a = IpEntryWindow(c, d)
# c.wait_window(a)
# d.saveEditedVals()
# c.mainloop()

# print(d.connection_status_string)
# print(a.getIp())
# print(a.getPort())
# print(a.getUserName())
# print(a.getPassword())