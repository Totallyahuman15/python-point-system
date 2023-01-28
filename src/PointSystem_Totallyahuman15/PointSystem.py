class points:
    def __init__(self, tokenAmount: int):
        self.points = tokenAmount

    def add(self, add: int):
        self.points = self.add = self.points + add

    def sub(self, sub: int):
        self.points = self.sub = self.points - sub

    def mult(self, mult: int):
        self.points = self.mult = self.points * mult

    def div(self, div: int):
        self.points = self.div = self.points / div