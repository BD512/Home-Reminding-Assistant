class CsvReader:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def getLength(self) -> int: # returns the number of rows in the csv file (including headers if any)
        rows = 0
        with open(self.file_name, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows += 1
        return rows
    
    def getContentsList(self) -> list:
        contents = []
        with open(self.file_name, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                contents += [row]
        return contents