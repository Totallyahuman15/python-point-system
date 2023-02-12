from PointSystem.Points import points
from PointSystem.Economy import item

you = points(100, classifier="Coins", front=True)
potatoChips = item(price=3.54, demand=10, supply=100, popular=True)
print(potatoChips.price)
potatoChips.progress(time=10)
print(potatoChips.price)
you.show()
you.buy(potatoChips)
you.show()