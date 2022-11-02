class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

    def checkBST(root,mini,maxi):
        if root is None:
            return True
        if root.data < mini or root.data > maxi:
            return False
        return Node.checkBST(root.left, mini, root.data - 1) and Node.checkBST(root.right, root.data + 1, maxi)
        
    def height(root):
        if root == None:
            return -1
        else:
            left = Node.height(root.left)
            right = Node.height(root.right)
            if left>right:
                return left + 1
            else:
                return right + 1

    def insert_subtree(r,num,val):
        if r != None:
            h = Node.height(r)
            max_node = pow(2,h+1)-1
            current = r
            if num+1 > max_node:
                while(current.left != None):
                    current = current.left
                current.left = Node(val)
                return
            elif num+1 == max_node:
                while(current.right != None):
                    current = current.right
                current.right = Node(val)
                return
            if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
                Node.insert_subtree(current.left,num - round(pow(2,h)/2),val)
            else:
                Node.insert_subtree(current.right,num - pow(2,h),val)
        else:
            return
        
    def printTree(node, level = 0):
        if node != None:
            Node.printTree(node.right, level + 1)
            print('     ' * level, node)
            Node.printTree(node.left, level + 1)


class Tree:
    def __init__(self): 
        self.root = None
        self.num = 0

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
            self.num += 1
        else:
            h = Node.height(self.root)
            max_node = pow(2,h+1)-1
            current = self.root
            if self.num+1 > max_node:
                while(current.left != None):
                    current = current.left
                current.left = Node(val)
                self.num+=1
            elif self.num+1 == max_node:
                while(current.right != None):
                    current = current.right
                current.right = Node(val)
                self.num+=1
            else:
                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
                    Node.insert_subtree(current.left,self.num - round(pow(2,h)/2),val)
                else:
                    Node.insert_subtree(current.right,self.num - pow(2,h),val)
                self.num+=1

    def checkBST(self,mini,maxi):
        return Node.checkBST(self.root, mini, maxi)


tree = Tree()
data = input("Enter Input : ").split()
for e in data:
    tree.insert(int(e))
tree.root.printTree()
print(tree.checkBST(0,100))