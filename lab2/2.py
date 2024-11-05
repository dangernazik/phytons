def func(x, k):
    return (x**(4*k + 3)) / (4*k + 3)

x =  0.2
d = 10**-6
h = 0.01

while x <= 0.3:
    k = 0
    sum_ = 0
    while func(x, k) >= d:
        sum_ += func(x, k)
        k += 1
    print(f"Результат при x= {x:.2f} : {sum_}")
    x += h




















