a = input("4 xonali son kiriting: ")
if len(a) == 4:
    kopaytma = int(a[0]) * int(a[1]) * int(a[2]) * int(a[3])
    print(f'Raqamlar ko\'paytmasi: {kopaytma}')
else:
    print("Siz 4 xonali son kiritmadingiz!")