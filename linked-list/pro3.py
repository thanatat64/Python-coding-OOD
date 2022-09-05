class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList: #stack
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def pop(self, pos):
        current = self.head
        count = 0
        if pos == 0:
            ans = self.head.value
            self.head = self.head.next
        else:
            while count < pos-1 :
                count += 1
                current = current.next
            ans = current.next.value
            current.next = current.next.next
        return ans
            

def merge(L1 : LinkedList, L2 : LinkedList):
        while not L2.isEmpty():
            L1.append(L2.pop(L2.size() - 1))
        return L1
        

inp = input("Enter Input (L1,L2) : ").split()
L1,L2 = LinkedList(),LinkedList()
for i in inp[0].split("->"): L1.append(i)
for i in inp[1].split("->"): L2.append(i)

print("L1    :",L1)
print("L2    :",L2)
print(f"Merge : {merge(L1,L2)}" )