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