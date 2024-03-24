from gpiozero import LED
from time import sleep
# pin 37, GPIO 26 + pin 18, GPIO 24
class ResponseLed(LED):
    def __init__(self, gpio:int):
        super().__init__(gpio)
    
    def turnOn(self):
        self.on()
        
    def turnOff(self):
        self.off()
        
    def flashToOff(self, time_s): # flashes for time_s seconds with 1 flash per second
        for s in range(time_s):
            sleep(0.5)
            self.on()
            sleep(0.5)
            self.off()
            
    def flashToOn(self, time_s): # flashes for time_s seconds with 1 flash per second
        for s in range(time_s):
            sleep(0.5)
            self.off()
            sleep(0.5)
            self.on()