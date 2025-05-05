import pickle
import tkinter as tk


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

with open("dasturlash/topshiriq16/AVTO", "rb") as f:
    avto_lar = pickle.load(f)
    for avto in avto_lar:
        avtolar.append(avto)

with open("dasturlash/topshiriq16/TA_MIR", "rb") as f:
    holat_lar = pickle.load(f)
    for holat in holat_lar:
        holatlar.append(holat)



def A_shart():
    result = []
    for holat in holatlar:
        mashina_holati = holat.holat
        mashina_nomeri = holat.tabel_raqam
        
        try:
            mashina = [avto for avto in avtolar if avto.malumot(mashina_nomeri)]
            if mashina_holati == 1:
                egasi = mashina[0].egasi
                nomeri = mashina[0].nomer
                turi = mashina[0].turi
                result.append((egasi, nomeri, turi))
        except:
            continue
    return result



# # B shart

def B_shart(nomer):
    result = []
    for avto in avtolar:
        try:
            tabel_raqami = avto.nomer_malumot(nomer)
            holati = [holat.holat for holat in holatlar if holat.tex_holat(tabel_raqami)]
            if holati:
                result.append((nomer, umumiy_holarlar.get(holati[0])))
        except:
            continue
    return result


# # C shart
# holat_yaxshi = [holat.tabel_raqam for holat in holatlar if holat.holat == 1]
# avtolar = [avto for avto in avtolar if avto.tabel_raqam not in holat_yaxshi]

# with open("TA_MIR", "wb") as f:
#     pickle.dump(holatlar, f)


def choice():
    shart = input_oyna.get()
    if shart == "1":
        result = A_shart()
        text = ''
        for i in result:
            text += f"Egasi: {i[0]} Nomeri: {i[1]} Turi: {i[2]}\n"
        oyna.geometry("500x500")
        natija_label.config(text=text)
    
    elif shart == "2":
        oyna.geometry("500x500")
        natija_label.config(text="Mashina nomerini kiritng:")
        input_B = tk.Entry(oyna, width=30)
        input_B.pack()

        tugma = tk.Button(oyna, text="submit", command=shart_B)
        tugma.pack(pady=10)

    elif shart == "3":
        oyna.geometry("500x500")
        natija_label.config(text="333")

def shart_B():
    nomer = input_oyna.get()
    result = B_shart(nomer)
    text = ""
    for i in result:
        text += f"{i[0]} nomerli mashina holati {i[1]}"
    natija_label.config(text=text)



oyna = tk.Tk()
oyna.title("Topshiriq 16")
oyna.geometry("400x400")

yorliq = tk.Label(oyna, text="Shartni tanlang:")
yorliq.pack(pady=20)

shart1 = tk.Label(oyna, text="1. A shart")
shart1.pack(pady=10)

shart2 = tk.Label(oyna, text="2. B shart")
shart2.pack(pady=10)

shart3 = tk.Label(oyna, text="3. D shart")
shart3.pack(pady=10)

input_oyna = tk.Entry(oyna, width=30)
input_oyna.pack()

tugma = tk.Button(oyna, text="submit", command=choice)
tugma.pack(pady=10)

natija_label = tk.Label(oyna, text="")
natija_label.pack()

oyna.mainloop()

