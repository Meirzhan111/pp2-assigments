#Python Strings
#1
a = "My name is Meirzhan"
print(a)
b = 'My name is Meirzhan'
print(b)
c = '''My name is Meirzhan'''
print(c)

#Slicing String
#1
b = "My name is Meirzhan"
print(b[3:6])
#2
b = "Hello, World!"
print(b[-6:-3])

#Modify Strings
#1
a = "Kazakhstan!"
print(a.upper())
#2
a = "KAZAKHSTAN!"
print(a.lower())
#3
a = " welcome "
print(a.strip()) # returns "welcome"
#4
a = "Welcome to kbtu"
print(a.replace("o", "t"))
#5
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
#1
a = "Bye"
b = "Bye"
c = a + b
print(c)

#Format - Strings
#1
weight = 60
txt = f"My name is Meirzhan, my weight is {weight}"
print(txt)

#Escape Characters
#1
txt = "We are the so-called \"Vikings\" from the north."

