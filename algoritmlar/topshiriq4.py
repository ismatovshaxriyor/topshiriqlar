class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Left = None
        self.Right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, qiymat):
        yangi = Node(qiymat)

        if self.root is None:
            self.root = yangi
            return

        tugun = self.root
        while True:
            if qiymat < tugun.Data:
                if tugun.Left is None:
                    tugun.Left = yangi
                    break
                tugun = tugun.Left
            elif qiymat > tugun.Data:
                if tugun.Right is None:
                    tugun.Right = yangi
                    break
                tugun = tugun.Right
            else:
                break

    def inorder(self):
        tugun = self.root
        while tugun:
            if tugun.Left is None:
                print(tugun.Data)
                tugun = tugun.Right
            else:
                old_tugun = tugun.Left
                while old_tugun.Right and old_tugun.Right != tugun:
                    old_tugun = old_tugun.Right

                if old_tugun.Right is None:
                    old_tugun.Right = tugun
                    tugun = tugun.Left
                else:
                    print(tugun.Data)
                    old_tugun.Right = None
                    tugun = tugun.Right


daraxt = BST()

daraxt.add(5)
daraxt.add(3)
daraxt.add(7)
daraxt.add(2)
daraxt.add(4)
daraxt.add(6)
daraxt.add(8)

daraxt.inorder()  
