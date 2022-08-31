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
q = Queue()
for x in lst:
    if x[0] == 'E':
        q.enQueue(x[2:])
        print(f"Add {x[2:]} index is {q.size()-1}")
    elif x[0] == "D":
        if q.isEmpty():
            print("-1")
        else:
            print(f"Pop {q.deQueue()} size in queue is {q.size()}")
if q.isEmpty():
    print("Empty")
else:
    print("Number in Queue is : ",q.items)
