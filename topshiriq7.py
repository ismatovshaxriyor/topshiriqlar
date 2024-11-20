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
    for row in matritsa: # matritsadan har bir qatorni ajratib oladi
        max_element = max(row) # har bir qatordagi maksimal qiymatni oladi
        max_element_index = row.index(max_element) # va o'sha maksilmal qiymatning indeksini aniqlaydi
        katta_sonlar.append(max_element) # olingan katta sonni katta_sonlar listiga qo'shadi
        katta_sonlar_index.append(max_element_index) # va o'sha katta sonning olingan indeksini katta_sonlar_index listiga qo'shadi
    return katta_sonlar, katta_sonlar_index

def for_min():
    for row in matritsa: # matritsadan har bir qatorni ajratib oladi
        min_element = min(row) # har bir qatordagi minimal qiymatni oladi
        min_element_index = row.index(min_element) # va o'sha minimal qiymatning indeksini aniqlaydi
        kichik_sonlar.append(min_element) # olingan kichik sonni kichik_sonlar listiga qo'shadi
        kichik_sonlar_index.append(min_element_index) # va o'sha kichik sonning olingan indeksini kichik_sonlar_index listiga qo'shadi
    return kichik_sonlar, kichik_sonlar_index

maximums, max_indexs = for_max() # har bir qatordagi katta sonlarni maximums o'zgaruvchisiga, ularning indekslarini max_indexs o'zgaruvchisiga qo'shib oladi
minimums, min_indexs = for_min() # har bir qatordagi kichik sonlarni minimums o'zgaruvchisiga, ularning indekslarini min_indexs o'zgaruvchisiga qo'shib oladi

matritsa_max = max(maximums) # butun matritsadagi eng katta qiymatni oladi
print(f'matritsaning maksimal qiymati: {matritsa_max}')
matritsa_min = min(minimums) # butun matritsadagi eng kichik qiymatni oladi
print(f'matritsaning minimal qiymati: {matritsa_min}')

matritsa_max_index1 = maximums.index(matritsa_max) # matritsaning eng katta qiymatining qator bo'yicha indeksini oladi
matritsa_max_index2 = max_indexs[matritsa_max_index1] # matritsaning eng katta qiymatining ustun bo'yicha indeksini oladi
print(f"matritsaning maksimal qiymati {matritsa_max_index1 + 1}-qatorning {matritsa_max_index2 + 1}-tartibida joylashgan")

matritsa_min_index1 = minimums.index(matritsa_min) # matritsaning eng kichik qiymatining qator bo'yicha indeksini oladi
matritsa_min_index2 = min_indexs[matritsa_min_index1] # matritsaning eng kichik qiymatining ustun bo'yicha indeksini oladi
print(f"matritsaning minimal qiymati {matritsa_min_index1 + 1}-qatorning {matritsa_min_index2 + 1}-tartibida joylashgan")

matritsa[matritsa_max_index1][matritsa_max_index2], matritsa[matritsa_min_index1][matritsa_min_index2] = matritsa[matritsa_min_index1][matritsa_min_index2], matritsa[matritsa_max_index1][matritsa_max_index2]
# ularning o'rni almashtiriladi

for row in matritsa:
    print(row) # matritsaning har bir qatorini chiqarib beradi

