i = 1
while i < 6:
  print(i)
  i += 1

#1
temperature = 20
while temperature < 25:
    print("Current temperature:", temperature)
    temperature += 1
#2
level = 1
while level < 6:
    print("Level", level)
    if level == 3:
        print("Stopping at level 3")
        break
    level += 1
#3
step = 0
while step < 6:
    step += 1
    if step == 3:
        continue
    print("Step number:", step)
#4
level = 1
while level < 4:
    print("Current game level:", level)
    level += 1
else:
    print("You have completed all the levels")
#5
pages = 1
while pages < 4:
    print("Reading page", pages)
    pages += 1
else:
    print("Finished reading the book")