import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])
#1
import json
fruit_info = '{"type": "Apple", "weight": 200, "origin": "Almaty"}'
data = json.loads(fruit_info)
print(data["weight"])
#2
import json
fruit_data = {
    "type": "Mango",
    "weight": 500,
    "country": "Thailand"
}
json_output = json.dumps(fruit_data)
print(json_output)
#3
import json
fruit_stock = {
    "variety": "Gala",
    "quantity": 150,
    "organic": True,
    "imported": False,
    "suppliers": ("GreenFarm", "EcoGarden"),
    "pests": None,
    "batches": [
        {"id": "A-101", "weight_kg": 15.5},
        {"id": "B-202", "weight_kg": 20.3}
    ]
}
result = json.dumps(fruit_stock, indent=4)
print(result)
#4
import json
fruit_stock = {
    "variety": "Gala",
    "quantity": 150,
    "organic": True,
    "imported": False,
    "suppliers": ("GreenFarm", "EcoGarden"),
    "pests": None,
    "batches": [
        {"id": "A-101", "weight_kg": 15.5},
        {"id": "B-202", "weight_kg": 20.3}
    ]
}
print(json.dumps(fruit_stock, indent=4, separators=(". ", " = ")))
#5
import json
fruit_stock = {
    "variety": "Gala",
    "quantity": 150,
    "organic": True,
    "imported": False,
    "suppliers": ("GreenFarm", "EcoGarden"),
    "pests": None,
    "batches": [
        {"id": "A-101", "weight_kg": 15.5},
        {"id": "B-202", "weight_kg": 20.3}
    ]
}
print(json.dumps(fruit_stock, indent=4, sort_keys=True))