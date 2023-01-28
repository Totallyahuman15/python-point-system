class points:
    def __init__(self, tokenAmount: int):
        self.points = tokenAmount

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