from gpiozero import Button
# pin 35, GPIO 19
class ProblemButton(Button):
    def __init__(self, gpio):
        super().__init__(gpio)
        self.pressed = False
    
    def startListen(self):
        self.wait_for_press()
        self.pressed = True
        
    def reset(self):
        self.pressed = False
    