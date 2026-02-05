class Person:
    def greet(self):
        print("Hello!")
class Student(Person):
    def greet(self):
        print("Hi, I am a student!")
p = Person()
s = Student()
p.greet()
s.greet()
#1
class Animal:
    def sound(self):
        print("Some sound")
class Dog(Animal):
    def sound(self):
        print("Woof!")
a = Animal()
d = Dog()
a.sound()
d.sound()
#2
class Device:
    def info(self):
        print("Generic device")
class Phone(Device):
    def info(self):
        print("This is a phone")
dev = Device()
ph = Phone()
dev.info()
ph.info()
#3
class Vehicle:
    def move(self):
        print("Vehicle is moving")
class Car(Vehicle):
    def move(self):
        print("Car is driving")
v = Vehicle()
c = Car()
v.move()
c.move()
#4
class Fruit:
    def taste(self):
        print("Some taste")
class Orange(Fruit):
    def taste(self):
        print("Citrus and sweet")
f = Fruit()
o = Orange()
f.taste()
o.taste()
#5
class Message:
    def show(self):
        print("Default message")
class Email(Message):
    def show(self):
        print("This is an email")
m = Message()
e = Email()
m.show()
e.show()