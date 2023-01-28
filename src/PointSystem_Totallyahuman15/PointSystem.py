class points:
    def __init__(self, tokenAmount: int, *,  classifier: str = None, front: bool = False):
        self.str = None
        self.points = tokenAmount
        if classifier == None:
            self.classifier = None
        else:
            if front == True:
                self.classifier = [classifier + ": ", ""]
            else:
                self.classifier = ["", " " + classifier]

    def add(self, add: int):
        self.points = self.points + add

    def sub(self, sub: int):
        self.points = self.points - sub

    def mult(self, mult: int):
        self.points = self.points * mult

    def div(self, div: int):
        self.points = self.points / div

    def set(self, amount: int = None):
        self.points = amount

    def round(self):
        self.points = int(self.points)

    def float(self):
        self.points = float(self.points)

    def reset(self):
        self.points = 0

    def setClassifier(self, classifier: str, front: bool):
        if front == True:
            self.classifier = [classifier + ": ", ""]
        else:
            self.classifier = ["", " " + classifier]

    def show(self):
        if self.classifier == None:
            print(self.points)
        else:
            print(str(self.points).join(self.classifier))

    def getStr(self):
        if self.classifier == None:
            self.str = str(self.points)
        else:
            self.str = str(str(self.points).join(self.classifier))