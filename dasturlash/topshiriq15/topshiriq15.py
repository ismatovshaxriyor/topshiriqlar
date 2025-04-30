"""a) texnik holati yaxshi bo'lgan barcha avtomobillar haqidagi ma'lumot
chop etilsin;
b) ko'rsatilgan avtomobil nomeri bo'yicha uning texnik holati
aniqlansin;
d) texnik holati yaxshi bo'lgan barcha avtomobillar haqidagi ma'lumot
fayldan o'chirilsin."""

import pickle

class Avto:
    def __init__(self, tabel_raqam, egasi, nomer, turi):
        self.tabel_raqam = tabel_raqam
        self.egasi = egasi
        self.nomer = nomer
        self.turi = turi
    
    def malumot(self, tabel_raqami):
        if self.tabel_raqam == tabel_raqami:
            return self.egasi, self.nomer, self.turi
    
    def nomer_malumot(self, nomer):
        if self.nomer == nomer:
            return self.tabel_raqam

class TexnikHolat:
    def __init__(self, tabel_raqam, holat): 
        self.tabel_raqam = tabel_raqam
        self.holat = holat
    
    def tex_holat(self, tabel_raqami):
        if self.tabel_raqam == tabel_raqami:
            return self.holat

avtolar = []
holatlar = []
umumiy_holarlar = {
    1: "Yaxshi",
    2: "Qoniqarli",
    3: "Qoniqarsiz"
}

with open("AVTO", "rb") as f:
    avto_lar = pickle.load(f)
    for avto in avto_lar:
        avtolar.append(avto)

with open("TA_MIR", "rb") as f:
    holat_lar = pickle.load(f)
    for holat in holat_lar:
        holatlar.append(holat)

# # A shart
# for holat in holatlar:
#     mashina_holati = holat.holat
#     mashina_nomeri = holat.tabel_raqam
    
#     try:
#         mashina = [avto for avto in avtolar if avto.malumot(mashina_nomeri)]
#         if mashina_holati == 1:
#             egasi = mashina[0].egasi
#             nomeri = mashina[0].nomer
#             turi = mashina[0].turi
#             print(f"Mashina Egasi: {egasi}, Mashina nomeri: {nomeri}, Mashina turi: {turi}")
#     except:
#         continue


# # B shart
# nomer = input("Mashina nomerini kiriting: ")

# for avto in avtolar:
#     try:
#         tabel_raqami = avto.nomer_malumot(nomer)
#         holati = [holat.holat for holat in holatlar if holat.tex_holat(tabel_raqami)]
#         if holati:
#             print(f"{nomer} nomerli mashina holati: {umumiy_holarlar.get(holati[0])}")
#     except:
#         continue


# # C shart
# holat_yaxshi = [holat.tabel_raqam for holat in holatlar if holat.holat == 1]
# avtolar = [avto for avto in avtolar if avto.tabel_raqam not in holat_yaxshi]

# with open("TA_MIR", "wb") as f:
#     pickle.dump(holatlar, f)


