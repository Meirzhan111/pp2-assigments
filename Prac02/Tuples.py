thistuple = ("apple", "banana", "cherry")
print(thistuple)

#1
Country = ("China","Germany","Russia","Kazakhstan")
print(Country)
#2
names = ("Alinur", "Saule", "Aibol","Jarkyn")
print(names[::-1])
#3
Instruments = ("Dombra", "Piano", "Kobyz","Guitar")
y = list(Instruments)
y.append("Cello")
Instruments = tuple(y)
#4
Animals = ("Cat","Bunny","Hourse")
mytuple = Animals * 5
print(mytuple)
#5
numbers = (1,2,5,8,7,9,4,2,6,5)
counter = numbers.count(2)
print(counter)
