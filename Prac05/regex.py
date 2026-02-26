import re
#1 
s = "abbb"
print(bool(re.fullmatch(r"ab*", s)))
#2
s = "abb"
print(bool(re.fullmatch(r"ab{2,3}", s)))
#3
s = "hello_world test_case"
print(re.findall(r"[a-z]+_[a-z]+", s))
#4
s = "Hello World Apple"
print(re.findall(r"[A-Z][a-z]+", s))
#5
s = "axxxb"
print(bool(re.fullmatch(r"a.*b", s)))
#6
s = "Hello, world. Python"
result = re.sub(r"[ ,.]", ":", s)
print(result)
#7
def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)

print(snake_to_camel("hello_world_test"))
#8
s = "HelloWorldPython"
print(re.findall(r"[A-Z][^A-Z]*", s))
#9
s = "HelloWorldPython"
result = re.sub(r"([A-Z])", r" \1", s).strip()
print(result)
#10
s = "helloWorldPython"
result = re.sub(r"([A-Z])", r"_\1", s).lower()
print(result)