def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#1
def show_items(*items):
    print("Type of items:", type(items))
    print("First item:", items[0])
    print("Second item:", items[1])
    print("All items:", items)
show_items("Apple", "Banana", "Cherry")
#2
def greet_all(message, *people):
    for person in people:
        print(message, person)
greet_all("Hi", "Alex", "Daniel", "Chris")
#3
def show_last_name(**person):
    print("Their last name is " + person["last_name"])
show_last_name(first_name="Alex", last_name="Johnson")
#4
def my_function(*numbers):
    result = 1
    for num in numbers:
        result *= num 
    return result
print(my_function(1, 2, 3))       
print(my_function(10, 20, 30, 40)) 
print(my_function(5))             
#5
def my_function(a, b, c):
    return a * b * c
numbers = [2, 3, 4]
result = my_function(*numbers)
print(result)
