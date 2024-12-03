a1 = float(input("a1 sonni kiriting: "))
b1 = float(input("b1 sonni kiriting: "))
a2 = float(input("a2 sonni kiriting: "))
b2 = float(input("b2 sonni kiriting: "))

son1 = a1 + b1 * 1j
son2 = a2 + b2 * 1j

print(f"1-son: {son1}")
print(f"2-son: {son2}")

def amallar():
    qoshish = son1 + son2
    ayirish = son1 - son2
    kopaytma = son1 * son2
    bolish = son1 / son2
    return qoshish, ayirish, kopaytma, bolish

qoshish, ayirish, kopaytma, bolish = amallar()

print(f"Yig'indisi: {qoshish}")
print(f"Ayirmasi: {ayirish}")
print(f"Ko'paytmasi: {kopaytma}")
print(f"Bolinmasi: {bolish}")