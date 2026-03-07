names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
for index, name in enumerate(names):
    print(index, name)
for name, score in zip(names, scores):
    print(name, score)
x = "123"
print(type(x))
num = int(x)
print(num, type(num))