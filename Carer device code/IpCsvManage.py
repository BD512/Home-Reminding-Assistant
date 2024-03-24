import csv
from CsvWriter import *

class IpCsvManage(CsvWriter): 
    def __init__(self, csv_file:str):
        super().__init__(csv_file)
        self.csv_file = csv_file
        
    def writeIpDetails(self, ip_address:str, port_num:int, username:str, password:str): # Takes in the parameters ip_address (string), port_num (integer), username (string) and password (string) and writes them to the CSV file.  
        self.writeString(ip_address)
        self.writeComma()
        self.writeNumber(port_num)
        self.writeComma()
        self.writeString(username)
        self.writeComma()
        self.writeString(password)
        self.writeEndOfLine()
            
    def reset(self): # clears the CSV file contents
        f = open(self.csv_file, 'w')
        f.close()
            
    def getContentsList(self) -> list: # returns a list of the CSV file contents
        try:
            contents = []
            with open(self.csv_file, 'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    contents += row
            return contents
        except:
            return []
        
    
                
                