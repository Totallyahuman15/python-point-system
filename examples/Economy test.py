from PointSystem.Points import points
from PointSystem.Economy import item

you = points(100, classifier="Coins", front=True)
potatoChips = item(price=3.54, demand=10, supply=100, name="Potato Chips", popular=True)
print(potatoChips.price)
potatoChips.progress(time=10)
print(potatoChips.price)
print(" ".join(you.items))
print(potatoChips.supply)
you.show()
you.buy(potatoChips)
you.buy(potatoChips)
you.show()
print(potatoChips.supply)
print(", ".join(you.items))
