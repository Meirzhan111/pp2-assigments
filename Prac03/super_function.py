class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()
#1
class Animal:
    def __init__(self, species):
        self.species = species
    def speak(self):
        print("This is a", self.species)
class Pet(Animal):
    def __init__(self, species):
        super().__init__(species)
p = Pet("Dog")
p.speak()
#2
class Device:
    def __init__(self, name):
        self.name = name
    def info(self):
        print("Device:", self.name)
class Phone(Device):
    def __init__(self, name):
        super().__init__(name)
ph = Phone("iPhone")
ph.info()
#3
class Fruit:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("Fruit:", self.name)
class Citrus(Fruit):
    def __init__(self, name):
        super().__init__(name)
c = Citrus("Orange")
c.show()
#4
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def display(self):
        print("Brand:", self.brand)
class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
my_car = Car("Toyota")
my_car.display()
#5
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello,", self.name)
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
s = Student("Alice")
s.greet()