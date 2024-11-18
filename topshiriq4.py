a = int(input("4 xonali son kiriting: "))

minglar_xonasi = a // 1000
yuzlar_xonasi = (a // 100) % 10
onlar_xonasi = (a // 10) % 10 
birlar_xonasi = a % 10

if a >= 1000 and a <= 9999:
    kopaytma = minglar_xonasi * yuzlar_xonasi * onlar_xonasi * birlar_xonasi
    print(f"Raqamlar ko'paytmasi: {kopaytma}")
else:
    print("4 xonali son kiritmadingiz!")