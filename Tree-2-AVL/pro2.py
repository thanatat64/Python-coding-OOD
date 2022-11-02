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

    def closestValue(root, value, close = None):
        if root is None:
            return close
        if close is None:
            close = root.data
        else:
            dc = abs(value - close)
            dr = abs(root.data - value)
            if dr < dc:
                close = root.data
            elif dr == dc:
                close = max(root.data,close)     
        L = Node.closestValue(root.left, value, close)
        R = Node.closestValue(root.right, value, close)
        s,m,b = sorted(sorted([close,L,R], reverse=True),key=lambda a: abs(a-value)) #sorted base--> น้อย ---> ไป
        return s
        # 8 4 2/3
        # 5 1 1
        # 1 1 5(sorted)(คือ ความสำคัญ ไม่ใช่ value)
#print    4 2 8
        

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
print(f"Closest value of {a} : {tree.root.closestValue(int(a))}")
#Closest value of -4 : -4



