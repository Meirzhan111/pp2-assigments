#RegEx examples
import re
#1 
a = "abbb"
print(bool(re.fullmatch(r"ab*", a)))
#2
a = "abb"
print(bool(re.fullmatch(r"ab{2,3}", a)))
#3
a = "hello_world test_case"
print(re.findall(r"[a-z]+_[a-z]+", a))
#4
a = "Hello World Apple"
print(re.findall(r"[A-Z][a-z]+", a))
#5
a = "axxxb"
print(bool(re.fullmatch(r"a.*b", a)))
#6
a = "Hello, world. Python"
result = re.sub(r"[ ,.]", ":", a)
print(result)
#7
def snake_to_camel(a):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), a)

print(snake_to_camel("hello_world_test"))
#8
a = "HelloWorldPython"
print(re.findall(r"[A-Z][^A-Z]*", a))
#9
a = "HelloWorldPython"
result = re.sub(r"([A-Z])", r" \1", a).strip()
print(result)
#10
a = "helloWorldPython"
result = re.sub(r"([A-Z])", r"_\1", a).lower()
print(result)


#receipt parsing examples
import re
import json
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
#1
prices = re.findall(r"\d[\d ]*,\d{2}", text)
#2
products = re.findall(r"\d+\.\n(.+)", text)
#3
total_match = re.search(r"ИТОГО:\n([\d ]+,\d{2})", text)
total = total_match.group(1) if total_match else None
#4
datetime_match = re.search(r"Время:\s*(.+)", text)
datetime = datetime_match.group(1) if datetime_match else None
#5
payment_match = re.search(r"(Банковская карта|Наличные)", text)
payment = payment_match.group(1) if payment_match else None
#6
data = {
    "products": products,
    "prices": prices,
    "total": total,
    "datetime": datetime,
    "payment_method": payment
}
print(json.dumps(data, ensure_ascii=False, indent=4))