from tkinter import *
import threading
import time
from RpFtpConnection import *
from ReminderRecords import ReminderRecords
from ReminderRecord import ReminderRecord
from RecordDataEntryMain import RecordDetailsEntryMain
from RecordValueLabels import DatetimeLabel, TextLabel, RepeatLabel, ImagePathLabel, AudioPathLabel, RingLabel, ResponseLabel

class RecordsDisplay(Canvas):
    def __init__(self, master, records:ReminderRecords, rp_connection=RpFtpConnection):
        super().__init__(master)
        self.master = master
        self.records = records
        self.rp_connection = rp_connection
        self.addHeaders()
        for col in range(9):
            self.columnconfigure(col, weight=1)
        self.data_labels = self.displayData(records=self.records, starting_row=1)
        
        
    def addHeaders(self):
        self.rowconfigure(0, weight=1)
        dt_header = Frame(self, highlightbackground="black", highlightthickness=1)
        Label(dt_header, text="Next date+time", font="bold").grid(row=0, column=0, sticky="nsew")
        dt_header.grid(row=0, column=0, sticky="nsew")
        # Label(self, text="Time", font="bold").grid(row=0, column=1)#
        repeat_header = Frame(self, highlightbackground="black", highlightthickness=1)
        Label(repeat_header, text="Repeat", font="bold").grid(row=0, column=0, sticky="nsew")
        repeat_header.grid(row=0, column=1, sticky="nsew")
        txt_header = Frame(self, highlightbackground="black", highlightthickness=1)
        Label(txt_header, text="Text", font="bold").grid(row=0, column=0, sticky="nsew")
        txt_header.grid(row=0, column=2, sticky="nsew")
        img_header = Frame(self, highlightbackground="black", highlightthickness=1)
        Label(img_header, text="Audio file", font="bold").grid(row=0, column=0, sticky="nsew")
        img_header.grid(row=0, column=3, sticky="nsew")
        audio_header = Frame(self, highlightbackground="black", highlightthickness=1)
        Label(audio_header, text="Image file", font="bold").grid(row=0, column=0, sticky="nsew")
        audio_header.grid(row=0, column=4, sticky="nsew")
        edit_header = Frame(self, highlightbackground="black", highlightthickness=1)
        ring_header = Frame(self, highlightbackground="black", highlightthickness=1)
        Label(ring_header, text="Ring", font="bold").grid(row=0, column=0, sticky="nsew")
        ring_header.grid(row=0, column=5, sticky="nsew")
        Label(edit_header, text="Edit", font="bold").grid(row=0, column=0, sticky="nsew")
        edit_header.grid(row=0, column=6, sticky="nsew")
        delete_header = Frame(self, highlightbackground="black", highlightthickness=1)
        Label(delete_header, text="Delete", font="bold").grid(row=0, column=0, sticky="nsew")
        delete_header.grid(row=0, column=7, sticky="nsew")
        response_header = Frame(self, highlightbackground="black", highlightthickness=1)
        Label(response_header, text="Last response", font="bold").grid(row=0, column=0, sticky="nsew")
        response_header.grid(row=0, column=8, sticky="nsew")

    def displayData(self, records:list, starting_row:int=1) -> list:
        data_labels = []
        for i in range(0, len(records)):
            data_labels.append(self.displayNewRecord(self.records[i], i+starting_row))
        return data_labels
            
    def displayNewRecord(self, record:ReminderRecord, row:int) -> list:
        self.rowconfigure(row, weight=3)
        dt_label = DatetimeLabel(self, record)
        print(type(dt_label))
        dt_label.grid(row=row, column=0, sticky="nsew")
        repeat_label = RepeatLabel(self, record)
        repeat_label.grid(row=row, column=1, sticky="nsew")
        txt_label = TextLabel(self, record)
        txt_label.grid(row=row, column=2, sticky="nsew")
        audio_label = AudioPathLabel(self, record)
        audio_label.grid(row=row, column=3, sticky="nsew")
        img_label = ImagePathLabel(self, record)
        img_label.grid(row=row, column=4, sticky="nsew")
        ring_label = RingLabel(self, record)
        ring_label.grid(row=row, column=5, sticky="nsew")
        edit_button = ReminderEditButton(self, record, self.records, self.rp_connection)
        edit_button.grid(row=row, column=6, sticky="nsew")
        delete_button = ReminderDeleteButton(self, record, self.records, self.rp_connection)
        delete_button.grid(row=row, column=7, sticky="nsew")
        response_label = ResponseLabel(self, record)
        response_label.grid(row=row, column=8, sticky="nsew")
        return [dt_label, repeat_label, txt_label, audio_label, img_label, edit_button, delete_button, response_label, ring_label]
        
    def editRow(self, original_record_labels, record):
        print(type(original_record_labels))
        original_record_labels[0].changeVal(record)
        original_record_labels[1].changeVal(record)
        original_record_labels[2].changeVal(record)
        original_record_labels[3].changeVal(record)
        original_record_labels[4].changeVal(record)
        original_record_labels[5].changeVal(record)
        original_record_labels[6].changeVal(record)
        original_record_labels[7].changeVal(record)
        original_record_labels[8].changeVal(record)
        # return [dt, repeat, txt, audio_path, img_path, ring, edit, delete, response]
    
    def editRecordRows(self, records:list):
        labels = []
        for row in range(len(records)): 
            self.editRow(original_record_labels=self.data_labels[row], record=records[row])
            labels.append(self.data_labels[row])
        return labels
        
    def clearRow(self, record_labels:list):
        for i in record_labels:
            i.destroy()
        
    def clearMultipleRows(self, records_labels:list):
        for row in records_labels:
            self.clearRow(row)
        
    def refreshFields(self):
        new_labels = []
        if len(self.data_labels) < len(self.records):
            if len(self.data_labels) != 0:
                new_labels += self.editRecordRows(self.records[0:len(self.data_labels)])
            new_labels += (self.displayData(self.records[len(self.data_labels):len(self.records)], starting_row=len(self.data_labels)+1))
        elif len(self.data_labels) == len(self.records):
            new_labels += self.editRecordRows(self.records)
        elif len(self.data_labels) > len(self.records):
            new_labels += self.editRecordRows(self.records)
            self.clearMultipleRows(self.data_labels[len(self.records):len(self.data_labels)])
        self.data_labels = new_labels
        
