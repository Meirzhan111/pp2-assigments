day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#1
month = 3
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
#2
score = 85
match score:
    case 90 | 100:
        print("Excellent")
    case 75 | 80 | 85:
        print("Good job")
    case 50 | 60 | 70:
        print("Needs improvement")
    case _:
        print("Failing")
#3
level = "medium"
match level:
    case "easy":
        print("You can solve this quickly")
    case "hard":
        print("This will take time")
    case _:
        print("Keep trying, it's a moderate challenge")
#4
score = 85
subject = "Math"
match score:
    case 90 | 100 if subject == "Math":
        print("Excellent in Math")
    case 80 | 85 if subject == "Math":
        print("Good job in Math")
    case 50 | 60 | 70 if subject == "Science":
        print("Needs improvement in Science")
    case _:
        print("Keep practicing")
#5
temperature = 30
match temperature:
    case temp if temp > 35:
        print("It's extremely hot")
    case temp if 25 <= temp <= 35:
        print("It's warm outside")
    case temp if 15 <= temp < 25:
        print("It's mild")
    case _:
        print("It's cold")
