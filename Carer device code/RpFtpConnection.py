from FtpConnection import *
from CsvWriter import *
import os
import datetime

class RpFtpConnection(FtpConnection):
    def __init__(self, client_csv:str="records.csv", rp_csv:str="records.csv"):
        super().__init__()
        self.connected = False
        self.client_csv = client_csv
        self.rp_csv = rp_csv
        self.username = ""

    def connectWithDetails(self, address:str, port:int, user:str, password:str) -> (bool,str):
        c = self.tryConnect(address, port)
        l = self.tryLogin(user, password)
        if c and l:
            self.username = user
            self.connected = True
            self.getToHomeDir()
            return True, "Connected"
        elif not c:
            self.connected = False
            return False, "Unable to connect to specified IP"
        elif not l:
            self.connected = False
            return False, "Unable to login using credentials"
        
    def updateIpDetails(self, ip_address, port_num, user, password) -> (bool, str):
        self.quitConnection()
        s = self.connectWithDetails(ip_address, port_num, user, password)
        self.connected = s[0]
        return s
    
    def updateSelfCsv(self):
        try:
            temporary_csv = "temporary.csv"
            self.copyFileFrom(self.rp_csv, temporary_csv)
            os.remove(self.client_csv)
            os.rename(temporary_csv, self.client_csv)
            return True
        except:
            return False
            
        
    def updateRpCsv(self):
        try:
            print("Updating csv")
            self.updateEditingFile(True)
            self.deleteFile(self.rp_csv)
            self.copyFileTo(self.client_csv, self.rp_csv)
            self.updateEditingFile(False)
            self.updateLastUpdatedTimeFile()
            print("Csv copied")
            return True
        except:
            return False
    
    def updateRpAudioFiles(self, file_names):
        files_on_rp = self.getDirList()
        for f in file_names:
            self_name = f[0]
            rp_name = f[1]
            if rp_name not in files_on_rp:
                print("file being copied")
                self.copyFileTo(self_name, rp_name)
                
    def updateRpImageFiles(self, file_names):
        files_on_rp = self.getDirList()
        for f in file_names:
            self_name = f[0]
            rp_name = f[1]
            if rp_name not in files_on_rp:
                print("file being copied")
                self.copyFileTo(self_name, rp_name)


    def getToHomeDir(self):
        # try:
        # self.goToDir("home\\"+self.username+"\\FTP") ###########################
        self.goToDir("home")
        self.goToDir(self.username)
        self.goToDir("FTP")
        self.goToDir("file")
        directory = "carerdevice" 
        if not (directory in self.getDirList()):
            self.addDirectory(directory)
        # if not (directory in self.currentPath()):
        self.goToDir(directory)
        # elif not (directory in self.getDirList()) and (directory in self.currentPath()):
            # pass
        print(self.getDirList())
        # except:
            # print("Could not got to directory")
            # pass

    def updateEditingFile(self, is_editing:bool):
        editing_file = "editing.txt"
        writer = CsvWriter(editing_file)
        writer.clear()
        if is_editing:
            writer.writeBool(True)
        else:
            writer.writeBool(False)
        print("Copied editing", self.copyFileTo(editing_file, editing_file))
            
    def updateLastUpdatedTimeFile(self):
        last_update_file = "last_updated.txt"
        writer = CsvWriter(last_update_file)
        writer.clear()
        writer.writeString(str(datetime.datetime.now()))
        print("LA sent", self.copyFileTo(last_update_file, last_update_file))
            
    def checkIfConnected(self):
        self.connected = self.isConnected()
        if self.connected:
            return True
        else:
            return False
            
        
        
        
    
    
