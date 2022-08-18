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


inp = input('Enter Infix : ')

print('Postfix : ', end='')
S = Stack()
o_p = ''
OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
PRIORITY_Dic = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
for x in inp:
    if x not in OPERATORS:
        o_p += x
    elif x =='(':  # else Operators push onto stack

            S.push('(')

    elif x ==')':

        while S.items and S.items[-1]!= '(':

            o_p+=S.pop()

        S.pop()
        
    else:
        while S.items and S.items[-1]!='(' and PRIORITY_Dic[x] <= PRIORITY_Dic[S.items[-1]]:
            o_p += S.pop()
            
        S.push(x)
print(o_p, end ='')

while not S.isEmpty():

    print(S.pop(), end='')

print()
