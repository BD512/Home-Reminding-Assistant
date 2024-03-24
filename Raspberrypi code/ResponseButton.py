from gpiozero import Button
from threading import *
# pin 16, GPIO 23 + pin 35, GPIO 19
class ResponseButton(Button):
    def __init__(self, gpio:int):
        super().__init__(gpio)
        self.pressed = False
        listen_thread = Thread(target=self.startListen)
        listen_thread.start()
    
    def startListen(self):
        self.wait_for_press()
        self.pressed = True
        
    def reset(self):
        self.pressed = False
        listen_thread = Thread(target=self.startListen)
        listen_thread.start()
        # self.startListenThread()
    
    def hasBeenPressed(self):
        return self.pressed
        
        
        