numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
#1
numbers = [2, 5, 7, 1, 9, 4, 3, 8]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)
#2
values = [1, 3, 5, 7, 9, 11]
range_numbers = list(filter(lambda x: 3 <= x <= 7, values))
print(range_numbers)
#3
words = ["cat", "elephant", "dog", "tiger", "ant"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)
#4
nums = [10, -5, 3, -1, 0, 7]
negative_numbers = list(filter(lambda x: x < 0, nums))
print(negative_numbers)
#5
numbers = [2, 3, 4, 6, 7, 9, 10, 12]
divisible_by_three = list(filter(lambda x: x % 3 == 0, numbers))
print(divisible_by_three)