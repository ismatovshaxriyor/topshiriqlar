sana = input("sanani kiriting(kun.oy.yil tartibida bo'lsin): ").split('.')
print(sana)
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
        a = False
        return a

def tugri_sana():
    

Oy_kunlari(int(sana[1]))
