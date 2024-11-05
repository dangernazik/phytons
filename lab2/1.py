import math

a = 2
b = 4
h = 0.2
x = a

def calculate_value(x):
    if x < 2.5:
        ln_x_squared = math.log(x ** 2)
        result = math.cos(ln_x_squared)
        print(f"x = {x}")
    elif 2.5 <= x <= 3.5:
        result = math.cos(1 / x**4)
        print(f"x = {x}")
        # return result
    else:
        result = math.tan(math.sin(x))
        print(f"x = {x}")
    return result



while x <= b:
    calculate_value(x)
    x = x + h
