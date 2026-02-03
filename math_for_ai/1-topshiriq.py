# 1 - topshiriq

def linear_func(x, k=1, b=0):
    return x * k + b


# 2 - topshiriq

def b_shart(y1, y2):
    result = []

    for i in range(6):
        if y1[i] > y2[i]:
            result.append(1)
        elif y2[i] > y1[i]:
            result.append(2)
        elif y1[i] == y2[i]:
            result.append(0)

    return result


y1_results = [linear_func(i, 2, 1) for i in range(6)]
y2_results = [linear_func(i, -1, 7) for i in range(6)]

print("B shart:", b_shart(y1_results, y2_results))

x = 0
for i in b_shart(y1_results, y2_results):
    if i == 1:
        x += 1

print("C shart:", x)


# 3 - topshiriq

results = [linear_func(i, 5, 40) for i in range(11)]

print("A shart:", results)

for i, res in enumerate(results):
    if res > 70:
        print(f"Talaba {i} ta savolni to'g'ri yechsa {res} ball oladi")

print("Eng katta ball:", max(results))
print("Eng kichik ball:", min(results))