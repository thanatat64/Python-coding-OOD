class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.dummy = Node(None)
        self.dummy.next = self.dummy
        self.dummy.previous = self.dummy

    def __str__(self) -> str:
        if self.isEmpty():
            return ""
        cur, s = self.dummy.next, ""
        while cur != self.dummy:
            s += str(cur.data)
            if cur.next is not self.dummy:
                s += "->"
            cur = cur.next
        return s

    def str_reverse(self):
        if self.isEmpty():
            return ""
        cur, s = self.dummy.previous, ""
        while cur != self.dummy:
            s += str(cur.data)
            if cur.previous is not self.dummy:
                s += "->"
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.dummy.next is self.dummy

    def append(self, data):
        new_node = Node(data)
        if self.dummy.next is self.dummy:
            self.addHead(data)
        else:
            self.dummy.previous.next = new_node
            new_node.previous = self.dummy.previous
            self.dummy.previous = new_node
            new_node.next = self.dummy
        
    def addHead(self, data):
        new_node = Node(data)
        new_node.next = self.dummy.next
        self.dummy.next.previous = new_node
        self.dummy.next = new_node
        new_node.previous = self.dummy
        
    def insert(self, id, data):
        new_node = Node(data)
        current = self.dummy.next
        count = 0
        if id == 0:
            self.addHead(data)

        elif id == self.size():
            self.append(data)
        else:
            while current is not self.dummy:
                if count == id - 1:
                    new_node.next = current.next
                    current.next.previous = new_node
                    current.next = new_node
                    new_node.previous = current
                count += 1
                current = current.next

    def remove(self, data):
        count = -1
        current = self.dummy
        while current.next is not self.dummy and current.next is not None:
            current = current.next
            count += 1
            if current.data == data:
                current.previous.next = current.next
                current.next.previous = current.previous
                return count    
        return -1

    def size(self):
        current = self.dummy.next
        count = 0
        while current is not self.dummy:
            count += 1
            current = current.next
        return count


L = DoublyLinkedList()
inp = input("Enter Input : ").split(",")
for x in inp:
    j = x.split()
    if j[0] == 'A':
        L.append(j[1])
        print(f"linked list : {L}")
        print(f"reverse : {L.str_reverse()}")
    elif j[0] == 'Ab':
        L.addHead(j[1])
        print(f"linked list : {L}")
        print(f"reverse : {L.str_reverse()}")
    elif j[0] == 'I':
        i = j[1].split(":")
        if int(i[0]) < 0 or int(i[0]) > L.size():
            print("Data cannot be added")
            print(f"linked list : {L}")
            print(f"reverse : {L.str_reverse()}")
        elif i[0] == 0:
            L.addHead(i[1])
            print(f"linked list : {L}")
            print(f"reverse : {L.str_reverse()}")
        elif i[0] == L.size():
            L.append(i[1])
            print(f"linked list : {L}")
            print(f"reverse : {L.str_reverse()}")

        else:
            print(f"index = {i[0]} and data = {i[1]}")
            L.insert(int(i[0]), i[1])
            print(f"linked list : {L}")
            print(f"reverse : {L.str_reverse()}")
    elif j[0] == 'R':
        t = L.remove(j[1])
        if t == -1:
            print("Not Found!")
        else:
            print(f"removed : {j[1]} from index : {t}")
        print(f"linked list : {L}")
        print(f"reverse : {L.str_reverse()}")
