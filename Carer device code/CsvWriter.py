import datetime

class CsvWriter:
    def __init__(self, file_name: str):
        self.file_name = file_name
        data_file = open(file_name, "a") # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        data_file.close()

    def clear(self): # clears the csv file
        data_file = open(self.file_name, "w")
        data_file.close()

    def writeBool(self, b:bool):
        data_file = open(self.file_name, "a")
        data_file.write(str(b).upper())
        data_file.close()

    def writeString(self, s:str, quoted:bool = True):
        data_file = open(self.file_name, "a")
        if quoted:
            data_file.write('\"' + str(s) + '\"')
        else:
            data_file.write(s)
        data_file.close()

    def writeNumber(self, number: int):
        data_file = open(self.file_name, "a")
        data_file.write(str(number))
        data_file.close()

    def writeNumber(self, number: float):
        data_file = open(self.file_name, "a")
        data_file.write(str(number))
        data_file.close()

    def writeComma(self):
        data_file = open(self.file_name, "a")
        data_file.write(",")
        data_file.close()
        
    def writeDatetime(self, time_delta:datetime.timedelta, quoted:bool=True):
        data_file = open(self.file_name, "a")
        if quoted:
            data_file.write('\"' + str(time_delta.total_seconds) + '\"')
        else:
            data_file.write(s)
        data_file.close()
        
    def writeDatetime(self, time:datetime.time, quoted:bool=True):
        data_file = open(self.file_name, "a")
        if quoted:
            data_file.write('\"' + str(time) + '\"')
        else:
            data_file.write(s)
        data_file.close()
        
    def writeDatetime(self, date:datetime.date, quoted:bool=True):
        data_file = open(self.file_name, "a")
        if quoted:
            data_file.write('\"' + str(date) + '\"')
        else:
            data_file.write(s)
        data_file.close()

    def writeEndOfLine(self):
        data_file = open(self.file_name, "a")
        data_file.write('\n')
        data_file.close()

