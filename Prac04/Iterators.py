mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

#1
words = ("Hello", "Good morning")
iter_ = iter(words)
print(next(iter_))
print(next(iter_))
#2
Word = "Kazakhstan"
letter = iter(Word)
print(next(letter))
print(next(letter))
print(next(letter))
#3
cars_list = ("Toyota", "Mercedes", "BMW")
for brand in cars_list:
    print(brand)
#4
city_name = "Almaty"
for letter in city_name:
    print(letter)
#5
class Counter:
  def __iter__(self):
    self.num = 10
    return self
  def __next__(self):
    val = self.num
    self.num += 10
    return val
obj = Counter()
iterator = iter(obj)
print(next(iterator))
print(next(iterator))
print(next(iterator))