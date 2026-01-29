fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#1
tasks = ["Homework", "Cleaning", "Shopping"]
for task in tasks:
    print(task)
    if task == "Cleaning":
        print("Stopping at cleaning task")
        break
#2
stations = ["Station A", "Station B", "Station C"]
for station in stations:
    if station == "Station B":
        break
    print(station)
#3
tasks = ["Homework", "Cleaning", "Shopping"]
for task in tasks:
    if task == "Cleaning":
        continue
    print(task)
#4
for num in range(11, 33):
  print(num)
#5
for num in range(5, 40, 4):
  print(num)