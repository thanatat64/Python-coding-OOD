class node:
    def __init__(self,data,next = None):
        self.data = data
        if next == None:
            self.next = None
        else: self.next = next

class list:
    def __init__(self):
        self.head = None
    def append(self,data):
        p = node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p