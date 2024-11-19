import numpy as np

# 7x7 o'lchamli matritsa yaratamiz (tasodifiy qiymatlar bilan)
matritsa = np.random.uniform(-100, 100, (7, 7))  # Haqiqiy turdagi elementlar
print("Dastlabki matritsa:")
print(matritsa)

# Eng katta va eng kichik elementlarni aniqlaymiz
max_value = matritsa.max()
min_value = matritsa.min()

# Ularning indekslarini topamiz
max_index = np.unravel_index(np.argmax(matritsa), matritsa.shape)
min_index = np.unravel_index(np.argmin(matritsa), matritsa.shape)

print(f"Eng katta qiymat: {max_value}, indeksi: {max_index}")
print(f"Eng kichik qiymat: {min_value}, indeksi: {min_index}")

# Qiymatlarni almashtiramiz
matritsa[max_index], matritsa[min_index] = matritsa[min_index], matritsa[max_index]

print("Qiymatlar almashtirilgandan keyingi matritsa:")
print(matritsa)
