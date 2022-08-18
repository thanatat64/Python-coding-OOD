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


def ManageStack(lst):
    for x in lst:
        x = x.split()
        if x[0] == 'A':
            s.push(x[1])
            print(f"Add = {x[1]}")
        elif x[0] == 'P':
            if s.isEmpty():
                print("-1")
            else:
                print(f"Pop = {s.items[-1]}")
                s.pop()
        elif x[0] == 'D':
            if s.isEmpty():
                print("-1")
            else:
                while not s.isEmpty():
                    t = s.pop()
                    if t == x[1]:
                        print(f"Delete = {t}")
                    else:
                        ns.push(t)
                while not ns.isEmpty():
                    s.push(ns.pop())
        elif x[0] == 'LD':
            if s.isEmpty():
                print("-1")
            else:
                while not s.isEmpty():
                    t = s.pop()
                    if int(t) < int(x[1]):
                        print(f"Delete = {t} Because {t} is less than {x[1]}")
                    else:
                        ns.push(t)
                while not ns.isEmpty():
                    s.push(ns.pop())
        elif x[0] == 'MD':
            if s.isEmpty():
                print("-1")
            else:
                while not s.isEmpty():
                    t = s.pop()
                    if int(t) > int(x[1]):
                        print(f"Delete = {t} Because {t} is more than {x[1]}")
                    else:
                        ns.push(t)
                while not ns.isEmpty():
                    s.push(ns.pop())
    return s.items

l = input("Enter Input : ").split(",")
s,ns = Stack(),Stack()
ManageStack(l)
print("Value in Stack =",[int(i) for i in s.items])
# 
# 5 2 1