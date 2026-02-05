class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Emil", 36)
print(p1.name)
print(p1.age)
#1
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
s1 = Student("Alice", 90)
print(s1.name)
print(s1.grade)
#2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
b1 = Book("1984", "George Orwell")
print(b1.title)
print(b1.author)
#3
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
c1 = Car("Toyota", 2020)
print(c1.brand)
print(c1.year)
#4
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price  
p1 = Product("Laptop", 1200)
print(p1.name)
print(p1.price)
#5
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
m1 = Movie("Inception", 8.8)
print(m1.title)
print(m1.rating)