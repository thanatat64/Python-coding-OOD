class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedlist:
    def __init__(self,data = None):
        self.dummy = Node(None)
        self.cursor = Node('|')
        self.dummy.next = self.cursor
        self.dummy.prev = self.cursor
        self.cursor.prev = self.dummy
        self.cursor.next = self.dummy

    
    def __str__(self):
        if self.__isEmpty__():
            return ""
        cur,s = self.dummy.next, ""
        while cur.next is not self.dummy:
            s += str(cur.data)
            if cur.next is not self.dummy:
                s += " "
            cur = cur.next
        else:
            s += str(cur.data)
        return s

    def __isEmpty__(self):
        return self.dummy.next == self.dummy
    
    def size(self):
        count = 0
        cur = self.dummy.next
        while cur is not self.dummy:
            cur = cur.next
            count += 1
        return count

    def insert(self,data):
        new_node = Node(data)
        new_node.next = self.cursor
        new_node.prev = self.cursor.prev
        self.cursor.prev.next = new_node
        self.cursor.prev = new_node

    def left(self):
        if self.cursor.prev is self.dummy:
            return
        self.cursor.data, self.cursor.prev.data = self.cursor.prev.data, self.cursor.data
        self.cursor = self.cursor.prev

    def right(self):
        if self.cursor.next is self.dummy:
            return
        self.cursor.data, self.cursor.next.data = self.cursor.next.data, self.cursor.data
        self.cursor = self.cursor.next

    def back(self):
        if self.cursor.prev is self.dummy:
            return
        self.cursor.prev = self.cursor.prev.prev
        self.cursor.prev.next = self.cursor

    def delete(self):
        if self.cursor.next is self.dummy:
            return
        self.cursor.next = self.cursor.next.next
        self.cursor.next.prev = self.cursor

inp = input("Enter Input : ").split(',')
L = DoublyLinkedlist()
for i in inp:
    j = i.split()
    if j[0] == 'I':
        L.insert(j[1])
    elif j[0] == 'L':
        L.left()
    elif j[0] == 'R':
        L.right()
    elif j[0] == 'B':
        L.back()
    else:
        L.delete()
print(L)    
