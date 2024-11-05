import math

x = 2.361
y = 1.149
division = x / y
value = math.log(division)
in_sin = x ** 2 - y
sin_value = math.sin(in_sin)
result = 3 * x * y + value - 17 * sin_value

print(result)
