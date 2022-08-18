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