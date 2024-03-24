import csv
import datetime
from CsvWriter import *
# works :)

class RecordsCsvManage(CsvWriter): 
    def __init__(self, csv_file:str):
        super().__init__(csv_file)
        self.csv_file = csv_file
        
    def writeRecord(self, dt:datetime.datetime, repeat_time:datetime.timedelta, text:str="", image_path_os:str="", image_path_rp:str="", audio_path_os:str="", audio_path_rp:str="", ring:bool=True, response_status="Not received", shown=False, specific_id="") -> bool:
        self.writeDatetime(dt)
        self.writeComma()
        try:
            self.writeNumber(float(repeat_time.total_seconds()))
        except:
            self.writeString(repeat_time)
        self.writeComma()
        self.writeString(text)
        self.writeComma()
        self.writeString(image_path_os)
        self.writeComma()
        self.writeString(image_path_rp)
        self.writeComma()
        self.writeString(audio_path_os)
        self.writeComma()
        self.writeString(audio_path_rp)
        self.writeComma()
        self.writeBool(ring)
        self.writeComma()
        self.writeString(response_status)
        self.writeComma()
        self.writeBool(shown)
        self.writeComma()
        self.writeString(specific_id)
        self.writeEndOfLine()
        return True
        # except:
        #     return False
        
    def reset(self): # deletes all values in the CSV file
        f = open(self.csv_file, 'w')
        f.close()
            
    def getContentsList(self) -> list: # gets a list of the contents in the CSV file
        contents = []
        with open(self.csv_file, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                r = ["", "", "", "", "", "", "", "", "", "", "", ""]
                for i in range(0, 11):
                    try:
                        r[i] = row[i]
                    except:
                        pass
                contents.append(r)
        return contents
                
        
    
# a = RecordsCsvManage("records.csv")
# b = [datetime.timedelta(hours=10)]
# a.writeRecord(datetime.datetime.now(), datetime.timedelta(hours=1), "Hi", "//", "//", "No", True)
# print("Done")
# for row in a.getContentsList():
#    a = row[0]
#    print(a)
   # print((datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')))

