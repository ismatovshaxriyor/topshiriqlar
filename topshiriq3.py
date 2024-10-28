x = float(input('x sonni kiriting: '))
i = 8
c = 0

if x != 0:
    while i != 0:
        a = x**2
        print(f"a = {a}")
        if i == 8:
            b = (2**i)/(x**2)
            print(f'b = {b}')
        else:
            b = 2**i/c
            print(f'b = {b}')
        i -= 1
        c = a + b
        print(f'c = {c}')

    javob = x / c
    print("Javobi:", javob)

else:
    print("x soni 0 ga teng bo'lishi mumkin emas")

