from PointSystem.Points import points

var = points(0, classifier="Coins", front=True) #You can put any number here, this is the amount the variable starts with
var.add(32)
var.div(3)
var.show()
var.round()
var.show()
var.float()
var.show()
var.mult(32)
var.getStr()
var2 = var.str
print(var2)
var.setClassifier(classifier="Points", front=False)
var.show()
print(var.points)