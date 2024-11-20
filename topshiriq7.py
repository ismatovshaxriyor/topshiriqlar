matritsa = [
    [1, 0, 2, 3, 4, 5, 6, 90],
    [-12, -3, 34, -32, 62, 12, 32.4],
    [-23, 54.3, -4.2, -82.1, -52.7, -32, 17.9],
    [8, 9, 10, 11, 12, 13, -90],
    [-12, -32, 90, 2.6, -28.5, -12.7, -32.4],
    [32, -14.3, -43, 23.7, -12, -43, 23.7],
    [53, 32, -32, 47, -12.4, -45.6, 60]
]

katta_sonlar = []
katta_sonlar_index = []
kichik_sonlar = []
kichik_sonlar_index = []

def for_max():
    for row in matritsa:
        max_element = max(row)
        max_element_index = row.index(max_element)
        katta_sonlar.append(max_element)
        katta_sonlar_index.append(max_element_index)
    return katta_sonlar, katta_sonlar_index

def for_min():
    for row in matritsa:
        min_element = min(row)
        min_element_index = row.index(min_element)
        kichik_sonlar.append(min_element)
        kichik_sonlar_index.append(min_element_index)
    return kichik_sonlar, kichik_sonlar_index

maximums, max_indexs = for_max()
minimums, min_indexs = for_min()

matritsa_max = max(maximums)
print(f'matritsaning maksimal qiymati: {matritsa_max}')
matritsa_min = min(minimums)
print(f'matritsaning minimal qiymati: {matritsa_min}')

matritsa_max_index1 = maximums.index(matritsa_max)
matritsa_max_index2 = max_indexs[matritsa_max_index1]
print(f"matritsaning maksimal qiymati {matritsa_max_index1 + 1}-qatorning {matritsa_max_index2 + 1}-tartibida joylashgan")

matritsa_min_index1 = minimums.index(matritsa_min)
matritsa_min_index2 = min_indexs[matritsa_min_index1]
print(f"matritsaning minimal qiymati {matritsa_min_index1 + 1}-qatorning {matritsa_min_index2 + 1}-tartibida joylashgan")

matritsa[matritsa_max_index1][matritsa_max_index2], matritsa[matritsa_min_index1][matritsa_min_index2] = matritsa[matritsa_min_index1][matritsa_min_index2], matritsa[matritsa_max_index1][matritsa_max_index2]

for row in matritsa:
    print(row)

