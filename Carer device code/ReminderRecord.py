import datetime
# from RecordDataEntry import *
import pathlib
import time
# works :)

class ReminderRecord:
    def __init__(self, specific_id, date_time=datetime.datetime.now(),
                 repeat_period=datetime.timedelta(seconds=0), text="", audio_path_os="//", audio_path_rp="//", image_path_os="//", image_path_rp="//", response_status="Not received", ring=True, shown=False): # str(datetime.datetime.now().time())
        self.date_time = date_time
        self.repeat_period = repeat_period # units handled by datetime library (e.g. hours, seconds, weeks ect.)
        self.text = text
        self.audio_path_os = audio_path_os
        self.audio_path_rp = audio_path_rp
        self.image_path_os = image_path_os
        self.image_path_rp = image_path_os
        self.ring:bool = ring
        self.response_status = response_status 
        self.shown = shown
        print(specific_id)
        self.specific_id = specific_id
        self.setRpMediaPaths()
        time.sleep(0.1)
        
        
    def editValues(self, dt:datetime.datetime, repeat_period:datetime.timedelta, text:str, audio_path_os:str, image_path_os:str, ring:bool):
        self.date_time = dt
        self.repeat_period = repeat_period
        self.text = text
        self.audio_path_os = audio_path_os
        self.image_path_os = image_path_os
        self.ring = ring
        self.setRpMediaPaths()
        # print(self.response_status)

        
    def setRpMediaPaths(self) -> None:
        current_time:str = str(datetime.datetime.now())
        if "." in self.audio_path_os and (self.audio_path_rp == "//" or self.audio_path_rp == ""):
            self.audio_path_rp = str(current_time)+(pathlib.Path(self.audio_path_os).suffix)
        if "." in self.image_path_os and (self.image_path_rp == "//" or self.image_path_rp == ""):
            self.image_path_rp = str(current_time)+(pathlib.Path(self.image_path_os).suffix)
            
    def getDate(self) -> datetime.date:
        return self.date_time.time()
    
    def getTime(self) -> datetime.time:
        return self.date_time.time()
    
    def getDatetime(self) -> datetime.datetime:
        return self.date_time
    
    def getRepeatPeriod(self) -> datetime.timedelta:
        return self.repeat_period
    
    def getText(self) -> str:
        return self.text
    
    def getOsAudioPath(self) -> str:
        return self.audio_path_os
    
    def getRpAudioPath(self) -> str:
        return self.audio_path_rp
    
    def getOsImagePath(self) -> str:
        return self.image_path_os
    
    def getRpImagePath(self) -> str:
        return self.image_path_rp
    
    def getResponseStatus(self) -> str:
        return self.response_status
    
    def getRing(self) -> bool:
        return self.ring
    
    def hasBeenShown(self) -> bool:
        return self.shown


        
        