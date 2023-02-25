from PointSystem.Points import points
from PointSystem.Economy import item, econ_progress

you = points(100, classifier="Coins", front=True)
potatoChips = item(price=3.54, demand=10, supply=100, name="Potato Chips", popular=True)
pp = item(price=234.33, demand=32, supply=32000, name="asdASDasd", popular=None)
print(potatoChips.price)
econ_progress(time=10)
print(f"Potato Chips: {potatoChips.price}\n"
      f"pp: {pp.price}")
print(potatoChips.price)
print(" ".join(you.items))
print(potatoChips.supply)
you.show()
you.buy(potatoChips)
you.buy(potatoChips)
you.show()
print(potatoChips.supply)
print(", ".join(you.items))
econ_progress(time=100)
print(f"Potato Chips: {potatoChips.price}\n"
      f"pp: {pp.price}")

