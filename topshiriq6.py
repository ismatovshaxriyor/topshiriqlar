a = input("To'plam kiriting(sonlarni faqat vergul bilan ajratib yozing): ").split(',')
k = int(input("k sonni kiriting: "))
h = int(input('h sonni kiriting: '))

if 1 <= k < h <= len(a):
    oraliq = a[k:(h+1)] # a to'plamdagi k- va h- elemetni ajratib oladi
    keyingi_oraliq = [] # o'rni almashtirilgan elementlar shu bo'sh to'plam ichiga qo'shib boriladi
    
    i = 0
    while i < len(oraliq) // 2:
        item1 = oraliq[i] # ajratib olingan elementlarning dastlabki elementilari olinib item1 ga tenglanadi
        item2 = oraliq[-(i + 1)] # ajratib olingan elementlarning oxirgi elementlari olinib item2ga tenglanadi
        keyingi_oraliq.append(item2) # o'rnini almashtitish maqsadida oxirgi element birnchi keyingi_oraliq to'plamiga qo'shiladi
        keyingi_oraliq.append(item1)
        i += 1
    
    if len(oraliq) % 2 != 0: # agar o'rtada ortiqcha son bo'lsa bu shart bajariladi
        orta_index = len(oraliq) // 2 # o'sha ortiqcha sonning indeksini anqilash uchun
        orta_element = oraliq[orta_index] # o'sha ortiqcha elementni orta_element o'zgaruvchisiga tenglaymiz
        keyingi_oraliq.insert(orta_index, orta_element) # o'sha ortiqcha element o'z o'rniga joylashtiriladi

    print(f"Oldingi oraliq: {oraliq}")
    print(f"Keyingi oraliq: {keyingi_oraliq}")
else:
    print("Kiritilgan k soni h soni kichi bo'lishi kerak va h soni a to'plamning uzunligiga teng yoki undan kkchik bo'lishi kerak")