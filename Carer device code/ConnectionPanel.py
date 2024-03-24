from tkinter import *
from IpDetailsMain import *
from IpEntryv4 import *


class ConnectionPanel(Frame):
    def __init__(self, master, main_management,
                 connection: IpDetailsMain):  # , update_class:Update, management_buttons:MainManagementButtons
        super().__init__(master, highlightbackground="black", highlightthickness=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.main_management = main_management
        self.font = "Helvetica 10"
        self.connection = connection
        # self.update_class = update_class
        # self.management_buttons = management_buttons
        self.status_widget = ConnectionStatusWidget(self, connected=self.connection.getConnectionStatus(),
                                                    connection_status_str=self.connection.getConnectionStatusString(),
                                                    ip_address=self.connection.getIpAddress(),
                                                    port_num=self.connection.getPortNum(),
                                                    username=self.connection.getUsername(),
                                                    password=self.connection.getPassword(),
                                                    font=self.font)  # add other parameters
        self.status_widget.grid(row=0, column=0, sticky="nsew")
        self.update_connection_button = ConnectButton(self, self.main_management, self.connection, font=self.font)
        self.update_connection_button.grid(row=1, column=0)  # , sticky="nsew"

    def updateInfo(self): # updates the information displayed by this widget
        self.status_widget.updateDetails(connected=self.connection.getConnectionStatus(),
                                         connection_status_str=self.connection.getConnectionStatusString(),
                                         ip_address=self.connection.getIpAddress(),
                                         port_num=self.connection.getPortNum(), username=self.connection.getUsername(),
                                         password=self.connection.getPassword())


class ConnectButton(Frame):
    def __init__(self, master: ConnectionPanel, main_management, ip_instance: IpDetailsMain, font='Helvetica 10'):
        super().__init__(master)
        self.main_management = main_management
        self.master = master
        self.ip_instance: IpDetailsMain = ip_instance  # instance of IpConnectionMain
        self.add_connection = Button(self, text='Change connection', bd='5', command=self.changeConnection)
        self.add_connection.grid(row=0, column=0)
        self.reconnect = Button(self, text='Reconnect', bd='5', command=self.reconnect)
        self.reconnect.grid(row=0, column=1)

    def changeConnection(self): # for changing the connection details
        ip_entry = IpEntryWindow(self.master, self.ip_instance)
        self.master.wait_window(ip_entry)
        self.master.updateInfo()
        self.main_management.updateAllFromRp()
        self.main_management.connectionCheck()

    def reconnect(self): # for trying to reconnect using the same connection details
        self.ip_instance.refreshConnection()
        self.master.updateInfo()
        self.main_management.updateAllFromRp()
        self.main_management.connectionCheck()


class ConnectionStatusWidget(Frame):
    def __init__(self, master: ConnectionPanel, connected: bool = False, connection_status_str: str = "No connection",
                 ip_address: str = "", port_num=0, username="", password="",
                 font='Helvetica 10'):  # could alternatively import a IpConnectionMain instance
        super().__init__(master)  #
        for row in range(5):
            self.rowconfigure(row, weight=1)
        self.columnconfigure(0, weight=1)
        self.title_font = font + " bold"
        self.font = font
        Label(self, text="Status:", font=self.title_font).grid(row=0, column=0, sticky="nsew")
        Label(self, text="IP address:", font=self.title_font).grid(row=1, column=0, sticky="nsew")
        Label(self, text="Port:", font=self.title_font).grid(row=2, column=0, sticky="nsew")
        Label(self, text="Username:", font=self.title_font).grid(row=3, column=0, sticky="nsew")
        Label(self, text="Password:", font=self.title_font).grid(row=4, column=0, sticky="nsew")
        self.status_label = Label(self, text=connection_status_str, font=self.font)
        self.status_label.grid(row=0, column=1, sticky="nsew")
        self.ip_label = Label(self, text=ip_address, font=self.font)
        self.ip_label.grid(row=1, column=1, sticky="nsew")
        self.port_label = Label(self, text=str(port_num), font=self.font)
        self.port_label.grid(row=2, column=1, sticky="nsew")
        self.user_label = Label(self, text=username, font=self.font)
        self.user_label.grid(row=3, column=1, sticky="nsew")
        try:
            self.pwd_label = Label(self, text=(password[0] + "*" * (len(password) - 1)), font=self.font)
        except:
            self.pwd_label = Label(self, text="N/A", font=self.font)
        self.pwd_label.grid(row=4, column=1, sticky="nsew")

    def updateDetails(self, connected: bool, connection_status_str: str, ip_address="", port_num="", username="",
                      password=""): # for upadting the connection details displayed
        self.status_label.config(text=connection_status_str)
        self.ip_label.config(text=ip_address)
        self.port_label.config(text=port_num)
        self.user_label.config(text=username)
        try:
            self.pwd_label.config(text=(password[0] + ("*" * (len(password) - 1))))
        except:
            self.pwd_label.config(text="-")


"""
a = Tk()
b = IpDetailsMain(RpIpTransmission())
c = ConnectionPannel(a, a, b)
c.grid(row=0, column=0)
a.mainloop()
   """
