class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Navbat:
    def __init__(self):
        self.head = None  
        self.tail = None   
        self.count = 0

    def EnQueue(self, data):           # Navbatning oxiriga element qo'shish
        node = Node(data)
        if self.head is None:  
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1    

    def DeQueue(self):            # Navbatning boshidan elementni olib tashlash
        if self.head is None:
            return "Navbat bo'sh!"
        else:
            cur = self.head.data
            self.head = self.head.next
            self.count -= 1
            return cur

    def print_head_tail(self):
        print(f"Navbat boshi: {self.head.data}")
        print(f"Navbat oxiri: {self.tail.data}")

    def Print(self):           # Navbatdagi elementlarni chiqarish
        if self.head is None:
            return "Navbat bo'sh!"
        cur = self.head
        while cur is not None:
            print(cur.data, end=" -> ")
            cur= cur.next
        print(None)

navbat1 = Navbat() 
navbat2 = Navbat()

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lst:
    if i % 2 == 1:
        navbat1.EnQueue(i)
    else:
        navbat2.EnQueue(i)

navbat1.Print()
navbat1.print_head_tail()
navbat2.Print()
navbat2.print_head_tail()
