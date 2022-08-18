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

    def checkHighest(self):
        return self.peek() if self.size() > 0 else 0


inp = input('Enter Input : ').split(',')
s = Stack()
for x in inp:
    #print(x)
    if x[0] == 'A':
        # print(x[2:])
        while int(x[2:]) >= s.checkHighest() and s.size() > 0:
            s.pop()
        s.push(int(x[2:]))
    else:
        print(s.size())
        