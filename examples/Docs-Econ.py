from PointSystem.Points import points
from PointSystem.Economy import item

item = item(price=3.50, demand=100, supply=1000, popular=None)
you = points(100, classifier="Coins", front=True)
print(f"{item.price}, {item.demand}, {item.supply}")
item.progress(time=10)
print(f"{item.price}, {item.demand}, {item.supply}")
print(item.isPopular)
item.progress(time=1, popular=True)
print(item.isPopular)