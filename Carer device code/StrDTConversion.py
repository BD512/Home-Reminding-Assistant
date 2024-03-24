# from datetime import datetime, timedelta
import datetime

class StrDateTimeConversions(str):
    def __init__(self, s:str):
        super().__init__()
        self+=s
        
    def toDTTime(self):
        try:
            return datetime.datetime.strptime(self, '%H:%M:%S')
        except:
            return "Unreadable"
    
    def toDTDate(self):
        try:
        #     print(self)
            # if "/" in self:
            #     return datetime.strptime(self, "%M/%dd/%yyyy")
            # else:
            return datetime.datetime.strptime(self, '%Y-%m-%d') # 
        except:
            return "Unreadable"
    
    def timeStampToDT(self):
        try:
            try:
                return datetime.datetime.strptime(self, '%Y-%m-%d %H:%M:%S.%f')
            except:
                return datetime.datetime.strptime(self, '%Y-%m-%d %H:%M:%S')
        except:
            return "Unreadable"
        
    def secondsToTimeDelta(self):
        try:
            return datetime.timedelta(seconds=float(self))
        except:
            return "Not set"
    
    
    
    