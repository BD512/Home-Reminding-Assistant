from tkinter import *
from OnOffOption import *
from tkcalendar import DateEntry
# from tkinter import filedialog as fd
from FileUpload import *
from RepeatWidget import *
from SelectTime import *
import datetime
from ReminderRecord import *
# works :)

class RecordDetailsEntry(Frame):
    def __init__(self, master, record, font='Helvetica 12'):
        super().__init__(master)
        self.record = record
        self.font = font
        self.dateScheduleEntry(0)
        self.timeEntry(1)
        self.repeatTimeEntry(2)
        self.textReminderEntry(3)
        self.selectAudioFilePath(4)
        self.selectImageFilePath(5)
        self.ringToneOption(6)
    
        
    def dateScheduleEntry(self, row:int, row_min:int=0, col_min:int=0) -> None: # initializes the entry for entering the date. 
        self.columnconfigure(row, weight=1, minsize=row_min)
        self.rowconfigure(row, weight=1, minsize=col_min)
        Label(self, text="Date to of reminder:", font=self.font).grid(column=0, row=row)
        self.date_entry = DateEntry(self)
        try:
            self.date_entry.set_date(self.record.getDatetime())
        except:
            pass
        self.date_entry.grid(column=1, row=row)
        
    def readDate(self) -> datetime.date: # reads and returns the date from the date entry.
        # print(self.date_entry.get_date())
        try:
            return self.date_entry.get_date()
        except:
            return None
    
    def timeEntry(self, row:int, row_min:int=0, col_min:int=0) -> None: # initializes the entry widget for entering the date.
        self.columnconfigure(row, weight=1, minsize=col_min)
        self.rowconfigure(row, weight=1, minsize=row_min)
        Label(self, text="Time to of reminder:", font=self.font).grid(column=0, row=row)
        self.time_entry = SelectTime(self)
        try:
            current_record_time = self.record.getTime()
            self.time_entry.setSbVals(current_record_time) 
        except:
            pass
        self.time_entry.grid(column=1, row=row)
        
    def readTime(self) -> datetime.time: # reads and returns the date from the time entry. 
        try:
            return self.time_entry.getTime()
        except:
            return None

    def repeatTimeEntry(self, row:int, row_min:int=0, col_min:int=0) -> None: # initializes repeat entry
        self.columnconfigure(row, weight=1, minsize=col_min)
        self.rowconfigure(row, weight=1, minsize=row_min)
        Label(self, text="Repeat every:", font=self.font).grid(column=0, row=row)
        self.repeat_entry = CustomizeRepeatability(self)
        print(self.record.getRepeatPeriod)
        self.repeat_entry.setVals(self.record.getRepeatPeriod())
        self.repeat_entry.grid(row=row, column=1)
        
    def readRepeat(self) -> datetime.timedelta: # reads repeat period for reminders from repeat entry
        try:
            return self.repeat_entry.readRepeatTimes()
        except:
            return None
   
    def textReminderEntry(self, row:int, row_min:int=0, col_min:int=0) -> None: # initializes entry for text for reminder
        self.columnconfigure(row, weight=1, minsize=col_min)
        self.rowconfigure(row, weight=1, minsize=row_min)
        Label(self, text="Text of reminder:", font=self.font).grid(column=0, row=row)
        self.text_entry = Entry(self)
        self.text_entry.insert(0, self.record.getText())
        self.text_entry.grid(row=row, column=1)
        
    def readText(self) -> str: # reads and returns text from text entry
        try:
            return self.text_entry.get()
        except:
            return None
    
    def selectAudioFilePath(self, row:int, row_min:int=0, col_min:int=0) -> None: # initializes the entry widget for uploading the file audio file path. 
        self.columnconfigure(row, weight=1, minsize=col_min)
        self.rowconfigure(row, weight=1, minsize=row_min)
        Label(self, text="Audio file path:", font=self.font).grid(column=0, row=row)
        self.audio_entry = FileUpload(self, [('WAV', '*.wav'), ('MP3', '*.mp3')])
        self.audio_entry.setPath(self.record.getOsAudioPath())
        self.audio_entry.grid(row=row, column=1)
        
    def readAudioPath(self) -> str: # reads and returns the path from the audio path entry
        try:
            return self.audio_entry.getPath()
        except:
            return None
        

    def selectImageFilePath(self, row:int, row_min:int=0, col_min:int=0) -> None: # initializes the entry widget for uploading the file image file path.
        self.columnconfigure(row, weight=1, minsize=col_min)
        self.rowconfigure(row, weight=1, minsize=row_min)
        Label(self, text="Image file path:", font=self.font).grid(column=0, row=row)
        self.image_entry = FileUpload(self, [('JPEG', '*.jpg'), ('PNG', '*.png')])
        self.image_entry.setPath(self.record.getOsImagePath())
        self.image_entry.grid(row=row, column=1)

    def readImagePath(self) -> str: # reads the value from the image path entry.
        try:
            return self.image_entry.getPath()
        except:
            return None
    
    def ringToneOption(self, row:int, row_min:int=0, col_min:int=0) -> None: # initializes the ring tone option widget. 
        self.columnconfigure(row, weight=1, minsize=col_min)
        self.rowconfigure(row, weight=1, minsize=row_min)
        Label(self, text="Ringtone before reminder:", font=self.font).grid(column=0, row=row)
        self.ring_tone_option = OnOffOption(self)
        self.ring_tone_option.setVals(self.record.getRing())
        self.ring_tone_option.grid(row=row, column=1)
        
    def readRingToneOption(self) -> bool: # reads and returns value from ring tone option widget.
        try:
            return self.ring_tone_option.get()
        except:
            return False
    
    

        


    
    
    
        
    