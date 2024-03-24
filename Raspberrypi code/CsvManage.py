import csv
import datetime
from CsvWriter import *

class CsvManage(CsvWriter): 
    def __init__(self, csv_file:str):
        super().__init__(csv_file)
        self.csv_file = csv_file
        
    def writeRecord(self, date:datetime.date, time:datetime.time, repeat_time:datetime.timedelta, text:str="", image_path:str="", audio_path:str="") -> bool:
        self.writeDatetime(date)
        self.writeEndOfLine()
        self.writeDatetime(time)
        self.writeEndOfLine()
        self.writeDatetime(repeat_time)
        self.writeEndOfLine()
        self.writeString(text)
        self.writeEndOfLine()
        self.writeString(image_path)
        self.writeEndOfLine()
        self.writeString(audio_path)
        self.writeEndOfLine()
            
    def reset(self):
        f = open(self.csv_file, 'w')
        f.close()
            
    def getContentsList(self) -> list:
        try:
            contents = []
            with open(self.csv_file, 'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    contents += [row]
            return contents
        except:
            return []
        
        
        
    
    
# a = CsvManage("Hi.csv")
# b = [datetime.timedelta(hours=10)]
# a.writeDataRow(b)
# for row in a.getContentsList():
#    a = row[0]
#    print(type(a))
#    # print((datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')))

