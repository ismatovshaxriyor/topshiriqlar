class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None 

class Stek:
    def __init__(self):
        self.head = None  
        self.count = 0

    def push(self, data):           
        node = Node(data) 
        node.Next = self.head  
        self.head = node  
        self.count += 1

    # <=== 1 - topshiriq ===>
    def get_max(self):
        max_elem = self.head.Data
        current = self.head.Next
        while current is not None:
            if current.Data > max_elem:
                max_elem = current.Data
            current = current.Next
        print(f"Max number: {max_elem}")

    # <=== 3 - topshiriq ===>
    def Count(self):
        count = 0
        current = self.head
        while current is not None:
            if 10 <= current.Data < 100:
                count += 1
            current = current.Next
        print(f"Musbat 2 xonali sonlar {count} ta")


    def pop(self):
        if self.is_empty():
            return "stek bo'sh"
        cur = self.head
        self.head = self.head.Next
        self.count -= 1
        return cur.Data

    def is_empty(self):               
        return self.head is None

    def peek(self):                
        if self.is_empty():
            return "stek bo'sh"
        return self.head.Data

    def print(self):                  
        if self.is_empty():       
            return "stek bo'sh"
        cur = self.head
        while cur is not None:
            print(cur.Data , end=" <=> ")
            cur = cur.Next
        print(None)


stek = Stek()

stek.push(5) 
stek.push(3) 
stek.push(44)
stek.push(555)
stek.push(1000)

stek.get_max()

stek.print()

stek.pop()
stek.pop()
stek.push(20)
stek.push(30)

stek.print()

stek.Count()