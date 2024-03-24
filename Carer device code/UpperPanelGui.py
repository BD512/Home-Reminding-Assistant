from tkinter import *
from MainManagementButtons import *
from ConnectionPanel import *


class UpperPanelGui(Frame):
    def __init__(self, master, main_connection_details:IpDetailsMain, records:ReminderRecords):
        super().__init__(master, highlightbackground="black", highlightthickness=1)
        self.master = master
        self.main_connection = main_connection_details
        self.records = records
        self.columnconfigure(0, weight = 1, minsize=210)
        self.columnconfigure(1, weight = 1, minsize=100)
        self.rowconfigure(0, weight = 1)
        self.initializeHeading(row=0, column=0)
        self.main_management_buttons, self.connection_panel = self.initializeWidgets(row=0, column=1)
            
    def initializeHeading(self, row=0, column=0):
        heading = Frame(self)
        heading.columnconfigure(0, weight = 1)
        heading.rowconfigure(0, weight = 1)
        heading.rowconfigure(1, weight = 1)
        Label(heading, text="Caring Assistant", font='Helvetica 16').grid(row=0, column=0, sticky="nsew")
        Label(heading, text="Technology", font='Helvetica 16').grid(row=1, column=0, sticky="nsew")
        heading.grid(row=row, column=column, sticky="w", columnspan=10)
        
    def initializeWidgets(self, row=0, column=1):
        widgets = Frame(self)
        widgets.columnconfigure(0, weight = 1)
        widgets.columnconfigure(1, weight = 1)
        widgets.rowconfigure(0, weight = 1)
        main_management_buttons = MainManagementButtons(widgets, update_class=self.master, records=self.records)
        main_management_buttons.grid(row=0, column=0, sticky="nse", padx=5, pady=5)
        connection_panel = ConnectionPanel(widgets, main_management=self.master, connection=self.main_connection)
        connection_panel.grid(row=0, column=1, sticky="nsw", padx=5, pady=5)
        widgets.grid(row=row, column=column, sticky="nse", columnspan=10)
        return main_management_buttons, connection_panel
        
    def disableAllButtons(self):
        self.main_management_buttons.disableAllButtons()
        
    def enableAllButtons(self):
        self.main_management_buttons.enableAllButtons()
        
    def updateConnectionPanelInfo(self):
        self.connection_panel.updateInfo()