class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

    def insert(root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = Node.insert(root.left,data)
        else:
            root.right = Node.insert(root.right,data)
        return root

    def delete(root, data):
        if root is None: #tree ว่่าง หรือ หาไม่เจอ
            print("Error! Not Found DATA")
            return None
        if data < root.data: # ข่อมูลที่จะลบอยู่ซ้าย
            root.left = Node.delete(root.left, data) # ลบข้อมูลฝั่งซ้าย
        elif data > root.data: # ข่อมูลที่จะลบอยู่ขวา
            root.right = Node.delete(root.right, data) # ลบข้อมูลฝั่งขวา
        else:# หา data ที่จะลบเจอแล้ว
            if root.left is not None and root.right is not None: # มีลูก 2
                cur = root.right
                while cur.left is not None:
                    cur = cur.left
                root.data, cur.data = cur.data, root.data
                root.right = Node.delete(root.right, data)
            elif root.left is not None:
                return root.left
            elif root.right is not None:
                return root.right
            else:
                return None
        return root
        

class BST:
    def __init__(self): 
        self.root = None

    def insert(self, data):
        self.root = Node.insert(self.root,data)
        return self.root
        
    def delete(self, data):
        self.root = Node.delete(self.root,data)
        return self.root
def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)

tree = BST()
inp = input("Enter Input : ").split(",")
for i in inp:
    if i[0] == "i":
        print("insert",i[2:])
        root = tree.insert(int(i[2:]))
        # BST.insert(tree,i[1:])
        printTree(root)
    if i[0] == "d":
        print("delete",i[2:])
        root = tree.delete(int(i[2:]))
        printTree(root)
