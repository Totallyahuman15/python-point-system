from tkinter import *
from src.PointSystem_Totallyahuman15.PointSystem import *

root = Tk()
root.title("Example")
root.geometry("500x500")

p = points(0, classifier="Coins", front=True)

add = Button(root, text="Add 1 coin", command=lambda: p.add(1))
add.pack()

sub = Button(root, text="Subtract 1 coin", command=lambda: p.sub(1))
sub.pack()

mult = Button(root, text="Multiply by 3", command=lambda: p.mult(3))
mult.pack()

div = Button(root, text="Divide by 3", command=lambda: p.div(3))
div.pack()

def show():
    p.getStr()
    CoinLabel = Label(root, text=p.str)
    CoinLabel.pack()

show = Button(root, text="Show coin amount", command=show)
show.pack()

root.mainloop()