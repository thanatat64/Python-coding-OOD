class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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
 
    def addHead(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def search(self, item):
        current = self.head
        while current is not None:
            if current.value == item:
                return "Found"
            current = current.next
        return "Not Found"

    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            if current.value == item:
                return count
            count += 1
            current = current.next
        return -1

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
        if not (0 <= pos < self.size()):
            return "Out of Range"
        elif pos == 0:
            self.head = self.head.next
        else:
            while count < pos-1 :
                count += 1
                current = current.next
            current.next = current.next.next
        return "Success"
     
L = LinkedList()     
inp = input('Enter Input : ').split(',')
for i in inp:     
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)