i = input("koordinatalar sonini kiriting: ")
n = int(i)

def x():
    i = 1
    xN = 0
    while i < (n + 1):
        xN += i
        i += 1
    return float(xN/n)

def y():
    i = 1
    yN = 0
    while i < (n + 1):
        yN += i
        i += 1
    return float(yN/n)

def z():
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


print(f"massa markazi ({x()}, {y()}, {y()}) nuqtada")
masofalar()