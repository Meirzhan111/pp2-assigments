class MyClass:
    x = 10
obj1 = MyClass()
obj2 = MyClass()
print(obj1.x)
print(obj2.x)
#1
class Book:
    category = "Fiction"
b1 = Book()
b2 = Book()
print(b1.category)
print(b2.category)
#2
class Numbers:
    values = [1, 2, 3]
n1 = Numbers()
n2 = Numbers()
print(n1.values)
print(n2.values)
#3
class Light:
    is_on = True
l1 = Light()
l2 = Light()
print(l1.is_on)
print(l2.is_on)
#4
class Counter:
    count = 0
c1 = Counter()
c2 = Counter()
Counter.count += 5
print(c1.count)
print(c2.count)
#5
class Person:
    total_people = 0
    def __init__(self, name):
        self.name = name
        Person.total_people += 1
p1 = Person("Alice")
p2 = Person("Bob")
p3 = Person("Charlie")
print(Person.total_people)
