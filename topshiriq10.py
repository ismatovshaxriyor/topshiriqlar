import math

sana = input("sanani kiriting(kun.oy.yil tartibida bo'lsin): ").split('.')
hafta_kunlari = ['dush', 'sesh', 'chor', 'pay', 'juma', 'shan', 'yak']
oy_kunlari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def Oy_kunlari(d):
    if d == 1:
        print(f"Siz kiritgan oyda {oy_kunlari[d - 1]} kun bor")
    elif d == 2:
        print(f"Siz kiritgan oyda {oy_kunlari[d - 1]} kun bor")
    elif d == 3:
        print(f"Siz kiritgan oyda {oy_kunlari[d - 1]} kun bor")
    elif d == 4:
        print(f"Siz kiritgan oyda {oy_kunlari[d - 1]} kun bor")
    elif d == 5:
        print(f"Siz kiritgan oyda {oy_kunlari[d - 1]} kun bor")
    elif d == 6:
        print(f"Siz kiritgan oyda {oy_kunlari[d - 1]} kun bor")
    elif d == 7:
        print(f"Siz kiritgan oyda {oy_kunlari[d - 1]} kun bor")
    elif d == 8:
        print(f"Siz kiritgan oyda {oy_kunlari[d - 1]} kun bor")
    elif d == 9:
        print(f"Siz kiritgan oyda {oy_kunlari[d - 1]} kun bor")
    elif d == 10:
        print(f"Siz kiritgan oyda {oy_kunlari[d - 1]} kun bor")
    elif d == 11:
        print(f"Siz kiritgan oyda {oy_kunlari[d - 1]} kun bor")
    elif d == 12:
        print(f"Siz kiritgan oyda {oy_kunlari[d - 1]} kun bor")
    else:
        print("1 yil 12 oydan iborat")
        return False

def tugri_sana(d, m):
    if d < oy_kunlari[m]:
        print(f"To'g'ri sana kiritildi")
    else:
        print(f"Noto'g'ri sana kiritildi. Siz kiritgan oyda {oy_kunlari[m - 1]} kun bor")

def kunlarsoni(d, m):
    kunlar = 0
    for i in range(m):
        kunlar += oy_kunlari[i]
    print(f"1-yanvardan siz kiritgan sanagacha {kunlar + d} kun bor")

def hafta_kuni(m, y):
    kunlar1 = (y - 1) * 365
    kunlar2 = 0
    for i in range(m):
        kunlar2 += oy_kunlari[i]
    kunlar = kunlar1 + kunlar2
    hafta_kuni = kunlar % 7
    print(f"bu kun {hafta_kunlari[math.floor(hafta_kuni)]} ga to'g'ri keladi")

if int(sana[2]) % 4 != 0 and int(sana[1]) <= 12:
    Oy_kunlari(int(sana[1]))
    tugri_sana(int(sana[0]), int(sana[1]))
    kunlarsoni(int(sana[0]), int(sana[1]))
    hafta_kuni(int(sana[1]), int(sana[2]))
else:
    print("Siz kabisa yili yoki noto'g'ri oy kiritdingiz")
