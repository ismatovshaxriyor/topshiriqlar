x = 2
i = 8
c = 0

while i != 0:
    a = x**2
    if i == 8:
        b = (x**i)/(x**2)
        print(b)
    else:
        b = x**i/c
        print(b)
    i -= 1
    c = a + b
    print(c)


print("Javobi:", c)

