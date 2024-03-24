from RecordDisplay import *
from ReminderRecords import *
from RpFtpConnection import *
from IpDetailsMain import *
from tkinter import *
from UpperPanelGui import *
import time

class Main(Tk): # the main gui for the carer
    def __init__(self):
        super().__init__()
        self.title("Carer assisstant technology")
        self.resizable(True, True)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.records = ReminderRecords(csv_file="records.csv")
        self.rp_connection = RpFtpConnection(client_csv="records.csv", rp_csv="records.csv")
        self.main_ip_manage = IpDetailsMain(connection_instance=self.rp_connection, details_file="ip_info.csv")
        self.records_table = self.initializeRecordDisplay(row=1, column=0)
        self.upper_panel = self.initializeUpperPannel(row=0, column=0)
        self.updateAllFromRp()
        self.connectionCheck()

    def initializeRecordDisplay(self, row=1, column=0): # initializes the display of the reminder records
        records_table = RecordsDisplay(self, records=self.records, rp_connection=self.rp_connection)
        records_table.grid(row=row, column=column, sticky="nsew", columnspan=15, rowspan=1)
        return records_table
    
    def initializeUpperPannel(self, row=0, column=0): # initializes the display of the upper pannel with contains management buttons such as refresh, save and add new record as well as the connection status pannel to the client's CAT device
        upper_panel = UpperPanelGui(master=self, main_connection_details=self.main_ip_manage, records=self.records)
        upper_panel.grid(row=row, column=column, sticky="nsew", columnspan=15, rowspan=1)
        return upper_panel
        
    def enableDisconnectedMode(self): # disables buttons and sets mode to disconnected to raspberry pi
        print("Disconnect mode being enabled")
        self.upper_panel.disableAllButtons()
        self.upper_panel.updateConnectionPanelInfo()
        
    def disableDisconnectedMode(self): # enables buttons and sets mode to connected to raspberry pi
        print("Disconnected mode being disabled")
        self.upper_panel.enableAllButtons()
        self.upper_panel.updateConnectionPanelInfo()
        
    def updateAllFromRp(self): # updates the info on the computer being run on (carer computer) from the client raspberry pi so that the records can be updated
        self.rp_connection.updateSelfCsv()
        self.records.updateFromCsv()
        self.records_table.refreshFields()
        
    def updateAllToRp(self): # saves all the reminder records currently in use to the raspberry pi
        print("Updating files - look into audio files/ image file upload")
        self.records.updateRecordsCsv()
        self.rp_connection.updateRpCsv()
        self.rp_connection.updateRpAudioFiles(file_names=self.records.getAudioPaths())
        self.rp_connection.updateRpImageFiles(file_names=self.records.getImagePaths())
        self.records_table.refreshFields()
        # time.sleep(0.5)

    def setEditingMode(self): # sets editing to true in a text file indicating that the raspberry pi should not write to the csv file until this is false
        print("Editing mode enabled")
        self.rp_connection.updateEditingFile(True)

    def turnOffEditingMode(self):# sets editing to text false in a file indicating that the raspberry pi can write to the csv file. 
        print("Editing mode disabled")
        self.rp_connection.updateEditingFile(False)
        
    def connectionCheck(self): # checks and manages the connection status
        if self.main_ip_manage.checkConnection():
            print("Connection checked - connected")
            self.disableDisconnectedMode()
        else:
            print("Connection checked - disconnected")
            self.enableDisconnectedMode()
    
a = Main()
a.mainloop()
