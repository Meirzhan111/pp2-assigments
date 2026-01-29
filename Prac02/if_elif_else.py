a = 33
b = 200
if b > a:
  print("b is greater than a")

#1
temperature = 30
if temperature > 25:
    print("It's hot outside")
#2
score1 = 85
score2 = 92
if score2 > score1:
    print("score2 is higher than score1")
elif score1 == score2:
    print("Both scores are equal")
#3
temperature = 15
threshold = 20
if temperature > threshold:
    print("Temperature is above threshold")
elif temperature == threshold:
    print("Temperature is exactly at threshold")
else:
    print("Temperature is below threshold")
#4
speed = 80
limit = 60
if speed > limit: print("You are over the speed limit")
#5
temperature = 30
humidity = 80
wind = 20
if temperature > 25 or humidity > 70:
    print("The weather is either hot or very humid")
