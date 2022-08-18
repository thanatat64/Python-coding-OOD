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

l = input("Enter Input : ").split(",")
s = Stack() #สร้าง obj
for x in l:
    x = x.split()  
    if x[0] == 'A':
        s.push(x[1])
        print(f"Add = {x[1]} and Size = {s.size()}")
    else:
        if s.isEmpty():
            print("-1")
        else:
            print(f"Pop = {s.pop()} and Index = {s.size()}")
if s.isEmpty():
    print("Value in Stack = Empty")
else:
    print("Value in Stack =",*s.items)