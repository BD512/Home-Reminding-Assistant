

class CheckEditingMode:
    def __init__(self, file="editing.txt"):
        self.editing_file =  file # False if computer not editing records currently
        
    def read(self) -> bool:
        f = open(self.editing_file, "r")
        carer_editing = f.read()
        f.close()
        if carer_editing.lower() == "true":
            return True
        else:
            return False
        