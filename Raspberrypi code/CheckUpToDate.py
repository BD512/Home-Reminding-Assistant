from datetime import *
from StrDTConversion import *

class CheckUpToDate:
    def __init__(self, file="last_updated.txt"):
        self.last_updated_instance = "-"
        self.last_updated_csv = "--"
        self.file = file
    
    def readLastUpdated(self):
        try:
            f = open(self.file, "r")
            self.last_updated_csv = f.read()
            f.close()
        except:
            pass
            
    def isUpToDate(self):
        self.readLastUpdated()
        if self.last_updated_instance == self.last_updated_csv:
            return True
        else:
            return False
        
    def updated(self): # called to reference that the records have been updated
        self.readLastUpdated()
        self.last_updated_instance = self.last_updated_csv