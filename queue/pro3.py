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
    def getQ(self):
        return self.items

lst = input("Enter Input : ").split("/")
q = Queue(lst[0].split(" "))
# print()
# print("list input :",lst)
     
# print("in queue before process: ",q.items)
lst2 = lst[1].split(",")
# print("list process: ",lst2)
for x in lst2:
    if x[0] == 'E': q.enQueue(x.split(" ")[1])
    if x[0] == 'D': q.deQueue()
# print("in queue after process: ",q.items)
# print()
#print(x)

test = []
temp = q.getQ()
is_dup = False
for i in temp:
    if i not in test:
        test.append(i)
    else:
        is_dup = True
        break

# count = 0
# for i in temp :
#     for j in temp :
#         if i in j : count += 1
# if count > q.size() : print("Duplicate")
if is_dup : print("Duplicate")
else: print("NO Duplicate")
# print(count)