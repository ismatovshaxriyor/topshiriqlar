class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None

class Navbat:
    def __init__(self):
        self.boshi = None

    def Navbatga(self, data):
        node = Node(data)
        if self.boshi is None:
            self.boshi = node
        else:
            current = self.boshi
            while current.Next is not None:
                current = current.Next
            current.Next = node

    def Tozalash(self):
        while self.boshi is not None:
            self.boshi = self.boshi.Next

    def BushNavbat(self):
        if self.boshi is None:
            return True

    def Navbatdan(self):
        bosh = self.boshi
        self.boshi = self.boshi.Next
        print(f"Birinchi navbat: {bosh.Data}")

    def Print(self):
        cur = self.boshi
        while cur is not None:
            print(cur.Data)
            cur = cur.Next

class MUSBAT_MANFIY_NAVBATLAR(Navbat):
    def __init__(self):
        super().__init__()

    def saralash(self, lst):
        self.musbat_navbat = Navbat()
        self.manfiy_navbat = Navbat()
        for i in lst:
            if i > 0:
                self.musbat_navbat.Navbatga(i)
            else:
                self.manfiy_navbat.Navbatga(i)

    def Print_musbat(self):
        cur = self.musbat_navbat.boshi
        while cur is not None:
            print(cur.Data)
            cur = cur.Next

    def Print_manfiy(self):
        cur = self.manfiy_navbat.boshi
        while cur is not None:
            print(cur.Data)
            cur = cur.Next

navbat = Navbat()

navbat.Navbatga(1)
navbat.Navbatga(2)
navbat.Navbatga(3)

# navbat.Tozalash()

# result = navbat.BushNavbat()
# if result == True:
#     print("Navbat bo'sh")
# else:
#     print("Navbat bo'sh emas")

# navbat.Navbatdan()

lst = [1, -2, 3, -4, 5, -6]
MNN = MUSBAT_MANFIY_NAVBATLAR()
MNN.saralash(lst)

MNN.Print_musbat()
MNN.Print_manfiy()