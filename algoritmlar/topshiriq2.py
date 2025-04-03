class Node:
    def __init__(self,data):
        self.Data = data
        self.Next = None
        self.Prev = None

class DList:
    def __init__(self):
        self.head = None
        self.tail = None  
        self.count = 0 

    def Add(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:    
            self.tail.Next = node
            node.Prev = self.tail
            self.tail = node
        self.count += 1

    # <=== 1 - topshiriq ===>
    def doubleItem(self, item):
        current = self.head
        while current is not None:
            if current.Data > item:
                newNode = Node(current.Data)
                newNode.Next = current.Next
                newNode.Prev = current
                if current.Next: 
                    current.Next.Prev = newNode
                current.Next = newNode
                if current == self.tail:
                    self.tail = newNode
                current = newNode
                self.count += 1
            current = current.Next

    # <=== 2 - topshiriq ===>
    def deleteItem(self, item):
        current = self.head
        while current is not None:
            if current.Data == item and current.Next is not None:
                delItem = current.Next
                current.Next = delItem.Next
                if delItem.Next:
                    delItem.Next.Prev = current
                else:
                    self.tail = current
                self.count -= 1
            current = current.Next


    def output(self):
        current = self.head
        while current is not None:
            print(current.Data, end=" <=> ")
            current = current.Next
        print(None)

    def output_reverse(self):
        current = self.tail
        while current is not None:
            print(current.Data, end=" <=> ")
            current = current.Prev
        print(None)

dll = DList()

dll.Add(1)
dll.Add(2)
dll.Add(3)
dll.Add(3)
dll.Add(2)
dll.Add(4)
dll.Add(5)

# dll.doubleItem(3)
dll.deleteItem(2)

dll.output()
dll.output_reverse()