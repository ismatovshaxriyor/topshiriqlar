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
    
    def firstZero(self):
        position = 0
        current = self.head
        while current != None:
            if current.Data != 0:
                current = current.Next
                position += 1
            else:
                print(current.Data)
                print(position)
                break

list1 = LList()

list1.Add(1)
list1.Add(1)
list1.Add(0)
list1.Add(3)

list1.firstZero()