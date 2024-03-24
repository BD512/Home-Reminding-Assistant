from ReminderRecordRpv import *
from RecordsCsvManage import *
from StrDTConversion import *
import os
# works :)

class ReminderRecords(list): # a list class storing and managing the records of reminder events which will be used
    def __init__(self, csv_file="records.csv"): # gives optional initialization of the csv file which will store the records
        super().__init__()
        self.records_csv = RecordsCsvManage(csv_file) # initialzes the csv which will store self
        
    def editRecordResponse(self, record, response): # edits the response for the record from the person cared for
        record.setResponse = response
        
    def deleteRecordByIndex(self, index): # deletes a records of a given index 
        self.pop(index)
        self.updateRecordsCsv()
        
    def deleteRecord(self, r:ReminderRecord): # deletes a records of a given instance of ReminderRecord
        self.remove(r)
        self.updateRecordsCsv()
        
    def getRecordFromId(self, record_id):
        for r in self:
            if r.getSpecificId() == record_id:
                return r
        return False
        
    def updateRecordsCsv(self): # updates the csv file (self.records_csv) with the values of the current ReminderRecords (self)
        self.records_csv.reset()
        for r in self:
            self.records_csv.writeRecord(dt=r.date_time, repeat_time=r.repeat_period, text=r.text, image_path_os=r.image_path_os, image_path_rp=r.image_path_rp, audio_path_os=r.audio_path_os, audio_path_rp=r.audio_path_rp, ring=r.ring, response_status=r.response_status, shown=r.shown, specific_id=r.specific_id)
         
    def clearRecords(self): # deletes all the reminder records
        self.clear()
        
    def toBool(self, val:str): # converts a string to bool 
        if val.upper() == "TRUE":
            return True
        else:
            return False
        
        
    def updateFromCsv(self): # updates the values of self from specified csv (self.records_csv) file
        self.clearRecords()
        print("Reading")
        for r in self.records_csv.getContentsList():
            # try:
            print(r[6])
            self.append(ReminderRecord(date_time=StrDateTimeConversions(r[0]).timeStampToDT(), repeat_period=StrDateTimeConversions(r[1]).secondsToTimeDelta(), text=r[2], image_path_os=r[3], image_path_rp=r[4], audio_path_os=r[5], audio_path_rp=r[6], ring=self.toBool(r[7]), response_status=r[8], shown=self.toBool(r[9]), specific_id=r[10]))            
            print(r[10])
            # except:
            #     pass
            
    def getNextRecord(self) -> ReminderRecord: # gets the next record to be displayed (one with the lowest datetime
        next_record = None
        for r in self:
            current_datetime = r.getDatetime()
            if next_record == None:
                if not r.shown:
                    next_record = r
            elif current_datetime < next_record.getDatetime() and not r.shown:
                next_record = r
        return next_record
        # except:
        #     print("No records")
        #     return None # no datetimes in self - no records available
        
    def compareFilesToNewList(self, new_audio_list, new_images_list):
        for f in self.getAudioPaths():
            if f not in new_audio_list:
                try:
                    os.remove("//home//we-were-groot//FTP//file//carerdevice//"+str(f[0]))
                except:
                    pass
        for f in self.getImagePaths():
            if f not in new_images_list:
                try:
                    os.remove("//home//we-were-groot//FTP//file//carerdevice//"+str(f))
                except:
                    pass
                
    def getAudioPaths(self): # returns a list of all the audio paths (for when sending audio files to raspberry pi)
        paths = []
        for r in self:
            client_path = r.getOsAudioPath()
            rp_path = r.getRpAudioPath()
            if "." in client_path:
                paths.append([client_path, rp_path])
        return paths
    
    def getImagePaths(self): # returns a list of all the image paths (for when sending image files to raspberry pi)
        paths = []
        for r in self:
            client_path = r.getOsImagePath()
            rp_path = r.getRpImagePath()
            if "." in client_path:
                paths.append([client_path, rp_path])
        return paths
    
        
# test code:
# records = ReminderRecords(csv_file="records.csv")
# records.updateFromCsv()
# print(records[0].getDatetime())
# print(records.getNextRecord()) # fill in this function to test it

