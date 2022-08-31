
class Queue:
    def __init__(self, lst=None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def enQueue(self, s):
        self.items.append(s)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[0]


class Stack():
    def __init__(self, lst=None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def push(self, s):
        self.items.append(s)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


lst = input("Enter Input (Normal, Mirror) : ").split(" ")
norW, mirW = Queue(list(lst[0])), Stack(list(lst[1]))
q = Queue()
exploN = 0
exploM = 0
fail = 0

# print(norW.items)
# print(mirW.items)
tmpS = Stack()
count = 0
s = ""
while not mirW.isEmpty():
    if s == mirW.peek():
        count += 1
    else:
        count = 0
        s = mirW.peek()
    tmpS.push(mirW.pop())
    if count == 2:
        exploM += 1
        count = 0
        q.enQueue(s)
        for i in range(3):
            if not tmpS.isEmpty():
                tmpS.pop()
        s = ""
while not tmpS.isEmpty():
    mirW.push(tmpS.pop())

tmpS = Stack()
count = 0
s = ""
while not mirW.isEmpty():
    if s == mirW.peek():
        count += 1
    else:
        count = 0
        s = mirW.peek()
    tmpS.push(mirW.pop())
    if count == 2:
        exploM += 1
        count = 0
        q.enQueue(s)
        for i in range(3):
            if not tmpS.isEmpty():
                tmpS.pop()
        s = ""
while not tmpS.isEmpty():
    mirW.push(tmpS.pop())

# print("Item: ", q.items)


tmpS = Stack()
count = 0
s = ""
while not norW.isEmpty():
    f = norW.deQueue()
    if s == f:
        count += 1
    else:
        count = 0
        s = f
    tmpS.push(f)
    if count == 2:
        if not q.isEmpty():
            t1 = tmpS.pop()
            i1 = q.deQueue()
            t2 = tmpS.pop()
            t3 = tmpS.pop()
            if i1 == t2 == t3:
                fail += 1
            else:
                tmpS.push(t3)
                tmpS.push(t2)
                tmpS.push(i1)
            tmpS.push(t1)
            count = 0
            s = ""
        else:
            i1 = tmpS.pop()
            i2 = tmpS.pop()
            i3 = tmpS.pop()
            exploN += 1
            count = 0
            s = ""

while not tmpS.isEmpty():
    norW.enQueue(tmpS.pop())

tmpS = Stack()
count = 0
s = ""
while not norW.isEmpty():
    f = norW.deQueue()
    if s == f:
        count += 1
    else:
        count = 0
        s = f
    tmpS.push(f)
    if count == 2:
        if not q.isEmpty():
            t1 = tmpS.pop()
            i1 = q.deQueue()
            t2 = tmpS.pop()
            t3 = tmpS.pop()
            if i1 == t2 == t3:
                fail += 1
            else:
                tmpS.push(t3)
                tmpS.push(t2)
                tmpS.push(i1)
            tmpS.push(t1)
            count = 0
            s = ""
        else:
            i1 = tmpS.pop()
            i2 = tmpS.pop()
            i3 = tmpS.pop()
            exploN += 1
            count = 0
            s = ""

while not tmpS.isEmpty():
    norW.enQueue(tmpS.pop())


tmpS = Stack()
count = 0
s = ""
while not norW.isEmpty():
    f = norW.deQueue()
    if s == f:
        count += 1
    else:
        count = 0
        s = f
    tmpS.push(f)
    if count == 2:
        if not q.isEmpty():
            t1 = tmpS.pop()
            i1 = q.deQueue()
            t2 = tmpS.pop()
            t3 = tmpS.pop()
            if i1 == t2 == t3:
                fail += 1
            else:
                tmpS.push(t3)
                tmpS.push(t2)
                tmpS.push(i1)
            tmpS.push(t1)
            count = 0
            s = ""
        else:
            i1 = tmpS.pop()
            i2 = tmpS.pop()
            i3 = tmpS.pop()
            exploN += 1
            count = 0
            s = ""

while not tmpS.isEmpty():
    norW.enQueue(tmpS.pop())

print("NORMAL :")
print(norW.size())
if norW.isEmpty():
    print("Empty")
else:
    print(*norW.items, sep="")
print(f"{exploN} Explosive(s) ! ! ! (NORMAL)")
if fail > 0:
    print(f"Failed Interrupted {fail} Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(mirW.size())
if mirW.isEmpty():
    print("ytpmE")
else:
    print(*mirW.items, sep="")
print(f"(RORRIM) ! ! ! (s)evisolpxE {exploM}")
# while loop ซ้ำ EX DDDFFFGGG CABBBAACC
