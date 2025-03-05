class Node:
    def __init__(self, d):
        self.Data = d
        self.Next = None

class LList:
    def __init__(self):
        self.head = None
    
    def AddFirst(self, data):
        node = Node(data)
        node.Next = self.head
        self.head = node

    def Add(self, data):
        node = Node(data)
        current = self.head
        if current != None:
            while current.Next != None:
                current = current.Next
            current.Next = node
        else:
            self.head = node
    
    def output(self):
        current = self.head
        while current != None:
            print(current.Data)
            current = current.Next
    
    # <=== 1 - topshiriq ===>
    def firstZero(self):
        current = self.head
        while current != None:
            if current.Data == 0:
                nextNode = Node(0)
                nextNode.Next = current.Next
                current.Next = nextNode
                current = nextNode
            current = current.Next
    
    # <=== 2 - topshiriq ===>
    def findMin(self):
        min1 = self.head.Data
        current = self.head

        while current != None and current.Next != None:
            min2 = current.Next.Data
            if min1 <= min2:
                current = current.Next
            else:
                min1 = min2
        return min1

    def EndMin(self):
        Min = self.findMin()
        current = self.head
        count = 0

        while current != None:
            if current.Data == Min:
                count += 1
            current = current.Next
        return count

    def EndMinPos(self):
        current = self.head
        endMin = self.findMin()
        count = self.EndMin()
        a = 0

        while current != None and count != 0:
            if current.Data == endMin:
                count -= 1
            a += 1
            current = current.Next
        return a

    def delEndMin(self):
        count = self.EndMin()
        pos = self.EndMinPos()
        cur = self.head
        prev = None
        k = 1
        if cur is not None and count > 1:
            while cur.Next != None and k < pos:
                prev = cur
                cur = cur.Next
                k = k + 1
            if k<=1:
                self.head = self.head.Next
            else:
                prev.Next = cur.Next
        else:
            print(f"o'chirilayotgan element 1 marta uchragan\n")
    
    # <=== 3 - topshiriq ===>
    def juftSonlar(self):
        current = self.head
        juft_sonlar = 0
        while current != None:
            if current.Data % 2 == 0:
                juft_sonlar += 1
            current = current.Next
        print(f"Juft sonlar {juft_sonlar} marta uchragan")
    
    # <=== 4 - topshiriq ===>
    def x(self):
        current = self.head
        while current != None:
            if current.Data % 2 == 1:
                nextNode = Node(current.Data)
                nextNode.Next = current.Next
                current.Next = nextNode
                current = nextNode
            current = current.Next

list1 = LList()

list1.Add(3)
list1.Add(1)
list1.Add(4)
list1.Add(0)
list1.Add(1)
list1.Add(2)
list1.Add(0)
list1.Add(19)

# list1.firstZero()
# list1.juftSonlar()
# list1.delEndMin()
list1.x()


list1.output()