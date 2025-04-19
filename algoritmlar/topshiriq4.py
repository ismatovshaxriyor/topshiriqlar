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

    # <=== 1 - topshiriq ===>
    def Count_toq(self):
        count = 0
        tugun = self.root
        while tugun is not None:
            if tugun.Left is None:
                if tugun.Data % 2 == 1:
                    count += 1
                tugun = tugun.Right
            else:
                old_tugun = tugun.Left
                while old_tugun.Right and old_tugun.Right != tugun:
                    old_tugun = old_tugun.Right

                if old_tugun.Right is None:
                    old_tugun.Right = tugun
                    tugun = tugun.Left
                else:
                    if tugun.Data % 2 == 1:
                        count += 1
                    old_tugun.Right = None
                    tugun = tugun.Right
        print("Toq sonlar soni:", count)

    # <=== 2 - topshiriq ===>
    def search(self, num):
        topildi = False
        tugun = self.root
        while tugun is not None:
            if tugun.Left is None:
                if tugun.Data == num:
                    topildi =True
                tugun = tugun.Right
            else:
                old_tugun = tugun.Left
                while old_tugun.Right and old_tugun.Right != tugun:
                    old_tugun = old_tugun.Right

                if old_tugun.Right is None:
                    old_tugun.Right = tugun
                    tugun = tugun.Left
                else:
                    if tugun.Data == num:
                        topildi =True
                    old_tugun.Right = None
                    tugun = tugun.Right
        
        if topildi:
            print(f"{num} soni daraxtda mavjud")
        else:
            print(f"{num} soni daraxtda mavjud emas")

    # <=== 3 - topshiriq ===>
    def chech_brother(self):
        def tekshir(tugun):
            if tugun is None:
                return
            if tugun.Left and tugun.Right:
                print(f"{tugun.Left.Data} va {tugun.Right.Data} aka uka")
            tekshir(tugun.Left)
            tekshir(tugun.Right)

        tekshir(self.root)

    # <=== 4 - topshiriq ===>
    def go_right(self):
        if self.root is None:
            return None

        tugun = self.root
        while tugun.Right is not None:
            tugun = tugun.Right

        print(f"eng uchidagi son: {tugun.Data}")

    def print(self):
        tugun = self.root
        while tugun is not None:
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
daraxt.add(10)
daraxt.add(7)
daraxt.add(2)
daraxt.add(9)
daraxt.add(6)
daraxt.add(8)

daraxt.search(3)
daraxt.chech_brother()
daraxt.go_right()

daraxt.print()

daraxt.Count_toq()
