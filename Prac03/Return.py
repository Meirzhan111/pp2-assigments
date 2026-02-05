def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))
#1
def compute_factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * compute_factorial(number - 1)
print(compute_factorial(6))
#2
def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)
print(fib(8))
#3
def total_elements(elements):
    if len(elements) == 0:
        return 0
    else:
        return elements[0] + total_elements(elements[1:])
numbers = [10, 20, 30, 40]
print(total_elements(numbers))
#4
def get_largest(values):
    if len(values) == 1:
        return values[0]
    else:
        largest_rest = get_largest(values[1:])
        return values[0] if values[0] > largest_rest else largest_rest
my_values = [5, 12, 4, 8, 3]
print(get_largest(my_values))
#5
import sys
print("Current recursion limit is:", sys.getrecursionlimit())
