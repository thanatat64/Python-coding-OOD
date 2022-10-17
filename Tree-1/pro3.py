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
    

def powerfulRed(root: Node, k):
    if root is None:
        return
    if root.data > k:
        root.data *= 3
        powerfulRed(root.left,k)
    powerfulRed(root.right,k)
    

T = BST()
inp,k = input('Enter Input : ').split('/')
for i in inp.split():
    root = T.insert(int(i))
T.printTree(root)
print("-"*50)
powerfulRed(root,int(k))
T.printTree(root)
