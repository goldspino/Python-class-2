def Num1(num):
  value1 = 2 * num + 1
  return value1

var = Num1(90)
print(var)


def Num2(num):
  value2 = 3 + num * 5
  return value2

var = Num2(80)  
print(var)


class Human:
  def __init__(self, age, name, weight):
    self.age = age
    self.name = name
    self.weight = weight

  def Walk(self):
      print("I am walking")
  
  def Talk(self):
    print("My weight is " + str(self.weight))
    print("My name is " + str(self.name))
    print("My age is " + str(self.age))

Swarup = Human(9, "Swarup", 100)
Swarup.Walk()
Swarup.Talk()