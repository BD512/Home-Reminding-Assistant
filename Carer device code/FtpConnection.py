from ftplib import FTP

class FtpConnection(FTP):
    def __init__(self):
        super().__init__()
        
    def tryConnect(self, host, port=21) -> bool: # tries to connect to the specifies port number at the ip address specified as "host"
        try:
            self.connect(host=host, port=port, timeout=10)
            print("Connectedd")
            return True
        except:
            print("Not connected")
            return False
        
    def tryLogin(self, user="anonymous", password="") -> bool: # tries to login with the username defined as parameter "user" and password defined as parameter "password"
        try:
            self.login(user=user, passwd=password)
            print("Logged in")
            return True
        except:
            print("Not logged in")
            return False
        
    def quitConnection(self) -> bool: # instance cannot be reused after executing this. Quits the connection between client and FtpServer.
        try:
            self.quit()
            return True
        except:
            try:
                self.close()
                return True
            except:
                return False
    
            
    def copyFileTo(self, client_file_path:str, filename:str) -> bool: # filename is the name it will be stored as on the ftp server
        try:
            client_file = open(client_file_path, "rb")
            self.storbinary(f"STOR {filename}", client_file)
            client_file.close()
            return True
        except:
            return False
        
    def copyFileFrom(self, server_file_name, client_file_path): # replaces contents of OS file with contents of read file specified by "server_file_name"
        try:
            client_file = open(client_file_path, "ab")
            self.retrbinary(f"RETR {server_file_name}", client_file.write)
            client_file.close()
            return True
        except:
            return False
        
    def getDirList(self) -> list: # returns a list of the contents of the current directory
        try:
            return self.nlst()
        except:
            return [False]
    
    def renameFile(self, current_name, new_name) -> bool: # renames a specified file on the connected device with the new name
        try:
            self.rename(current_name, new_name)
            return True
        except:
            return False
            
    def deleteFile(self, filename) -> bool: # deletes a specified file on the connected device
        try:
            self.delete(filename)
            return True
        except:
            return False
        
    def deleteDirectory(self, dirname) -> bool: # takes in the directory name of a directory on the connected device then deletes it. 
        try:
            self.rmd(dirname)
            return True
        except:
            return False
        
    def addDirectory(self, new_dirname): # Takes in a directory name and creates this in the current directory on the connected device. 
        try:
            self.mkd(new_dirname)
            return True
        except:
            return False
        
    def goToDir(self, dirname) -> bool: # takes in a directory name and goes to this directory on the connected device.  
        try:
            self.cwd(dirname)
            return True
        except:
            return False
        
    def currentPath(self): # returns the current path name on the connected device.  
        try:
            return self.pwd()
        except:
            return False
        
    def isFileInCurrentPath(self, filename:str) -> bool: #takes in the name of a file and returns true if the file is in the current directory on the connected device and false otherwise.
        if filename in self.getDirList():
            return True
        else:
            return False
        
    def isConnected(self) -> bool: # sends a void command to check whether the connection is still active. 
        try:
            self.voidcmd("NOOP")
            print("Void command received")
            return True
        except:
            return False
    
            
