class Node:
    def __init__(self,d):
        self.Data = d
        self.Next = None

class LList:
    def __init__(self):
        self.head = None

    def AddFirst(self, data):
        node = Node(data)
        node.Next = self.head
        self.head=node

    def Add(self, data):
        node = Node(data)
        cur = self.head
        if cur != None:
            while cur.Next != None:
                cur = cur.Next
            cur.Next=node
        else:
            self.head=node

    def Insert(self, data, pos):
        node = Node(data)
        cur = self.head
        k = 1

        if cur != None:
            while cur.Next != None and k<pos:
                cur = cur.Next
                k=k+1
            node.Next = cur.Next
            cur.Next = node
        else:
            self.head = node

    def Delete(self,pos):
        cur = self.head
        prev = None
        k = 1
        if cur is not None:
            while cur.Next != None and k < pos:
                prev = cur
                cur = cur.Next
                k = k + 1
            if k<=1:
                self.head = self.head.Next
            else:
                prev.Next = cur.Next



    def Print(self):
        cur =self.head
        while cur != None:
            print(cur.Data)
            cur = cur.Next

l = LList()


l.Add(1)
l.Add(2)
l.Add(3)
l.Delete(2)


l.Print()