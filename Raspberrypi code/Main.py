from ResponseButton import *
from ResponseLed import *
from MainGui import *
from Audio import *
from CheckUpToDate import *
from CheckEditingMode import *
from ReminderRecordsRpv import *
from datetime import *
import time# , threading
# make audio files play + text show when ringing
class Main:
    def __init__(self):
        self.root_folder = "//home//we-were-groot//FTP//file//carerdevice//"
        self.records = ReminderRecords(csv_file=self.root_folder+"records.csv")
        self.up_to_date = CheckUpToDate(file=self.root_folder+"last_updated.txt")
        self.carer_editing = CheckEditingMode(file=self.root_folder+"editing.txt")
        self.current_reminder = None
        self.current_reminder_start = None
        self.next_reminder = None
        self.gui = MainGui(width=800, height=480)
        self.check_button = ResponseButton(23)
        self.help_button = ResponseButton(19)
        self.check_led = ResponseLed(24)
        self.check_led.turnOn()
        self.help_led = ResponseLed(26)
        self.help_led.turnOn()
        self.updateRecordsFromCsv()
        self.mainRun(first_run=True)
        # run.start()
        self.gui.mainloop()
        #self.gui.after(1000, self.mainRun)
        
    def mainRun(self, first_run=False):
        # print("Reading")
        if not first_run:
            if not self.current_reminder == None:
                if self.check_button.hasBeenPressed():
                    self.respondAndComplete("Completed")
                    self.check_button.reset()
                elif self.help_button.hasBeenPressed():
                    self.respondAndComplete("Needs help")
                    self.help_button.reset()
                elif self.current_reminder_start+timedelta(minutes=30)<datetime.now():
                    self.respondAndComplete("Didn't respond after 30 minutes")
            else:
                if not self.up_to_date.isUpToDate():
                    self.updateRecordsFromCsv()
                    self.next_reminder = self.records.getNextRecord()
                if self.next_reminder == None:
                    self.next_reminder = self.records.getNextRecord()
                elif self.next_reminder.getDatetime() <= datetime.now():
                    self.startNextReminder()
        self.gui.after(1000, self.mainRun)
                    
    def startNextReminder(self):
        self.current_reminder = self.next_reminder
        self.current_reminder_start = datetime.now()
        self.gui.setOnlyText("-")
        if self.current_reminder.getRing():#
            self.check_button.reset()
            self.help_button.reset()
            self.ring()
            self.check_button.reset()
            self.help_button.reset()
        if "." in self.current_reminder.getRpImagePath() and self.current_reminder.getText() != "":
            print("Setting imagetext reminder")
            self.gui.setImageText(self.root_folder+self.current_reminder.getRpImagePath(), self.current_reminder.getText())
        elif "." in self.current_reminder.getRpImagePath():
            print("Setting image reminder")
            self.gui.setOnlyImage(self.root_folder+self.current_reminder.getRpImagePath())
        else:
            print("Setting text reminder")
            print(self.current_reminder.getText())
            self.gui.setOnlyText(self.current_reminder.getText())
        print(self.current_reminder.getRpAudioPath())
        if self.current_reminder.getRpAudioPath() != "" and self.current_reminder.getRpAudioPath() != "//":
            sound = Audio(self.root_folder+self.current_reminder.getRpAudioPath())
            sound.playSound()
            
                    
    def updateRecordsFromCsv(self): # delete any files no longer present
        new_records = ReminderRecords(csv_file="records.csv")
        new_records.updateFromCsv()
        new_records_audio = new_records.getAudioPaths()
        new_records_images = new_records.getImagePaths()
        self.records.compareFilesToNewList(new_records_audio, new_records_images)
        self.records.updateFromCsv()
        self.up_to_date.updated()
                
        
    def respondAndComplete(self, response):
        self.gui.setNoAlerts()
        record = self.current_reminder
        self.completeReminder(response, record) # maybe add to different thread
        self.current_reminder = None
        self.current_reminder_start = None
        self.next_reminder = None
        
    def completeReminder(self, response, record):
        done = False 
        record_id = record.getSpecificId()
        while not done:
            if not self.carer_editing.read(): # cannot edit CSV file while carer is editing it
                #   print("Reading record true")
                self.updateRecordsFromCsv()
                try:
                    record = self.records.getRecordFromId(record_id)
                    record.changeResponse(response)
                    if record.getRepeatPeriod() == "Not set" or record.getRepeatPeriod() == timedelta(seconds=0):
                        record.shown = True
                    else:
                        record.date_time = record.getDatetime()+record.getRepeatPeriod()
                    self.records.updateRecordsCsv()
                except:
                    print("Record no longer exists")
                done = True
        
    def ring(self):
        # self.gui.setOnlyText("Ringing, press any button to continue")
        start_time = datetime.now()
        sound = Audio("/home/we-were-groot/Documents/PA_rp_2024/Raspberrypi/ring.wav")
        while not self.check_button.hasBeenPressed() and not self.help_button.hasBeenPressed() and not (datetime.now()>start_time+timedelta(minutes=5)):
            if not sound.isPlaying():
                sound.playSound()
        sound.stopSound()
        self.check_button.reset()
        time.sleep(0.5)
        
            
Main()