class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()
#1
class Animal:
    def __init__(self, species, color):
        self.species = species
        self.color = color
    def describe(self):
        print(self.species, self.color)
class Pet(Animal):
    pass
p = Pet("Dog", "Brown")
p.describe()
#2
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_info(self):
        print(self.brand, self.model)
class Car(Vehicle):
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand, model)
c1 = Car("Toyota", "Corolla")
c1.show_info()
#3
class Animal:
    def __init__(self, species):
        self.species = species
    def speak(self):
        print("This is a", self.species)
class Pet(Animal):
    def __init__(self, species):
        Animal.__init__(self, species)
p = Pet("Dog")
p.speak()
#4
class Device:
    def __init__(self, name):
        self.name = name
    def info(self):
        print("Device:", self.name)
class Phone(Device):
    def __init__(self, name):
        Device.__init__(self, name)
ph = Phone("iPhone")
ph.info()
#5
class Fruit:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("Fruit:", self.name)
class Citrus(Fruit):
    def __init__(self, name):
        Fruit.__init__(self, name)
c = Citrus("Orange")
c.show()