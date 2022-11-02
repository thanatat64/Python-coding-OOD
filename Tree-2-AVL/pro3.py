class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = Node.insert(root.left, data)
        else:
            root.right = Node.insert(root.right, data)
        return root

    def printTree(node, level = 0):
        if node != None:
            Node.printTree(node.right, level + 1)
            print('     ' * level, node)
            Node.printTree(node.left, level + 1)

    def rank(root,data):
        if root is None:
            return 0
        if data < root.data:
            return Node.rank(root.left,data)
        else:
            return 1+ Node.rank(root.left,data) + Node.rank(root.right,data)

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = Node.insert(self.root,data)
        return self.root


tree = BST()
data,a = input("Enter Input : ").split("/")
for i in data.split():
    tree.insert(int(i))
tree.root.printTree()
print("-"*50)
print(f"Rank of {a} : {tree.root.rank(int(a))}")



