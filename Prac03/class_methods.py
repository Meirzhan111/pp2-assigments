class Person:
  def __init__(self, name):
    self.name = name
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil")
p1.greet()
#1
class Animal:
    def __init__(self, species):
        self.species = species
    def introduce(self):
        print("I am a " + self.species)
a1 = Animal("Dog")
a1.introduce()
#2
class MathOperations:
    def subtract(self, a, b):
        return a - b
    def divide(self, a, b):
        return a / b
math_op = MathOperations()
print(math_op.subtract(10, 4))
print(math_op.divide(20, 5))
#3
class Animal:
    def __init__(self, species, weight):
        self.species = species
        self.weight = weight
    def get_info(self):
        return f"The {self.species} weighs {self.weight} kg"
a1 = Animal("Elephant", 1200)
print(a1.get_info())
#4
class Tree:
    def __init__(self, species, age):
        self.species = species
        self.age = age
    def grow_one_year(self):
        self.age += 1
        print(f"The {self.species} is now {self.age} years old")
t1 = Tree("Oak", 10)
t1.grow_one_year()
t1.grow_one_year()
#5
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
c1 = Car("Toyota", 2020)
print(c1)
