class Mother:
    def skills(self):
        print("Cooking, Painting")
class Father:
    def skills(self):
        print("Gardening, Driving")
class Child(Mother, Father):
    pass
c = Child()
c.skills()
#1
class Mother:
    def cooking(self):
        print("Mother can cook")
class Father:
    def driving(self):
        print("Father can drive")
class Child(Mother, Father):
    pass
c = Child()
c.cooking()
c.driving()
#2
class A:
    def show(self):
        print("A's show")
class B:
    def show(self):
        print("B's show")
class C(A, B):
    def show(self):
        print("C's show")
c = C()
c.show()
#3
class A:
    def greet(self):
        print("Hello from A")
class B:
    def greet(self):
        print("Hello from B")
class C(A, B):
    def greet(self):
        super().greet()
        print("Hello from C")
c = C()
c.greet()
#4
class Father:
    def drive(self):
        print("Father drives")
class Mother:
    def paint(self):
        print("Mother paints")
class Uncle:
    def joke(self):
        print("Uncle jokes")
class Child(Father, Mother, Uncle):
    pass
c = Child()
c.drive()
c.paint()
c.joke()
#5
class Parent1:
    hobby = "Gardening"
class Parent2:
    skill = "Coding"
class Child(Parent1, Parent2):
    pass
c = Child()
print(c.hobby)
print(c.skill)