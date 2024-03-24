from PIL import Image


class ImageManage(Image.Image):
    def __init__(self, filename):
        super().__init__()
        self.open(name=filename)

    def resize(self, width=780, height=290):
        self.resize((width, height), self.ANTIALIAS)


ImageManage('CO2 graph.png').resize()
