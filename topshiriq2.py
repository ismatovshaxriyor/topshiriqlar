a = float(input("a sonni kiriting: "))
b = float(input("b sonni kiriting: ")) 
c = float(input("c sonni kiriting: "))
d = float(input("d sonni kiriting: "))

if a <= b <= c <= d:
    a, b, c, d = d, d, d, d
    print(f"a = {a}\nb = {b}\nc = {c}\nd = {d}")
elif (a > b > c > d):
    print(f"a = {a}\nb = {b}\nc = {c}\nd = {d}")
else:
    print(f"a = {a**2}\nb = {b**2}\nc = {c**2}\nd = {d**2}")