class Data:
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __str__(self):
        return "({0}, {1})".format(self.key, self.data)

class hash:

    def __init__(self,size,MaxCollision):
        self.size = size
        self.table = [None for i in range(size)] #init table ให้ ทุกช่องเป็น None
        self.maxCollision = MaxCollision

    def isFull(self):
        for i in self.table:
            if i is None: return False
        return True

    def insertQuadatric(self,key: list,data):
        if self.isFull():
            print("This table is full !!!!!!")
            exit()
        summ = 0
        for i in key:
            summ += ord(i)
        index = summ % self.size
        realIndex, colI = index, 0
        while self.table[index] is not None:
            colI += 1
            print(f"collision number {colI} at {index}")
            if colI == self.maxCollision:
                print("Max of collisionChain")
                break
            else:
                index = (realIndex + colI**2) % self.size
        if self.table[index] is None:
            self.table[index] = str(Data(key, data))
        
    def printTable(self):
        for i in range(self.size):
            print("#"+str(i+1)+"	",end="")
            if self.table[i] == None:print(None)
            else:print(self.table[i])
        print("---------------------------")

print(" ***** Fun with hashing *****")
k,lst = input("Enter Input : ").split("/")
sizeOfTable,MaxCollision = map(int,k.split())
H = hash(sizeOfTable,MaxCollision)
for i in lst.split(","):
    H.insertQuadatric(i.split()[0],i.split()[1])
    H.printTable()