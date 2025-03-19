class Node:
    def __init__(self, data):
        self.Data = data
        self.Prev = None
        self.Next = None

class DList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        current = self.head
        if current != None:  
            while current.Next:
                current = current.Next
            current.Next = node
            node.Prev = current  
        else:
            self.head = node

    def takrorlash(self, item):
        current = self.head
        while current != None:
            if current.Data > item:
                node = Node(current.Data)
                current.Next = node
                node.Prev = node
            current = current.Next

    def display_forward(self):
        current = self.head
        while current is not None:
            print(current.Data, end=" -> ")
            current = current.Next
        print(None)

    def display_backward(self):
        current = self.head
        while current.Next:
            current = current.Next
        
        while current is not None:
            print(current.Data, end=" -> ")
            current = current.Prev
        print(None)


dll = DList()
dll.append(1)
dll.append(2)
dll.append(0)
dll.append(3)
dll.append(2)
dll.append(4)

dll.takrorlash(2)

dll.display_forward()  
dll.display_backward()