a = input("To'plam kiriting(sonlarni faqat vergul bilan ajratib yozing): ").split(',')
k = int(input("k sonni kiriting: "))
h = int(input('h sonni kiriting: '))

if 1 <= k < h <= len(a):
    oraliq = a[k:(h+1)]
    keyingi_oraliq = []
    i = 0
    
    while i < len(oraliq) // 2:
        item1 = oraliq[i]
        item2 = oraliq[-(i + 1)]
        keyingi_oraliq.append(item2)
        keyingi_oraliq.append(item1)
        i += 1

    if len(oraliq) % 2 != 0:
        orta_index = len(oraliq) // 2
        orta_element = oraliq[orta_index]
        keyingi_oraliq.insert(orta_index, orta_element)

    print(f"Oldingi oraliq: {oraliq}")
    print(f"Keyingi oraliq: {keyingi_oraliq}")
else:
    print("k va h indekslari noto'g'ri!")
