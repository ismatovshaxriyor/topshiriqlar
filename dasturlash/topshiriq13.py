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

navbat.Print()