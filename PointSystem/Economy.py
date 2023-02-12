import random
class item():

    def __init__(self, demand: int, price: float, supply: int, popular: bool = None):
        self.demand = demand
        self.price = price
        self.supply = supply
        self.multiplier = self.price / self.demand
        self.isPopular = popular

    def progress(self, time: int, *, popular: bool = 0):
        x = None
        while time > 0:
            if popular == 0:
                if self.isPopular == True:
                    x = random.randint(self.demand + 10, self.demand + 30)
                elif self.isPopular == None:
                    x = random.randint(self.demand - 5, self.demand + 5)
                elif self.isPopular == False:
                    x = random.randint(self.demand - 30, self.demand - 10)
                else:
                    pass
            elif popular == True:
                x = random.randint(self.demand + 10, self.demand + 30)
            elif popular == None:
                x = random.randint(self.demand - 5, self.demand + 5)
            elif popular == False:
                x = random.randint(self.demand - 30, self.demand - 10)
            else:
                raise ("Error!")
            time -= 1
            if time <= 0:
                self.demand = x
                self.price = round(self.demand * self.multiplier, 2)