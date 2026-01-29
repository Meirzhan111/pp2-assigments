thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#1
subject = {
    "name": "Mathematics",
    "level": "School",
    "hours": 5
}
print(subject["name"])
#2
device = {
    "type": "Laptop",
    "brand": "HP",
    "ram": "16GB"
}
x = device.keys()
print(x)
#3
course = {
    "name": "Physics",
    "level": "High School",
    "hours": 6
}
course.pop("level")
print(course)
#4
planets = {
    "Mercury": 1,
    "Venus": 2,
    "Earth": 3
}
for planet in planets:
    print(planet)
#5
city1 = {
    "name": "Paris",
    "population": 2148327
}
city2 = {
    "name": "London",
    "population": 8982000
}
city3 = {
    "name": "Tokyo",
    "population": 13929286
}
countries = {
    "city1": city1,
    "city2": city2,
    "city3": city3
}
print(countries)
