numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
#1
values = [10, 20, 30, 40, 50]
tripled = list(map(lambda n: n * 3, values))
print(tripled)
#2
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
#3
words = ["apple", "banana", "cherry"]
capitalized = list(map(lambda w: w.upper(), words))
print(capitalized)
#4
values = [1, 2, 3, 4]
as_strings = list(map(lambda n: str(n), values))
print(as_strings)
#5
words = ["hello", "world", "python"]
excited = list(map(lambda w: w + "!", words))
print(excited)
