from tkinter import *
from RecordDataEntryv2 import *
from ReminderRecord import *
from ReminderRecords import *

# works :)

class RecordDetailsEntryMain(Toplevel): 
    def __init__(self, master, record:ReminderRecord, records:ReminderRecords, font='Helvetica 12'):
        super().__init__(master)
        self.font = font
        self.record = record
        self.records = records
        self.entry = RecordDetailsEntry(master=self, record=self.record, font=self.font)
        self.entry.grid(row=0, column=0)
        Button(self, text="Enter", command=self.saveRecord).grid(row=1, column=0)
        self.title("Reminder setup")
        self.grab_set()
        
    def saveRecord(self):
        self.records.editRecord(self.record, dt=datetime.datetime.combine(self.entry.readDate(), self.entry.readTime()), repeat_period=self.entry.readRepeat(), text=self.entry.readText(), audio_path_os=self.entry.readAudioPath(), image_path_os=self.entry.readImagePath(), ring=self.entry.readRingToneOption())
        self.destroy()
        

# r = ReminderRecord(text="Hi", repeat_period=datetime.timedelta(hours=1), audio_path_os="Downloads")
# records = ReminderRecords()
# records.append(r)
# b = Tk()
# a = ReminderDetailsEntryMain(r, records)

# print(r.get())
# a.pa()
# a.mainloop()
# print(r.date_time)