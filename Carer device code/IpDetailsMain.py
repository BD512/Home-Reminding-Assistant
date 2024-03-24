from IpCsvManage import *
from RpFtpConnection import *
# Class for IP details
# add mdoule to manage the update of records when IP details changed

class IpDetailsMain:
    def __init__(self, connection_instance:RpFtpConnection, details_file="ip_info.csv"):
        self.ip_address = str()
        self.port_num = int(21)
        self.username = str("anonymous")
        self.password = str("")
        self.connection_status = bool(False)
        self.connection_status_string = "No connection"
        self.connection_instance = connection_instance
        self.csv = IpCsvManage(details_file)
        self.updateIpFromCsv()
        self.updateConnectionInstance()
    
    def getConnectionStatus(self) -> bool: # returns the current connection status to the raspsberry pi. 
        return self.connection_status
    
    def getConnectionStatusString(self) -> str: # returns the current connection status to the raspsberry pi. 
        return self.connection_status_string
    
    def getIpAddress(self) -> str: # returns the IpAddress being used. 
        return self.ip_address
    
    def getPortNum(self) -> int: # returns the port number being used.
        return self.port_num
    
    def getUsername(self) -> str: # returns the username being used. 
        return self.username
    
    def getPassword(self) -> str: # returns the password being used. 
        return self.password
        
    def updateIpFromCsv(self) -> bool: # updates the IP details from the CSV file
        try:
            data = self.csv.getContentsList()
            self.ip_address = data[0]
            self.username = data[2]
            self.password = data[3]
            return True
        except:
            return False
            
    
    def saveToCsv(self) -> None: # saves the Ip details to the CSV file
        self.csv.reset()
        self.csv.writeIpDetails(self.ip_address, self.port_num, self.username, self.password)
    
    def updateConnectionInstance(self): # updates the IP details to the connection instance
        connection = self.connection_instance.updateIpDetails(ip_address=self.ip_address, port_num=self.port_num, user=self.username, password=self.password)
        self.connection_status = connection[0]
        self.connection_status_string = connection[1]
        
    def refreshConnection(self): # updates the connection instance
        self.updateConnectionInstance()
        
    def editVals(self, ip_address, port_num, username, password) -> None: # changes the connection details. 
        self.ip_address = ip_address
        self.port_num = port_num
        self.username = username
        self.password = password
        
    def saveEditedVals(self): # saves the values stored in the class to the CSV and updates the connection instance. 
        self.saveToCsv()
        self.updateConnectionInstance()
        
    def checkConnection(self): # checks whether still connection instance connected and updates the value of this to the connection status. 
        if not self.connection_instance.checkIfConnected():
            self.connection_status_string = "Disconnected"
            self.connection_status = False
            print("Not connected")
            return False
        else:
            self.connection_status_string = "Connected"
            self.connection_status = True
            print("Connected")
            return True
        
    
    