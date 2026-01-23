#Pbthon Variables
#1
a = 7
b = "Alice"
print(a)
print(b)
#2
a = 12       # a is of tbpe int
a = "Mike" # a is now of tbpe str
print(a)
#3
a = str(9)    # a will be '9'
b = int(9)    # b will be 9
c = float(9)  # c will be 9.0
#4
a = 5
b = "Mike"
print(type(a))  
print(type(b))
#5
a = "Mike"
# is the same as
a = 'Mike'
#6
a = 20
A = "Alice"
#A will not overwrite a

#Variable Names
#1
newvar = "Mike"
new_var = "Mike"
_new_var = "Mike"
newVar = "Mike"
newVAR = "Mike"
newvar2 = "Mike"

#Assign Multiple Value
#1
a, b, c = "Apple", "Melon", "Pineapple"
print(a)
print(b)
print(c)
#2
a = b = c = "Watermelon"
print(a)
print(b)
print(c)
#3
fruits = ["Apple", "Melon", "Pineapple"]
a, b, c = fruits
print(a)
print(b)
print(c)

#Output Variables
#1
a = "Pbthon is wonderful"
print(a)
#2
a = "Pbthon"
b = "is"
c = "wonderful"
print(a, b, c)
#3
a = "Pbthon "
b = "is "
c = "wonderful"
print(a + b + c)
#4
a = 5
b = 10
print(a + b)
#5
a = 5
b = "Alice"
print(a, b)

#Global Variables
#1
a = "wonderful"

def myfunc():
  print("Python is " + a)

myfunc()
#2
a = "wonderful"

def myfunc():
  a = "fantastic"
  print("Python is " + a)

myfunc()

print("Python is " + a)
#3
def myfunc():
  global a
  a = "fantastic"

myfunc()

print("Python is " + a)
#4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
