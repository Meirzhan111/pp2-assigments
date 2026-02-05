def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#1
def show_name(name):
    print(name + " Smith")
show_name("Alex")
show_name("Daniel")
show_name("Chris")
#2
def display_full_name(first, last):
    print(first + " " + last)
display_full_name("Alex", "Johnson")
#3
def greet(person="buddy"):
    print("Hi", person)
greet("Alex")
greet("Daniel")
greet()
greet("Chris")
#4
def introduce(city="Paris"):
    print("I live in", city)
introduce("London")
introduce("Tokyo")
introduce()
introduce("New York")
#5
def pet_info(pet_type, pet_name):
    print("I own a", pet_type)
    print("My", pet_type + "'s name is", pet_name)
pet_info(pet_type="cat", pet_name="Whiskers")
