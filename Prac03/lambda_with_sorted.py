students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
#1
words = ["apple", "pie", "banana", "cherry"]
sorted_by_last_letter = sorted(words, key=lambda x: x[-1])
print(sorted_by_last_letter)
#2
numbers = [10, -3, 7, -1, 0]
sorted_by_abs = sorted(numbers, key=lambda x: abs(x))
print(sorted_by_abs)
#3
students = [("Alice", 90), ("Bob", 85), ("Charlotte", 95)]
sorted_by_name_length = sorted(students, key=lambda x: len(x[0]))
print(sorted_by_name_length)
#4
numbers = [5, 2, 7, 4, 9, 6]
sorted_even_first = sorted(numbers, key=lambda x: x % 2)
print(sorted_even_first)
#5
words = ["Hello", "WORLD", "PyThon", "code"]
sorted_by_upper = sorted(words, key=lambda x: sum(1 for c in x if c.isupper()))
print(sorted_by_upper)
