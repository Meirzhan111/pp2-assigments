x = lambda a : a + 10
print(x(5))
#1
multiply = lambda x, y: x * y
print(multiply(7, 8))
#2
add_three = lambda p, q, r: p + q + r
print(add_three(3, 7, 5))
#3
def make_multiplier(factor):
    return lambda x: x * factor
mytripler = make_multiplier(3)
print(mytripler(7))
#4
def multiplier(factor):
    return lambda x: x * factor
double_it = multiplier(4)
triple_it = multiplier(5)
print(double_it(6))
print(triple_it(6))
#5
def create_multiplier(factor):
    return lambda x: x * factor
quadrupler = create_multiplier(4)
print(quadrupler(5))
