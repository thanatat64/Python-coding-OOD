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

    def getHeight(root: Node):
        if root is None:
            return -1
        return 1 + max(BST.getHeight(root.left),BST.getHeight(root.right))
        
        
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Height of this tree is :",BST.getHeight(root))
