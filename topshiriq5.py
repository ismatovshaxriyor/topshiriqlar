import re  # noqa: F401

i = input("koordinatalar sonini kiriting: ")

def x(n):
    i = 1
    xN = 0
    while i < (n + 1):
        xN += i
        i += 1
    return float(xN/n)

def y(n):
    i = 1
    yN = 0
    while i < (n + 1):
        yN += i
        i += 1
    return float(yN/n)

def z(n):
    i = 1
    zN = 0
    while i < (n + 1):
        zN += i
        i += 1
    return float(zN/n)

def masofalar():
    i = 1
    while i < (n + 1):
        d = ((i - x())**2 + (i - y())**2 + (i - z())**2)**(1/2)
        print(f"massa markazidan {i}-nuqtagacha bo'lgan masofa: {d}")
        i += 1


regex = re.findall("[0-9]", i)
if regex:
    n = int(i)
    print(f"massa markazi ({x(n)}, {y(n)}, {y(n)}) nuqtada")
    masofalar(n)
else:
    print("natural son kiriting")




