class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def top(self):
        return self.items[-1] if self.size()>0 else -1

    def push(self,tmp):
        self.items.append(tmp)
    
    def pop(self):
        return self.items.pop()

s = Stack()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[0]=='A':
        while int(i[2:])>=s.top() and s.size()>0:
            s.pop()
        s.push(int(i[2:]))
    else:
        print(s.size())