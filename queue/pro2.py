class Queue:
    def __init__(self,lst = None):
        if lst == None:
            self.items = []
        else:
            self.items = lst
    def enQueue(self,s):
        self.items.append(s)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

lst = input("Enter Input : ").split(",")
qN = Queue()
qS = Queue()
for x in lst:
    if x[0] == 'D':
        if qN.isEmpty() and qS.isEmpty():
            print("Empty")
        else:
            if not qS.isEmpty():
                print(qS.deQueue())
            else:
                print(qN.deQueue())
    elif x[:2] == 'EN':
        qN.enQueue(x[3:])
    elif x[:2] == 'ES':
        qS.enQueue(x[3:])
# print("Check qN: ",qN.items)
# print("Check qS: ",qS.items)
       
