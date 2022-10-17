class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = BST._insert(self.root,data)
        return self.root
        
    def _insert(root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = BST._insert(root.left,data)
        else:
            root.right = BST._insert(root.right,data)
        return root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self,n):
        cur = self.root
        while cur is not None and n != cur.data:
            if n > cur.data:
                cur = cur.right
            elif n < cur.data:
                cur = cur.left
        if cur is None:
            print("Not exist")
        elif cur is self.root:
            print("Root")
        elif cur.left is not None or cur.right is not None:
            print("Inner")
        else:
            print("Leaf")

    
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp[1:]:
    root = T.insert(i)
T.printTree(root)
T.checkpos(inp[0])