class ReminderEditButton(Frame):
    def __init__(self, master:RecordsDisplay, record:ReminderRecord, records:ReminderRecords, rp_connection:RpFtpConnection):
        super().__init__(master, highlightbackground="black", highlightthickness=1)
        self.master = master
        self.record = record
        self.records = records
        self.rp_connection = rp_connection
        Button(self, text='Edit', bd='5', command=self.editRecord).grid(row=0, column=0, sticky="nsew")
        
    def editRecord(self):
        self.rp_connection.updateEditingFile(True)
        record_entry = RecordDetailsEntryMain(master=self.master, record=self.record, records=self.records)
        self.master.wait_window(record_entry)
        self.records.updateRecordsCsv()
        self.rp_connection.updateRpCsv()
        update_thread = threading.Thread(target=self.updateRp)
        update_thread.start()
        time.sleep(2)
        self.rp_connection.updateEditingFile(False)
        self.master.refreshFields()
        
    def updateRp(self):
        print("Update thread started")
        self.rp_connection.updateRpAudioFiles(file_names=self.records.getAudioPaths())
        self.rp_connection.updateRpImageFiles(file_names=self.records.getImagePaths())
        
    def changeVal(self, record):
        self.record = record
        
class ReminderDeleteButton(Frame):
    def __init__(self, master, record:ReminderRecord, records:ReminderRecords, rp_connection):
        super().__init__(master, highlightbackground="black", highlightthickness=1)
        self.record = record
        self.records = records
        self.rp_connection = rp_connection
        Button(self, text='Delete', bd='5', command=self.deleteRecord).grid(row=0, column=0, sticky="nsew")
        
    def deleteRecord(self):
        self.rp_connection.updateEditingFile(True)
        self.records.deleteRecord(r=self.record)
        self.records.updateRecordsCsv()
        self.rp_connection.updateRpCsv()
        self.rp_connection.updateEditingFile(False)
        self.master.refreshFields()
        
    def changeVal(self, record):
        self.record = record
"""
a = Tk()
r = ReminderRecords()
a.geometry("700x350")
r.updateFromCsv()
h=Scrollbar(a, orient='horizontal')

# r.append(ReminderRecord(text="Hi", repeat_period=datetime.timedelta(hours=1), audio_path_os="Downloads"))
# for p in r:
#     print(p.response_status)#
# print(r[0].ring)
b = RecordsDisplay(a, a, r)
c = Frame(b)
b.config(xscrollcommand=h.set)
h.config(command=b.xview)
b.config(scrollregion=c.bbox())
# Label(b, text="Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii").pack()
h.pack(side=BOTTOM, fill='x')
b.pack()


# def refresh():
#     a.after(6000, refresh)
#     b.refreshFields()
# refresh()
a.mainloop()

a = Tk()
r = ReminderRecords()
a.geometry("700x350")
f = Frame(a)
f.pack(expand = True, fill=BOTH)
canvas = RecordsDisplay(f, a, r)
canvas.config(scrollregion=(0,0,500,500))
vbar = Scrollbar(canvas, orient = VERTICAL)
vbar.pack(side = RIGHT, fill = Y)
vbar.config(command = canvas.yview)
  
canvas.config(width=300,height=300)
canvas.config(yscrollcommand=vbar.set)
canvas.pack(side=LEFT, expand = True, fill = BOTH)
a.mainloop()
"""
