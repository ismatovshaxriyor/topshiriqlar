n = int(input("fazoda nechta nuqta bor: "))

x_row = []
y_row = []
z_row = []

def koordinatalar():
    for i in range(n):
        x_koordinata = float(input(f"x{i+1}-koordinatani kiriting: "))
        x_row.append(x_koordinata)
        y_koordinata = float(input(f"y{i+1}-koordinatani kiriting: "))
        y_row.append(y_koordinata)
        z_koordinata = float(input(f"z{i+1}-koordinatani kiriting: "))
        z_row.append(z_koordinata)
    return x_row, y_row, z_row

x_koordinatalar, y_koordinatalar, z_koordinatalar = koordinatalar()

def markaz():
    i = 0
    x_markaz = 0
    y_markaz = 0
    z_markaz = 0
    while i < n:
        x_markaz = x_markaz + x_koordinatalar[i]
        y_markaz = y_markaz + y_koordinatalar[i]
        z_markaz = z_markaz + z_koordinatalar[i]
        i += 1
    return x_markaz/n, y_markaz/n, z_markaz/n

def markazdan_nuqtagacha():
    i = 0
    while i < n:
        masofa = ((x_row[i] - markaz()[0])**2 + (y_row[i] - markaz()[1])**2 + z_row[i] - markaz()[2]**2)**0.5
        print(f"Markazdan {i+1}-nuqta gacha masofa: {masofa}")
        i += 1

print(f'Markaz koordinatalari: {markaz()}')
markazdan_nuqtagacha()

